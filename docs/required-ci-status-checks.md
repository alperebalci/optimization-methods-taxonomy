# Require passing CI before merging into main

## Why this checklist exists

All workflows listed below were observed running at a current-HEAD pull request or default-branch commit on 10 October 2026. A successful workflow run is **not** the same as branch protection: without enforced GitHub rules, a user with write access may still be able to merge a red pull request or push directly.

The connected GitHub integration returned `403 Resource not accessible by integration` for branch-protection reads, and its exposed actions do not support branch-protection writes. Consequently, **the rules below have not been enabled automatically**. A repository administrator must apply and verify them in the GitHub UI.

## Administrator setup for each repository

1. Open the repository's **Settings → Rules → Rulesets**. If unavailable, use **Settings → Branches → Add branch protection rule** as supported by that repository.
2. Create or edit the ruleset targeting the `main` branch.
3. Enable **Require a pull request before merging**.
4. Enable **Require status checks to pass** and select every CI job listed for that repository below. Use the GitHub Actions app as the check source when offered. Select **Require branches to be up to date before merging** when appropriate for the project's merge queue and CI performance.
5. Consider **Block force pushes**, **Restrict deletions**, and **Do not allow bypassing**, subject to the legitimate maintainer/emergency workflow.
6. Save the ruleset, then verify enforcement with an intentionally failing change **on a disposable PR**, not by weakening real CI. Check that an untested branch cannot merge and a green branch can merge.

Do **not** require scheduled/manual-only benchmark or data-hydration workflows as always-on checks. A workflow that commits generated reports or downloads external data should remain explicitly initiated and separately validated.

## Suggested required check names

These are names returned by the repository's GitHub Actions jobs. In the UI, verify the exact display names against the most recent main build before selecting them.

| Repository | Required CI checks |
|---|---|
| [mathematics-for-machine-learning](https://github.com/alperebalci/mathematics-for-machine-learning) | `test` (optimization-for-ml workflow) |
| [pricing-and-revenue-optimization](https://github.com/alperebalci/pricing-and-revenue-optimization) | `test (causal-operations-and-experimentation)`, `test (empirical-operations-and-demand-modeling)` |
| [resource-allocation-optimization](https://github.com/alperebalci/resource-allocation-optimization) | `DEA model tests`, `Market design model tests` |
| [warehouse-and-terminal-optimization](https://github.com/alperebalci/warehouse-and-terminal-optimization) | `solve-and-audit (3.11)`, `solve-and-audit (3.12)` |
| [workforce-optimization-and-analytics](https://github.com/alperebalci/workforce-optimization-and-analytics) | `garment-workforce-planning`, `test` (Service Systems and Queueing workflow) |
| [aviation-operations-optimization](https://github.com/alperebalci/aviation-operations-optimization) | `test (3.10)`, `test (3.11)`, `test (3.12)`, `Dynamic gate reassignment / Python 3.10`, `Dynamic gate reassignment / Python 3.11`, `Dynamic gate reassignment / Python 3.12` |
| [classical-scheduling-optimization](https://github.com/alperebalci/classical-scheduling-optimization) | `test (3.10)`, `test (3.12)`, `jobshoplib-project`, `test` (Project Portfolio and Scheduling workflow) |
| [inventory-optimization-and-control](https://github.com/alperebalci/inventory-optimization-and-control) | `test (3.10)`, `test (3.11)`, `test (3.12)`, `test (3.13)`, `test` (Behavioral Operations workflow) |
| [robust-and-adaptive-supply-chain-optimization](https://github.com/alperebalci/robust-and-adaptive-supply-chain-optimization) | `test (3.10)`, `test (3.11)`, `test (3.12)`, `rl-control`, `test` (System Dynamics for Operations workflow) |
| [optimization-methods-taxonomy](https://github.com/alperebalci/optimization-methods-taxonomy) | `check` (Portfolio map consistency), `validate` (Portfolio Governance) |

The **Cross-repository CI health / audit** workflow is a scheduled diagnostic for other repositories. It is intentionally **not** a required pull-request check: a temporary unrelated repository/API failure should not block merging a correct local patch.

## Known exclusions

- `workforce-optimization-and-analytics`: `benchmark-garment-workforce` and `hydrate-garment-workforce-data` can write generated data/reports; keep them manual/specialized and do not make them required for every main commit.
- `computational-optimization-methods`: the evolutionary-project matrix contains multiple independent heavyweight package builds, currently path-triggered; review before making it a universal required check.
- `industry-4.0-lab`: dataset-dependent benchmarks and optional model toolchains require separate stable data/version contracts before becoming universal required checks.

## Verification of success

After rules are saved, create a throwaway PR with a deliberately failing test. Verify that GitHub blocks the merge until the required checks are green. Record the ruleset name and date in the repository's governance documentation.

**Scope caveat:** ruleset configuration and test adequacy are separate. A green source-only or structural notebook check cannot substitute for model training, numerical feasibility audits, or scientific benchmarks.
