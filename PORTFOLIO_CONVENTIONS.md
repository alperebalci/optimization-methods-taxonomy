# Portfolio Conventions

This document defines the repository-level conventions used across the Jors Academy optimization portfolio.

## Repository roles

### Umbrella

An umbrella repository is the primary entry point for a coherent research area, application domain, problem class, or methodological family.

It may contain:

- **native flagship work** implemented and maintained directly in the repository root or shared package;
- **consolidated projects** preserved under `projects/`;
- **planned research extensions** that are explicitly marked as planned rather than implemented.

### Standalone primary repository

A standalone primary repository is intentionally maintained as an independent work rather than as a container for related projects. Language editions, courses, substantial guides, and focused research systems may use this role.

## Native versus consolidated work

Umbrella repositories should distinguish the provenance of work explicitly.

Recommended status vocabulary:

- `Native flagship` — maintained directly as part of the umbrella repository;
- `Native research` — maintained directly but not designated as flagship;
- `Consolidated snapshot` — imported from a previously separate repository;
- `Planned` — documented research direction without a completed implementation.

Consolidated snapshots should retain a `SOURCE_REPOSITORY.md` record whenever source provenance is available.

## Machine-readable metadata

Primary repositories should contain `PORTFOLIO.yaml` with, at minimum:

```yaml
schema_version: 1
repository: example-repository
role: umbrella
axis: methodology
area: example-area
status: active
owner: jorsacademy
projects:
  - example-project
```

The `axis` field should normally be one of:

- `application`
- `methodology`
- `problem-class`
- `guide`
- `course`
- `standalone`

The central cross-repository registry lives in `PORTFOLIO_REGISTRY.json`.

## Reproducibility standard

Optimization repositories should prefer:

1. explicit mathematical decision models;
2. seeded or otherwise reproducible data generation;
3. independent feasibility checks where practical;
4. objective and KPI baselines;
5. solver status, bound, gap, or convergence diagnostics appropriate to the method;
6. tests for model invariants and result extraction;
7. clear separation between validation-scale examples and claims of industrial scalability;
8. explicit limitations.

## Naming

Repository names should describe the research area rather than implementation trivia. Solver or language names belong in project names only when they are materially relevant.

Prefer:

`vehicle-routing-optimization`

over:

`gurobi-python-vrp-projects`

## Cross-repository navigation

The portfolio is intentionally multi-axis. A repository can simultaneously belong to an application domain and a methodology family.

Use:

- `PORTFOLIO_MAP.md` for human navigation;
- `PORTFOLIO_REGISTRY.json` for central machine-readable grouping;
- repository-level `PORTFOLIO.yaml` for local metadata.

## New umbrella threshold

Do not create a new umbrella merely because one project exists. A new umbrella is justified when at least one of the following holds:

- the repository is a substantial native research platform;
- multiple coherent projects already exist;
- a clear research program with several planned implementations is being actively developed.

Otherwise, prefer a standalone repository until the research area has enough depth to justify an umbrella.
