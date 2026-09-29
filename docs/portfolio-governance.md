# Portfolio Governance

The Jors Academy optimization portfolio is organized as a small number of primary repositories rather than one repository per example. This document defines the metadata and navigation contract used to keep that structure coherent as the portfolio grows.

## Repository roles

### Umbrella

An umbrella repository is the primary entry point for a research area, application domain, or optimization problem family.

It may contain:

- native flagship implementations at repository root or in a shared package;
- consolidated source-project snapshots under `projects/`;
- common tests, benchmarks, fixtures, documentation, and experiment infrastructure.

Consolidated snapshots should preserve provenance through a `SOURCE_REPOSITORY.md` record when applicable.

### Standalone primary repository

A standalone primary repository contains a coherent research asset that should remain independent rather than being used as a container for smaller repositories.

Language editions of the same guide may remain separate when they serve distinct audiences, but they should cross-link explicitly.

## Metadata contract

Primary umbrella repositories contain a root-level `PORTFOLIO.yaml`.

The current schema is intentionally small:

```yaml
schema_version: 1
repository: vehicle-routing-optimization
role: umbrella
axis: problem-class
area: vehicle-routing
status: active
owner: jorsacademy
projects:
  - capacitated-vrp-branch-and-cut-python
  - stochastic-cvrp-sample-average-approximation-python
conventions:
  provenance_records: true
  reproducibility_expected: true
  benchmark_assumptions_documented: true
```

The controlled top-level fields are:

- `schema_version`: metadata schema version;
- `repository`: GitHub repository slug without owner;
- `role`: currently `umbrella` for governed umbrella repositories;
- `axis`: `application`, `methodology`, or `problem-class`;
- `area`: stable machine-readable research-area identifier;
- `status`: `active`, `maintenance`, or `archived`;
- `owner`: GitHub owner;
- `projects`: projects represented under the umbrella.

The central expected values are recorded in `portfolio/catalog.json`.

## README contract

Umbrella repositories use the markers:

```html
<!-- portfolio-umbrella:start -->
...
<!-- portfolio-umbrella:end -->
```

The marked section declares the repository's role in the consolidated portfolio.

README content should distinguish conceptually between:

1. **native flagship research** — active implementations maintained directly in the umbrella;
2. **consolidated snapshots** — projects imported under `projects/` with provenance;
3. **planned extensions** — explicit research directions that are not yet represented as complete implementations.

A native root implementation does not need to be moved under `projects/`; the README should simply make the distinction clear.

## Navigation

`PORTFOLIO_MAP.md` is the curated human-facing map. It intentionally supports multiple views because the repository graph is not a strict tree: a project can be an application of one method while belonging to another problem class.

The map is therefore navigational rather than a claim that each repository has exactly one intellectual parent.

## Automated validation

`scripts/portfolio_governance.py` validates every repository listed in `portfolio/catalog.json`.

The audit checks:

- required metadata fields exist;
- repository, role, axis, area, owner, and schema version match the catalog;
- umbrella README markers are present;
- every governed repository appears in `PORTFOLIO_MAP.md`;
- suspicious empty project lists are reported as warnings.

The GitHub Actions workflow runs on relevant changes, on manual dispatch, and on a daily schedule so drift in other repositories can be detected even though those changes do not trigger this repository directly.

## Adding a new umbrella

1. Create the repository only when the area is broad enough to sustain multiple coherent research projects.
2. Add the portfolio-role block to the README.
3. Add `PORTFOLIO.yaml`.
4. Add the repository to `portfolio/catalog.json`.
5. Add it to the appropriate sections of `PORTFOLIO_MAP.md`.
6. Run:

```bash
python scripts/portfolio_governance.py
```

7. Keep native and consolidated project status explicit.

## Current intentional gaps

The portfolio currently has strong application-level robust optimization work and several decomposition implementations, but two method families still merit dedicated top-level umbrellas when repositories are created:

- robust and distributionally robust optimization;
- decomposition and large-scale optimization beyond Benders alone.

Until those repositories exist, related implementations remain discoverable through their current domain umbrellas and the curated portfolio map.
