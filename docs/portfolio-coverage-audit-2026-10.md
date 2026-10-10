# IE/OR portfolio coverage audit — 10 October 2026

## Audit boundary

This is a repository-level reconciliation of external feedback against the current portfolio inventory, README documentation, and selected project code/file trees. It verifies **visibility and implementation location**, not the correctness or completeness of all algorithmic claims. Do not infer industrial maturity from the existence of a project.

## Confirmed structural fixes

- `PORTFOLIO_REGISTRY.json` contained **44** unique active entries; `portfolio/catalog.json` contained **40**. The previously unindexed entries were `decomposition-and-large-scale-optimization`, `robust-and-distributionally-robust-optimization`, `performative-optimization`, and `constraint-learning-for-industrial-engineering`.
- The regenerated catalog/index now include those four, plus the previously uncatalogued but existing `time-series-intelligence` and `decision-framing-and-sequential-decision-modeling`, both relevant to foundational IE/OR navigation. The map and index now both resolve to **46** unique active repositories.
- The historical `jorsacademy` repository namespace redirects to the `alperebalci` account. Map and index links use the latter's canonical URLs, while the historical `PORTFOLIO.yaml` metadata-owner contract is preserved until deliberate repository-by-repository migration.
- An offline audit now checks registry/catalog inventory parity and can fail CI before live GitHub checks. The generated-map and generated-index checks remain separate.

## Feedback judged already represented, not absent

| Criticism | Concrete existing evidence | Interpretation |
|---|---|---|
| Queueing / stochastic service systems absent | Workforce Erlang C and simulation; Jackson capacity network in simulation umbrella | Already implemented; broader distributional models remain useful |
| DES absent | Manufacturing event-calendar simulation with failures, finite buffers, warm-up, CRN and paired out-of-sample evaluation | Already implemented; improve input modeling/variance reduction |
| Statistics / causality / forecasting absent | SPC/DOE in manufacturing; ATE/DiD/AIPW in pricing; time-series demand/decision benchmark | Already implemented, previously under-discoverable |
| Game theory and market design absent | Stackelberg security, network interdiction, VCG assignment and stable matching | Already implemented for bounded examples; generic bilevel solvers remain a gap |
| Constraint programming, metaheuristics, multi-objective, MPC, facility layout, online optimization only in book | CP-SAT scheduling, ALNS, NSGA-II, QPALM MPC, facility QAP, dynamic CVRPTW | Existing code, previously missing from a topic-to-code index |
| OR in production entirely absent | Closed-loop production planning with data contracts, fallback, override, feedback and drift trigger | Decision-system prototype exists; deployable solver APIs and runtime monitoring remain incomplete |
| GPU first-order optimization absent | Sparse CPU matrix-free PDHG exists | GPU path is genuinely not evidenced; do not imply existing GPU acceleration |

Detailed and directly clickable project paths appear in [the book-to-code crosswalk](book-to-code-crosswalk.md).

## Remaining capabilities, in order of practical evidence value

1. **Simulation input/output statistics.** Within `simulation-optimization-and-uncertainty-quantification`, add input-distribution fitting, input uncertainty/validation, multiple-replication output diagnostics and further variance-reduction estimators. Require calibrated/held-out input checks, coverage studies, matched simulation budgets and failure-case tests. Do not recreate the DES/CRN project.
2. **General bilevel and equilibrium models.** Extend `resource-allocation-optimization` beyond existing small Stackelberg and interdiction cases with explicit leader/follower objectives, optimistic/pessimistic tie handling, proven follower-optimal responses, and exact small-instance oracles. Larger instances would require independently checked KKT/MPEC or decomposition formulations.
3. **Operational decision service engineering.** Extend the closed-loop production demonstration with a versioned solver API, idempotency, timeouts, audit trails, fallback guarantees, live input-drift and infeasibility monitoring, and rollback tests. Distinguish illustrative service software from a live deployed system.
4. **Genuine GPU LP acceleration.** Build on the existing CPU PDHG reference with device kernels, numerical parity tests, sparse matrix memory accounting, convergence diagnostics and hardware-documented comparisons to CPU PDHG and HiGHS. Do not label a CPU implementation GPU-accelerated or present first-order relaxations as a full MIP solver.
5. **Broader applications only where supported by decision data.** Disaster logistics, public systems, platform/retail operations, cloud/telecom service allocation and lifecycle/sustainability trade-offs can be nested in existing routing, workforce, resource allocation, or energy umbrellas. Do not open empty sector repositories to satisfy a checklist.

## Publishing rule

Promote `Planned` to `Implemented` only when a named code path, independent verification test, reproducible baseline, constraints/feasibility checks and documented limits exist. Avoid equating the number of repository names with depth or academic evidence. The goal is broader **methodological completeness and testable systems**, not repository-count inflation.
