#!/usr/bin/env python3
"""Audit latest default-branch GitHub Actions results for public owner repositories.

Historical failures are not counted as current failures. An absent/stale or
running workflow is never reported as a passing CI gate.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import sys
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

API = "https://api.github.com"
UNHEALTHY = {"failure", "timed_out", "action_required", "startup_failure"}


def get_json(url: str) -> dict | list:
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "ie-or-ci-portfolio-audit/1.0"}
    token = os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=25) as response:
        return json.load(response)


def list_public_repositories(owner: str) -> list[dict]:
    all_repos: list[dict] = []
    for page in range(1, 11):
        url = f"{API}/users/{urllib.parse.quote(owner)}/repos?per_page=100&page={page}&type=owner"
        batch = get_json(url)
        if not isinstance(batch, list):
            raise RuntimeError("GitHub repository listing was not an array")
        all_repos.extend(r for r in batch if not r.get("archived") and not r.get("disabled"))
        if len(batch) < 100:
            return all_repos
    raise RuntimeError("repository listing exceeded 1000 records; pagination incomplete")


def classify_runs(head_sha: str, runs: list[dict]) -> tuple[str, list[str]]:
    """Evaluate latest run of each workflow at *current* branch HEAD only."""
    if not runs:
        return "uncovered", []
    current = [r for r in runs if r.get("head_sha") == head_sha]
    if not current:
        return "stale", []
    latest: dict[str, dict] = {}
    for run in current:  # API returns newest first; still sort by run number.
        key = str(run.get("workflow_id") or run.get("name") or run.get("id"))
        prev = latest.get(key)
        score = (run.get("run_number", 0), run.get("run_attempt", 0))
        if prev is None or score > (prev.get("run_number", 0), prev.get("run_attempt", 0)):
            latest[key] = run
    failures = [str(r.get("name") or r.get("workflow_id")) for r in latest.values()
                if r.get("conclusion") in UNHEALTHY]
    if failures:
        return "failure", sorted(failures)
    if any(r.get("status") != "completed" or r.get("conclusion") is None for r in latest.values()):
        return "pending", []
    if any(r.get("conclusion") != "success" for r in latest.values()):
        return "incomplete", []
    return "success", []


def inspect(repo: dict) -> dict:
    name = repo["full_name"]
    branch = repo.get("default_branch") or "main"
    base = f"{API}/repos/{name}"
    try:
        # Resolve exact HEAD to avoid mislabeling stale checks as green.
        ref = get_json(base + "/git/ref/heads/" + urllib.parse.quote(branch, safe=""))
        sha = ref["object"]["sha"]
        payload = get_json(base + "/actions/runs?branch=" + urllib.parse.quote(branch)
                           + "&per_page=100")
        status, failing = classify_runs(sha, payload.get("workflow_runs", []))
        return {"repo": name, "branch": branch, "sha": sha, "status": status,
                "failed_workflows": failing, "url": f"https://github.com/{name}/actions"}
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return {"repo": name, "branch": branch, "status": "error",
                "error": str(exc), "url": f"https://github.com/{name}/actions"}


def render_report(owner: str, results: list[dict]) -> str:
    counts = Counter(r["status"] for r in results)
    lines = [
        f"# CI health audit: {owner}",
        "",
        "Public, non-archived repositories only. Current HEAD and its latest run per workflow "
        "are checked independently; old successes do not satisfy current HEAD.",
        "",
        f"Repositories: {len(results)}. " + ", ".join(
            f"{key}: {counts[key]}" for key in
            ("success", "failure", "pending", "incomplete", "stale", "uncovered", "error")
        ),
        "",
        "| Repository | HEAD coverage | Details |",
        "|---|---|---|",
    ]
    for r in results:
        detail = ", ".join(r.get("failed_workflows", [])) or r.get("error", "") or "-"
        detail = detail.replace("|", "/").replace("\n", " ")[:160]
        lines.append(f"| [{r['repo']}]({r['url']}) | {r['status']} | {detail} |")
    lines += [
        "",
        "Meaning: **success** = all detected current-HEAD workflows passed; "
        "**failure** = at least one current-HEAD workflow failed; "
        "**pending/incomplete** = no confirmed all-green outcome; "
        "**stale** = runs exist but no run for current HEAD; "
        "**uncovered** = no Actions runs returned; "
        "**error** = API evaluation failed.",
        "",
        "This audit does not run all archived-project tests or guarantee that each repo "
        "has comprehensive CI coverage. Private repositories are not included.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--owner", default="alperebalci")
    parser.add_argument("--output", type=Path, default=Path("ci-health.json"))
    parser.add_argument("--summary", type=Path, default=Path("ci-health.md"))
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()
    if args.workers not in range(1, 9):
        parser.error("--workers must be between 1 and 8")
    repos = list_public_repositories(args.owner)
    if not repos:
        raise RuntimeError("No public repositories retrieved: cannot assert portfolio health")
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = sorted(pool.map(inspect, repos), key=lambda item: item["repo"].lower())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.summary.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    report = render_report(args.owner, results)
    args.summary.write_text(report, encoding="utf-8")
    print(report)
    return 1 if any(item["status"] in {"failure", "error"} for item in results) else 0


if __name__ == "__main__":
    sys.exit(main())
