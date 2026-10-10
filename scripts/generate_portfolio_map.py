#!/usr/bin/env python3
"""Generate PORTFOLIO_MAP.md from PORTFOLIO_REGISTRY.json.

Stdlib-only by design so the consistency check can run in a minimal CI job.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "PORTFOLIO_REGISTRY.json"
OUTPUT = ROOT / "PORTFOLIO_MAP.md"


def title_from_slug(slug: str) -> str:
    special = {
        "llm": "LLM",
        "xva": "XVA",
        "qubo": "QUBO",
        "gnn": "GNN",
    }
    return " ".join(special.get(part, part.capitalize()) for part in slug.split("-"))


def render(registry: dict) -> str:
    owner = registry["owner"]
    lines = [
        "# Jors Academy Optimization Portfolio Map",
        "",
        "This map is generated from `PORTFOLIO_REGISTRY.json` and organizes the public Jors Academy portfolio along two independent axes: **application domain** and **methodology**. A repository may appear in more than one conceptual family; the purpose is navigation, not a mutually exclusive taxonomy.",
        "",
        "Portfolio curriculum, coverage analysis, scope decisions, and strategic priorities are maintained in [docs/modern-ie-or-curriculum-and-portfolio-alignment.md](docs/modern-ie-or-curriculum-and-portfolio-alignment.md).",
        "",
        "## By application domain",
        "",
    ]
    for group, repos in registry["domains"].items():
        lines += [f"### {group}", ""]
        for slug in repos:
            title = title_from_slug(slug)
            lines.append(f"- [{title}](https://github.com/{owner}/{slug})")
        lines.append("")

    lines += ["## By methodology", ""]
    for group, repos in registry["methodologies"].items():
        lines += [f"### {group}", ""]
        for slug in repos:
            title = title_from_slug(slug)
            lines.append(f"- [{title}](https://github.com/{owner}/{slug})")
        lines.append("")

    lines += [
        "## Portfolio conventions",
        "",
        "Primary umbrella repositories should:",
        "",
        "1. state their portfolio role near the top of the README;",
        "2. distinguish native flagship work from consolidated snapshots;",
        "3. preserve source provenance for consolidated projects;",
        "4. expose reproducible tests, benchmark assumptions and limitations;",
        "5. prefer a small number of coherent research umbrellas over one repository per small example.",
        "",
        "## Planned methodological gaps",
        "",
    ]
    for slug in registry.get("planned_methodological_umbrellas", []):
        lines.append(f"- `{slug}`")
    lines += [
        "",
        "These entries are planning targets only; they should become top-level umbrellas when dedicated repositories are created.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if PORTFOLIO_MAP.md is stale.")
    args = parser.parse_args()

    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    generated = render(registry)

    if args.check:
        current = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else ""
        if current != generated:
            print("PORTFOLIO_MAP.md is stale. Run scripts/generate_portfolio_map.py")
            return 1
        print("PORTFOLIO_MAP.md is up to date.")
        return 0

    OUTPUT.write_text(generated, encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
