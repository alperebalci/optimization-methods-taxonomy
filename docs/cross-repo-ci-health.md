# Cross-repository CI health audit

The [Cross-repository CI health](../.github/workflows/portfolio-ci-health.yml) GitHub Actions job discovers public, non-archived repositories owned by `alperebalci` and checks the **current default branch HEAD**, not an arbitrary previous green build.

Scheduled daily at 08:23 UTC, manually triggerable, and triggered by changes to its own auditor code. It writes a Markdown job summary and downloadable JSON evidence.

Statuses:

- **success:** every observed workflow on current branch HEAD has a latest successful completed run;
- **failure:** at least one workflow on current HEAD has a latest failed/timed-out/action-required run;
- **pending/incomplete:** no all-green result established on the current commit;
- **stale:** Actions history exists but not on the exact current HEAD SHA;
- **uncovered:** no Actions history returned;
- **error:** public GitHub API lookup failed.

The job fails on **failure** or **error**; it reports stale/uncovered separately rather than disguising them as passing checks. It does not execute tests from other repositories. Public-only results do not cover private repositories or independent snapshots that lack their own CI.

Use the report to prioritize missing workflows. For every new package or imported project, first define its own environment and deterministic tests, then enable branch protection / required status checks in repository settings where supported.

Local, read-only invocation (network and GitHub rate limits apply):

    GH_TOKEN=<your token> python scripts/audit_github_ci.py --owner alperebalci --output ci-health.json --summary ci-health.md

Never commit access tokens or secret-bearing output. The GitHub Actions workflow reads the provided ephemeral token via environment and publishes no token value.
