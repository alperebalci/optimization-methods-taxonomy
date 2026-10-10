#!/usr/bin/env python3
"""Validate cross-repository portfolio metadata and navigation.

The validator intentionally uses only the Python standard library so it can run
on a clean GitHub Actions runner without additional dependencies.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

USER_AGENT = "jorsacademy-portfolio-governance/1.0"


def fetch_text(url: str, retries: int = 3) -> str:
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=20) as response:
                return response.read().decode("utf-8")
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
            if attempt + 1 < retries:
                time.sleep(1.0 + attempt)
    raise RuntimeError(f"failed to fetch {url}: {last_error}")


def parse_portfolio_yaml(text: str) -> tuple[dict[str, str], list[str]]:
    """Parse the deliberately small PORTFOLIO.yaml contract.

    This is not a general YAML parser. The repository contract uses top-level
    scalar keys and a simple string list under projects.
    """
    scalars: dict[str, str] = {}
    projects: list[str] = []
    in_projects = False

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line == "projects:":
            in_projects = True
            continue
        if in_projects:
            stripped = line.strip()
            if stripped == "[]":
                in_projects = False
                continue
            if line.startswith("  - "):
                projects.append(line[4:].strip())
                continue
            if not line.startswith(" "):
                in_projects = False
        if not line.startswith(" ") and ":" in line:
            key, value = line.split(":", 1)
            scalars[key.strip()] = value.strip().strip("\'\\\"")
    return scalars, projects



def validate_sources(catalog: dict, registry: dict) -> list[str]:
    """Pure, offline parity checks: both generated views must share an inventory."""
    errors: list[str] = []
    for field in ("schema_version", "owner"):
        if catalog.get(field) != registry.get(field):
            errors.append(f"catalog/registry {field} mismatch")
    cat_owner = catalog.get("github_owner", catalog.get("owner"))
    reg_owner = registry.get("github_owner", registry.get("owner"))
    if cat_owner != reg_owner:
        errors.append("catalog/registry canonical GitHub owner mismatch")

    slugs = [item["repository"] for item in catalog["repositories"]]
    seen: set[str] = set()
    for slug in slugs:
        if slug in seen:
            errors.append(f"{slug}: duplicate catalog entry")
        seen.add(slug)
    grouped: set[str] = set()
    for dimension in ("domains", "methodologies"):
        for group, items in registry[dimension].items():
            if len(items) != len(set(items)):
                errors.append(f"{dimension}/{group}: duplicate repository")
            grouped.update(items)

    for slug in sorted(grouped - seen):
        errors.append(f"{slug}: in registry/map but missing from catalog/index")
    for slug in sorted(seen - grouped):
        errors.append(f"{slug}: in catalog/index but missing from registry/map")

    planned = registry.get("planned_methodological_umbrellas", [])
    if len(planned) != len(set(planned)):
        errors.append("planned methodological gaps contain duplicates")
    for slug in sorted(set(planned) & seen):
        errors.append(f"{slug}: planned gap already present in active catalog")
    for item in catalog["repositories"]:
        if item.get("role") not in {"umbrella", "standalone", "foundation"}:
            errors.append(f"{item['repository']}: unsupported catalog role")
    return errors

def validate(
    catalog_path: Path,
    map_path: Path,
    registry_path: Path = Path("PORTFOLIO_REGISTRY.json"),
    *,
    inventory_only: bool = False,
) -> int:
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    map_text = map_path.read_text(encoding="utf-8")
    owner = catalog["owner"]
    github_owner = catalog.get("github_owner", owner)
    errors: list[str] = validate_sources(catalog, registry)
    warnings: list[str] = []
    if inventory_only:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Catalog/registry inventory: {len(catalog['repositories'])} repositories, {len(errors)} error(s).")
        return 1 if errors else 0
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    required = {"schema_version", "repository", "role", "axis", "area", "status", "owner"}
    seen: set[str] = set()

    for item in catalog["repositories"]:
        repo = item["repository"]
        branch = item.get("default_branch", "main")
        if repo in seen:
            errors.append(f"{repo}: duplicate catalog entry")
            continue
        seen.add(repo)
        raw_base = f"https://raw.githubusercontent.com/{github_owner}/{repo}/{branch}"
        try:
            metadata_text = fetch_text(f"{raw_base}/PORTFOLIO.yaml")
        except RuntimeError as exc:
            errors.append(f"{repo}: {exc}")
            continue
        metadata, projects = parse_portfolio_yaml(metadata_text)
        missing = sorted(required - metadata.keys())
        if missing:
            errors.append(f"{repo}: missing metadata fields: {', '.join(missing)}")
            continue
        expected = {"repository": repo, "role": item["role"], "axis": item["axis"], "area": item["area"], "owner": owner}
        for key, expected_value in expected.items():
            if metadata.get(key) != expected_value:
                errors.append(f"{repo}: {key}={metadata.get(key)!r}, expected {expected_value!r}")
        if metadata.get("schema_version") != str(catalog["schema_version"]):
            errors.append(f"{repo}: schema_version={metadata.get('schema_version')!r}, expected {catalog['schema_version']!r}")
        if metadata.get("status") not in {"active", "maintenance", "archived"}:
            errors.append(f"{repo}: unsupported status {metadata.get('status')!r}")
        try:
            readme = fetch_text(f"{raw_base}/README.md")
        except RuntimeError as exc:
            errors.append(f"{repo}: {exc}")
            continue
        if item["role"] == "umbrella":
            if "<!-- portfolio-umbrella:start -->" not in readme:
                errors.append(f"{repo}: missing portfolio-umbrella:start marker")
            if "<!-- portfolio-umbrella:end -->" not in readme:
                errors.append(f"{repo}: missing portfolio-umbrella:end marker")
        if item["role"] == "umbrella" and not projects:
            warnings.append(f"{repo}: metadata currently lists no projects; verify whether this should remain an umbrella")
        expected_link = f"https://github.com/{github_owner}/{repo}"
        if expected_link not in map_text:
            errors.append(f"{repo}: missing from PORTFOLIO_MAP.md")

    print(f"Validated {len(seen)} portfolio repositories: {len(errors)} error(s), {len(warnings)} warning(s).")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1 if errors else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", type=Path, default=Path("portfolio/catalog.json"))
    parser.add_argument("--map", dest="map_path", type=Path, default=Path("PORTFOLIO_MAP.md"))
    parser.add_argument("--registry", type=Path, default=Path("PORTFOLIO_REGISTRY.json"))
    parser.add_argument("--inventory-only", action="store_true", help="Check local inventory without network.")
    args = parser.parse_args()
    return validate(args.catalog, args.map_path, args.registry, inventory_only=args.inventory_only)


if __name__ == "__main__":
    raise SystemExit(main())
