# Decision Science and Management Science coverage — 10 October 2026

## Review premise

A map/index-only inspection can correctly identify missing **top-level repo names**, but cannot establish that a technique is absent from nested `projects/`, flagship cases or root packages. This review compares the second external feedback with actual repository contents. Existence of readable code and tests is **not** evidence of empirical validity, field adoption, production security or causal impact.

**Decision intelligence is a pipeline**, not only a solver:

1. **Framing:** whose choice, which objectives, what constraints, what is observed and when, and which causal assumptions are being made?
2. **Normative evaluation:** risk attitude, uncertainty beliefs, preferences, information value, and trade-offs across incommensurate criteria.
3. **Prediction/prescription:** forecasting, optimization, simulation, experimentation and policy design.
4. **Organizational execution:** approvals, decision rights, human override paths, fallback and lifecycle monitoring.
5. **Learning:** observed outcome evaluation with an explicit design to distinguish correlation from the causal effect of a decision policy.

The portfolio was already strong on stage 3; stages 1, 2 and 4 existed but were relatively hard to discover. We have expanded them **inside existing repositories** rather than creating three empty method umbrellas.

## Verified existing coverage (not new omissions)

| Area in feedback | Existing project evidence | Important limitation |
|---|---|---|
| Classical decision analysis and risk attitude | [Management Science capacity-expansion case](https://github.com/alperebalci/management-science/tree/main/case-studies/flagships/decision-analysis-capacity-expansion) and [SDA static decision analysis](https://github.com/alperebalci/sequential-decision-analytics/blob/main/examples/static_decision_under_uncertainty.py) | EVPI and CARA based on declared synthetic priors/payoffs |
| Decision framing | [Dedicated decision-framing repository](https://github.com/alperebalci/decision-framing-and-sequential-decision-modeling) | Requirements/model traceability, not preference elicitation by itself |
| Behavioral operations | [Newsvendor biases and human overrides](https://github.com/alperebalci/inventory-optimization-and-control/tree/main/projects/behavioral-operations-and-human-decision-making) | Stylized experimental decision rules |
| DEA / efficiency | [CCR and BCC DEA](https://github.com/alperebalci/resource-allocation-optimization/tree/main/projects/data-envelopment-analysis-efficiency) | Relative frontier, not SFA, causation, or universal productivity |
| Project and portfolio management | [CPM/PERT, Monte Carlo risk and budgeted selection](https://github.com/alperebalci/classical-scheduling-optimization/tree/main/projects/project-portfolio-and-project-scheduling) | Multi-stage R&D/real options not proved |
| Discrete-choice marketing | [MNL demand estimation](https://github.com/alperebalci/pricing-and-revenue-optimization/tree/main/projects/empirical-operations-and-demand-modeling) | No CLV/conjoint/churn suite inferred |
| Causal and experimental decision | [ATE, DiD, AIPW treatment policy](https://github.com/alperebalci/pricing-and-revenue-optimization/tree/main/projects/causal-operations-and-experimentation); [contextual bandits](https://github.com/alperebalci/sequential-decision-analytics/tree/main/projects/contextual-bandits-dynamic-procurement) | Treatment identification and off-policy evaluation must be assessed per method |
| Systems thinking | [Stock-flow/bullwhip](https://github.com/alperebalci/robust-and-adaptive-supply-chain-optimization/tree/main/projects/system-dynamics-for-operations); [agent-based supply chain](https://github.com/alperebalci/robust-and-adaptive-supply-chain-optimization/tree/main/projects/agent-based-supply-chain-simulation-python) | Simulators are not empirical validation of social feedback |
| Strategic incentives | [VCG/matching](https://github.com/alperebalci/resource-allocation-optimization/tree/main/projects/market-design-mechanism-design-and-incentives), [bilevel Stackelberg pricing](https://github.com/alperebalci/resource-allocation-optimization/tree/main/projects/leader-follower-bilevel-pricing) | Narrow mathematical examples, not a full supply-contract/principal–agent lab |

## Newly strengthened foundations

### Normative decision analysis and preference models

A native [Management Science decision-science flagship](https://github.com/alperebalci/management-science/tree/main/case-studies/flagships/decision-science-preferences-and-information) provides:

- risk-neutral **Bayesian EVSI** with conditional actions and validated priors/likelihoods;
- numerically stable **CARA certainty equivalents** (utility-based risk attitude);
- **AHP** with reciprocal-judgment and consistency audits, plus geometric group aggregation;
- normalized **multi-attribute value scoring** (**MAVT**, not assumed to be general MAUT under risk);
- **TOPSIS** with explicit cost/benefit criterion directions;
- **probability-free scenario robustness and regret** screening.

The code distinguishes Pareto optimization (candidate feasible trade-offs) from MCDM (eliciting value models and ranking alternatives). Group AHP is a bounded aggregation method, not an expert-forecasting/Delphi protocol. A scenario-satisficing proportion is not a probability of future success.

### Decision rules, information structure and overrides

The [decision framing repository](https://github.com/alperebalci/decision-framing-and-sequential-decision-modeling) now documents:

- explicit `UNIQUE`/`FIRST` decision-table policies with finite coverage/overlap audits;
- structural influence graphs rejecting cycles and infeasible information timing;
- versioned recommendation and input fingerprint fields;
- constrained, reasoned human overrides with allowed actions and role gating;
- descriptive-only override rates and realized KPI summaries.

These are **not** a standards-conformant DMN engine, verified causal graphs, authenticated enterprise permissions, tamper-evident audit logs, calibrated human trust or randomized policy experiments.

## Remaining prioritized research gaps

| Priority | Specific missing capability | Recommended destination and acceptance test |
|---|---|---|
| P1 | Expert priors, forecast calibration and elicitation protocols | Add to the Management Science decision-science flagship: proper scoring rules, calibration curves, controlled forecast panels, prior sensitivity and held-out forecasts; do not conflate confidence with skill |
| P1 | Deeper MCDM and group decisions | Extend the same flagship with carefully verified ELECTRE/PROMETHEE/BWM or full MAUT, elicited marginal value functions, preference-reversal and rank-reversal sensitivity, and reproducible stakeholder weights |
| P1 | Decision-model governance, human–AI experimentation and impact | Extend the decision-framing layer and a production decision system: independent authorization/auditing, dataset/model versioning, incident/fallback tests, preregistered override experiments and out-of-sample decision value |
| P2 | Full RDM, info-gap and real-options valuation | Expand probability-free scenario screening with alternative stress ensembles, robust satisficing, adaptation pathways and financial option assumptions; compare against baseline policies without fabricated probabilities |
| P2 | FMEA/FTA, Bayesian risk-network analysis | A specialist risk/quality extension needs independently checked fault logic, conditional-probability assumptions and rare-event validation; no completed PRA system claimed |
| P2 | Process mining, Lean/Six Sigma integration and SFA | Ground management analytics in event-log conformance/variant checks, a documented process-improvement KPI and independent statistical frontier benchmarks |
| P3 | Marketing science beyond MNL | Add CLV/churn/conjoint/uplift only with leakage-safe, choice-consistent and causal outcome evaluation; do not mislabel predicted margin uplift as causal |
| P3 | Supply contracts, principal–agent and innovation/strategy | Extend market-design and capital-budgeting flagships with participation/incentive constraints, strategic contract benchmarks and ex-ante/ex-post sensitivity |

**No new sector-specific healthcare projects are in scope.** Existing healthcare snapshots elsewhere in the portfolio are not changed by this review.

## Portfolios and governance

`management-science` is an already-existing, independent management decision case collection. It is now explicitly cataloged as a **standalone primary repository**; the map and index therefore show **47 unique active repositories** rather than 46. This is not a new empty repository. The original historical metadata owner remains `jorsacademy` until a coordinated metadata migration; clickable canonical links target `alperebalci`.

## Research-quality threshold

A method is **implemented** only when there is an executable artifact, stable inputs, explicit mathematical/statistical assumptions, independent invariant/oracle tests and documented limits. A **documented gap** is not implemented. Production readiness additionally requires authenticated governance, monitoring, incident management and independent deployment evidence. A model's measured observational KPI difference cannot substitute for causal evidence of organizational benefit.
