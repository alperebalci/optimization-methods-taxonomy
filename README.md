# Optimization Methods Taxonomy

<!-- portfolio-umbrella:start -->
## Portfolio role

This repository is the primary umbrella repository for this Jors Academy research area. Related projects have been consolidated under `projects/` so the methods, implementations, experiments, and case studies can be maintained and explored from one place.

### Native flagship

The repository root contains the actively maintained **multi-axis optimization-methods taxonomy and learning guide** described below. The entries under `projects/` are consolidated companion projects.

### Included projects

- [`integer-programming-for-operations-research`](projects/integer-programming-for-operations-research/)
- [`intertemporal-optimization-for-operations-research`](projects/intertemporal-optimization-for-operations-research/)
- [`optimizasyon-yontemleri-taksonomisi`](projects/optimizasyon-yontemleri-taksonomisi/)

Each consolidated project keeps its own files and a `SOURCE_REPOSITORY.md` provenance record. The snapshot preserves the source repository's default-branch files at consolidation time; repository-level history and metadata remain separate from the snapshot.
<!-- portfolio-umbrella:end -->

> Portfolio navigation: see [PORTFOLIO_MAP.md](PORTFOLIO_MAP.md) for the cross-repository map by application domain and methodology.
>
> Portfolio standards: see [PORTFOLIO_CONVENTIONS.md](PORTFOLIO_CONVENTIONS.md) for repository roles, provenance, metadata, and reproducibility conventions.
>
> Machine-generated index: see [PORTFOLIO_INDEX.md](PORTFOLIO_INDEX.md), derived from [portfolio/catalog.json](portfolio/catalog.json).
>
> Portfolio governance: see [docs/portfolio-governance.md](docs/portfolio-governance.md) for the metadata contract and automated cross-repository audit.
>
> CI merge-protection checklist: see [docs/required-ci-status-checks.md](docs/required-ci-status-checks.md) for repository-specific required checks and administrator setup.
>
> Curriculum and portfolio alignment: see [docs/modern-ie-or-curriculum-and-portfolio-alignment.md](docs/modern-ie-or-curriculum-and-portfolio-alignment.md) for the modern IE/OR curriculum, cross-repository coverage, scope decisions, and portfolio priorities.
>
> Book-to-code crosswalk: see [docs/book-to-code-crosswalk.md](docs/book-to-code-crosswalk.md) for verified implementations corresponding to the book's topics, with explicitly marked gaps.
>
> Coverage audit: see [docs/portfolio-coverage-audit-2026-10.md](docs/portfolio-coverage-audit-2026-10.md) for the evidence-backed review of IE/OR methods and remaining priorities.
>
> Decision science and management coverage: see [docs/decision-science-and-management-coverage-2026-10.md](docs/decision-science-and-management-coverage-2026-10.md) for normative, behavioral, multi-criteria and organizational decision evidence and limits.
>
> University research crosswalk (2026/27): see [docs/2026-university-ie-or-research-crosswalk.md](docs/2026-university-ie-or-research-crosswalk.md) for official curriculum references, evidence gaps, completion criteria, and the twelve-week implementation order.

A practical, concept-first guide to classifying optimization models and algorithms without mixing independent concepts.

Optimization terminology is often taught as if methods belong to one simple tree: *exact vs. heuristic*, *deterministic vs. stochastic*, or *local vs. global*. That is convenient, but incomplete. These labels describe **different properties**. A single algorithm can belong to several categories at the same time.

This repository builds a clean mental model for those categories, explains where the boundaries are, and shows how to classify common optimization methods consistently.

> **Core idea:** optimization methods should be described along multiple independent axes, not forced into one mutually exclusive taxonomy.

## The four distinctions to learn first

1. **Exact vs. non-exact** describes the type of solution guarantee.
2. **Deterministic vs. stochastic** describes whether algorithmic randomness is used.
3. **Local vs. global search** describes the scope of the search process, not necessarily the guarantee obtained.
4. **Single-solution vs. population-based** describes the search representation.

Therefore:

- `exact` does **not** mean `deterministic`;
- `stochastic` does **not** mean `heuristic`;
- `global search` does **not** automatically mean `global-optimum guarantee`;
- `metaheuristic` does **not** automatically mean `population-based`;
- a `deterministic model` is not the same concept as a `deterministic algorithm`.

## A compact classification map

| Axis | Typical categories | Main question |
|---|---|---|
| Solution guarantee | Exact, approximation, heuristic, metaheuristic | What can be guaranteed about solution quality or optimality? |
| Randomness | Deterministic, stochastic/randomized | Does the algorithm use randomness? |
| Search scope | Local, global | Does it search a neighborhood or attempt broader/global exploration? |
| Search representation | Single-solution, population-based | Does it evolve one incumbent or many candidates? |
| Decision-variable domain | Continuous, discrete/integer, mixed, combinatorial | What kinds of decisions are being optimized? |
| Mathematical structure | Linear, nonlinear, convex, nonconvex, quadratic, nonsmooth, black-box | What structure does the model expose? |
| Constraint structure | Unconstrained, constrained, hard constraints, soft constraints | How is feasibility defined and enforced? |
| Number of objectives | Single-objective, multi-objective | Is there one objective or a trade-off among several? |
| Uncertainty model | Deterministic, stochastic, robust, fuzzy | How is uncertainty represented? |
| Time/information | Static, dynamic, online, real-time | Does information or system state evolve over time? |
| Computational organization | Centralized, distributed | Where are decisions and computations performed? |
| Model access | Model-based, model-free, surrogate-based | How much of the underlying system is known? |
| Search information | First-order, second-order, derivative-free / zeroth-order | What information guides the search? |

