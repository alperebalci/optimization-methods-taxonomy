# University IE/OR research crosswalk and evidence backlog (2026/27)

**Snapshot:** 10 October 2026. This is a portfolio action plan, not a university ranking, admissions prediction, degree equivalency claim, or certification of research quality. It complements [the existing IE/OR curriculum alignment](modern-ie-or-curriculum-and-portfolio-alignment.md) and [the experimental-methodology guide](14-benchmarking-experimental-methodology.md).

## Interpretation

A repository or project being *present* is not the same as a research result being *demonstrated*. The links below establish visible topic coverage. The open tasks target **evidence quality**: valid mathematics, appropriate baselines, independent feasibility audits, held-out experiments, performance at scale, and real-world relevance.

| Institution / official reference | Representative IE/OR emphasis | Existing repository starting point | Evidence to add (not a new topic repository) |
|---|---|---|---|
| [MIT ORC: master's curriculum](https://orc.mit.edu/academics/masters-operations-research/) | Optimization, applied probability, statistics, real-world research | `stochastic-programming-methods`, `simulation-optimization-and-uncertainty-quantification` | A stochastic decision study with held-out scenarios, paired seeds, confidence intervals, and explicit decision costs |
| [UC Berkeley IEOR](https://ieor.berkeley.edu/research/optimization-algorithms/) | Convex/nonconvex and integer/combinatorial optimization, scalable algorithms | `computational-optimization-methods`, `learning-augmented-optimization-solvers` | Matched-instance exact/learning-augmented solver comparisons, with wall time, valid bound/gap, ablations, and OOD cases |
| [Michigan IOE](https://ioe.engin.umich.edu/undergraduate/major-in-ioe/areas-of-study/) | Quality engineering, DOE, human systems, industrial service/production | `manufacturing-systems-optimization`, `workforce-optimization-and-analytics` | Extend existing SPC/DOE/ergonomic tests to process stability, measurement uncertainty, worker safety and a documented operational baseline |
| [Cornell ORIE MEng](https://www.duffield.cornell.edu/orie/degree/operations-research-information-engineering-meng-ithaca-campus-requirements/) | Optimization, stochastic modeling, data science/statistical modeling | `stochastic-programming-methods`, `sequential-decision-analytics` | Separate estimation/training from out-of-sample decision evaluation; quantify when improved prediction fails to improve decisions |
| [Carnegie Mellon Tepper OR](https://www.cmu.edu/tepper/faculty-and-research/academic-areas/operations-research/) | OR theory, algorithms, decision pipeline from data to actions | `learning-augmented-optimization-solvers`, `decomposition-and-large-scale-optimization` | Compare learned solver interventions with strong classical controls; demonstrate correctness under fallback and test performance claims independently |
| [RWTH Aachen: GCG](https://gcg.or.rwth-aachen.de/doc-3.5.0/devs.html) | Decomposition, column generation, branch-and-price, solver internals | `decomposition-and-large-scale-optimization`, `vehicle-routing-optimization` | A solver-integrated branch-and-price case study with pricing correctness, bound tracking and published configurations (not merely an algorithm sketch) |
| [TUM OR lecture, 2026](https://www.cs.cit.tum.de/en/dss/teaching/summer-semester-2026/operations-research-modul-in0025-ss26-1/) | LP duality, ILP, networks, column generation, convex/online optimization | `graph-algorithms-and-network-optimization`, `computational-optimization-methods` | Mathematical derivations and small exact counterexamples/oracles for representative online or large-scale methods |
| [Dauphine-PSL MODO, 2026/27](https://dauphine.psl.eu/formations/masters/informatique/m2-modelisation-optimisation-decision-et-organisation/programme) | Multi-criteria decisions, preferences, robust OR, graph algorithms, organization | `management-science`, `resource-allocation-optimization` | Show stakeholder preferences, robustness of rankings, sensitivity to weights and human override outcomes |
| [Paris-Saclay M2 Optimization](https://www.universite-paris-saclay.fr/en/education/masters-degree/mathematics-and-applications/m2-optimization) | Optimal control, game theory, stochastic optimization, analysis | `sequential-decision-analytics`, `robust-and-distributionally-robust-optimization` | Explicit assumptions/guarantees and small theoretical proofs or counterexamples paired with numerical experiments |
| [LSE MSc OR and Analytics, 2026/27](https://www.lse.ac.uk/study-at-lse/graduate/msc-operations-research-and-analytics) | Applied optimization, stochastic simulation, ML and organizational decisions | `management-science`, `pricing-and-revenue-optimization` | One realistic end-to-end decision case with calibrated uncertainty, operational KPI and limitations |
| [Warwick: Problem Structuring, 2026](https://courses.warwick.ac.uk/modules/2026/IB3A7-15) | Systems thinking, causal mapping, problem structuring, soft OR | `decision-framing-and-sequential-decision-modeling`, `production-planning-optimization` | Stakeholder map, problem boundary, assumptions, alternative objectives, interventions and deployment/override evaluation |
| [Edinburgh MSc OR with Computational Optimization](https://maths.ed.ac.uk/studying-here/msc/or/study-programme/msc-or-with-computational-optimization) | Theory, solver implementation, high-performance computation | `learning-augmented-optimization-solvers`, `computational-optimization-methods` | Scale curves and resource-aware runs on controlled hardware; distinguish CI correctness from research performance |

Institutional pages give representative topics, not a complete or fixed syllabus. Published course lists may change. The repository titles above identify **existing work**, not verified publication-grade results. Crosswalk links target the inspected `alperebalci` account; organization mirrors in the legacy catalog should be checked for canonical status before publishing externally.

## Confirmed existing scope: do not recreate

- SPC, factorial DOE and ergonomics: `manufacturing-systems-optimization`.
- Causal operations experiments: `pricing-and-revenue-optimization/projects/causal-operations-and-experimentation`.
- Behavioral newsvendor decisions: `inventory-optimization-and-control/projects/behavioral-operations-and-human-decision-making`.
- Mechanism design and fairness: `resource-allocation-optimization`.
- Queuing and service operations: `workforce-optimization-and-analytics`.
- Closed-loop operational decisions and human override: `production-planning-optimization/projects/closed-loop-production-decision-system`.

Healthcare/public service is explicitly **out of scope** in the existing curriculum governance document; do not classify it as an unresolved implementation defect.

## Priority evidence backlog

| Priority | Target | Required repository change | Acceptance test |
|---|---|---|---|
| P0 | `learning-augmented-optimization-solvers` | Resolve invalid presolve residuals and repeated-row elimination on the open matched-study PR | Python 3.11/3.12 CI passes; original and reduced model optima agree on edge cases |
| P1 | `learning-augmented-optimization-solvers` | Complete classical/expert/learned matched-instance campaigns | Identical instance fingerprints; matched budgets; baseline/ablation; exactness and fallback checks; seed-level CSV/JSON plus summary |
| P1 | `manufacturing-systems-optimization` | Record small-oracle vs large-instance evidence separately | Small exact oracle + independent audit; large-case wall time, memory/scale, solver status, gap where available |
| P1 | `simulation-optimization-and-uncertainty-quantification` | Out-of-sample statistical uncertainty campaign | Distinct calibration/test replications, interval coverage study, paired common-random-number comparison where valid |
| P2 | `production-planning-optimization` | Real-data/decision-loop case | Dataset license, timestamps, leakage audit, operator override, monitoring and operational KPI |
| P2 | `optimization-methods-taxonomy` | Cross-repo claim/evidence navigation | One canonical project per claim, evidence link, reproducibility command, claim limitations; avoid redundant repos |

## Minimum publishable research evidence package

An empirical claim becomes **reviewable** when the project contains:

1. **Question & hypotheses:** a falsifiable claim and relevant prior work.
2. **Model & guarantees:** mathematical objective/constraints; whether the method is exact, bounded or heuristic.
3. **Provenance:** data origin, permitted use, synthetic/real labels, generator version, immutable instance fingerprint.
4. **Experiment contract:** seeds, train/validation/test separation, equal budgets, hardware, versions, stopping criteria.
5. **Strong baselines:** a cheap operational baseline, a credible OR baseline, plus an expert or ablation when relevant.
6. **Independent validation:** re-evaluated constraints, integrality, objective, gaps, fallback and failure cases.
7. **Uncertainty:** repetitions, per-instance results, paired intervals or appropriate nonparametric summaries.
8. **Reproduction:** one command to regenerate machine-readable results, package lock/version info, artifact manifest.
9. **Claims ledger:** what tests demonstrate, what they do not, negative findings, distribution-shift limitations.
10. **Operational interpretation:** costs, service, risk, safety, adoption constraints; no industrial claim from CI smoke tests.

**Do not invent performance gains or present synthetic fixtures as observed factory data.** If independent evidence is missing, record it as `not yet evaluated` rather than `failed`.

## Twelve-week implementation order

- **Weeks 1–2:** repair solver CI, establish canonical project/evidence links and current-head CI status.
- **Weeks 3–5:** freeze three evidence protocols (solver learning, stochastic decisions, manufacturing); run representative baselines with full manifests.
- **Weeks 6–9:** select *one* original research question; perform held-out/OOD tests, ablations, uncertainty and failure analysis.
- **Weeks 10–12:** write a research paper draft and publish a reproducible benchmark package, raw results and limitations.

Publication or solver superiority is not guaranteed. Success is defined as **auditable research evidence**, not another repository count.