## Recommended learning path

Read the guide in this order:

1. [Foundations: how to think about optimization taxonomies](docs/01-foundations.md)
2. [Solution guarantees: exact, approximation, heuristic, metaheuristic](docs/02-solution-guarantees.md)
3. [Randomness, local/global search, exploration and exploitation](docs/03-randomness-and-search.md)
4. [Search representation and metaheuristic families](docs/04-search-representation-and-metaheuristics.md)
5. [Problem domains and mathematical structure](docs/05-problem-structure.md)
6. [Constraints, objectives and uncertainty](docs/06-constraints-objectives-uncertainty.md)
7. [Time, distribution and model access](docs/07-time-distribution-and-model-access.md)
8. [Hybrid methods and matheuristics](docs/08-hybrid-methods.md)
9. [Multi-dimensional comparison matrix](docs/09-comparison-matrix.md)
10. [How to classify any optimization algorithm](docs/10-classification-workflow.md)
11. [Common confusions and FAQ](docs/11-common-confusions.md)
12. [Algorithm and method index](docs/12-algorithm-index.md)
13. [Computational complexity for optimization](docs/13-computational-complexity.md)
14. [Benchmarking and experimental methodology](docs/14-benchmarking-experimental-methodology.md)
15. [Explainable optimization](docs/15-explainable-optimization.md)
16. [Operations Research software ecosystem: modelers, solvers and specialized engines](docs/16-or-software-ecosystem.md)
17. [Learning-enabled and AI-powered optimization](docs/17-learning-enabled-optimization.md)

## A first example: classify Genetic Algorithm correctly

A Genetic Algorithm is not simply “a stochastic method.” A more complete description is:

- **solution guarantee:** metaheuristic; generally no finite-time optimality guarantee,
- **randomness:** usually stochastic,
- **search scope:** global-search-oriented,
- **representation:** population-based,
- **search mechanism:** evolutionary,
- **information requirement:** typically derivative-free,
- **problem domain:** can be adapted to continuous, discrete, mixed or combinatorial problems.

The same multi-label description should be used for other algorithms.

## A second example: classify Branch and Bound correctly

Branch and Bound is typically:

- **solution guarantee:** exact when allowed to complete under the required assumptions,
- **randomness:** usually deterministic, although randomized branching or tie-breaking is possible,
- **search scope:** global in the sense that it systematically partitions the feasible search space,
- **representation:** a search tree rather than a population,
- **problem domain:** especially important for discrete, integer and global optimization models.

So “exact = deterministic” is not a definition. Determinism is an implementation property; exactness is a guarantee property.

## Terminology convention used in this repository

Optimization literature is not perfectly uniform. Some authors use *approximate method* as a broad umbrella containing approximation algorithms, heuristics and metaheuristics. Others reserve *approximation algorithm* for algorithms with a proven approximation ratio, especially in theoretical computer science.

This repository uses the following practical convention:

- **Exact method:** can establish an optimal solution or a valid optimality certificate under stated assumptions.
- **Approximation algorithm:** has a provable bound relative to the optimum, such as an approximation ratio.
- **Heuristic:** aims to find a good solution efficiently without a general optimality or approximation guarantee.
- **Metaheuristic:** a reusable high-level search framework that organizes exploration and exploitation, typically without a general finite-time optimality guarantee.

These definitions are intentionally explicit so the terms are not used interchangeably.

## Scope

The guide covers classical mathematical programming, combinatorial optimization, continuous optimization, metaheuristics, multi-objective optimization, robust and stochastic optimization, online/dynamic optimization, black-box optimization, surrogate methods, distributed optimization and hybrid exact–heuristic methods. It also maps the Operations Research software ecosystem, separating algebraic modeling languages and modeling frameworks from numerical solvers, constraint-programming engines, routing/planning systems, and uncertainty-specific packages. It also separates computational complexity from empirical runtime, provides a reproducible benchmarking framework, introduces optimization-specific explanation tools such as sensitivity analysis, counterfactual re-optimization, and inverse optimization, and distinguishes learning-enabled optimization from generic "AI-powered" marketing claims. The final algorithm index consolidates the named methods used throughout the tutorial into one searchable appendix.

It is a **taxonomy and conceptual guide**, not a replacement for a full textbook on convergence theory, computational complexity, numerical linear algebra, or solver implementation.

## Language

This is the English edition. A Turkish edition can mirror the same structure without changing the technical taxonomy.
