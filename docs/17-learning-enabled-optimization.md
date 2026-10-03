# 17. Learning-Enabled and AI-Powered Optimization

[← Operations Research software ecosystem](16-or-software-ecosystem.md) · [Back to README](../README.md)

The phrase **AI-powered optimization** is often too vague to be technically useful. An optimizer does not become intelligent merely because it is implemented in Python, uses a neural network somewhere in the software stack, or is wrapped in an AI product.

A more defensible description is **learning-enabled optimization**: data, experience or interaction updates a model, policy, search strategy or algorithm configuration, and that learned component changes future optimization decisions.

This chapter separates the main mechanisms.

## 17.1 A practical test: what exactly is learning?

Ask three questions:

1. **What is updated from data or experience?**
   - a predictive model,
   - a value function or policy,
   - a surrogate objective,
   - a branching/selection rule,
   - an algorithm configuration,
   - a search distribution,
   - a representation or embedding.

2. **Does the learned object affect future optimization decisions?**

3. **Can the system adapt when new observations arrive?**

If nothing is learned or updated, the method may still be sophisticated optimization, but calling it AI-powered adds little technical meaning.

A useful high-level split is:

| Pattern | What learns? | What changes? | Typical examples |
|---|---|---|---|
| Learn the system/model | Predictive or surrogate model | Objective/constraints/response estimates | Neural surrogates, Gaussian Processes, learned dynamics |
| Learn the decision policy | Policy or value function | Actions chosen from state | Reinforcement Learning, Approximate Dynamic Programming |
| Learn how to optimize | Search/control rule | Branching, neighborhoods, proposals, solver configuration | Learning to optimize, learned heuristics, meta-learning |
| Learn from repeated instances | Representation or initialization | Warm starts and transfer across related problems | Transfer learning, instance embeddings |
| Learn online | Model/policy/statistics | Decisions adapt as data arrives | Online learning, contextual bandits, adaptive control |

## 17.2 Neural surrogate models

A surrogate approximates an expensive simulation, experiment or black-box response:

```math
\hat f_\theta(x) \approx f(x).
```

Neural networks become useful when the response is strongly nonlinear and enough training data are available.

The optimization loop is then:

```text
collect evaluations
      ↓
fit / update surrogate
      ↓
optimize surrogate or acquisition criterion
      ↓
evaluate promising candidates on the real system
      ↓
add observations and repeat
```

Industrial examples:

- injection-molding parameter optimization when physical trials are expensive,
- chemical-process optimization when detailed simulation is slow,
- structural design when finite-element evaluations dominate runtime,
- energy-system design when each scenario simulation is costly.

The neural network is not itself automatically the optimizer. It may only be the learned response model used by an outer optimization algorithm.

## 17.3 GNN-guided combinatorial optimization

Many Operations Research problems are naturally graphs: routing, assignment, scheduling, network design and facility-location variants.

A Graph Neural Network can learn node, edge or whole-instance representations and then support optimization by:

- ranking candidate decisions,
- predicting promising edges or assignments,
- generating an initial solution,
- estimating values or costs,
- guiding branching, decomposition or local search.

Examples:

- in a Vehicle Routing Problem, a GNN can score customer-to-customer connections before a routing heuristic constructs tours;
- in scheduling, a disjunctive graph can be embedded and used to rank dispatching actions;
- in network design, learned edge scores can prioritize candidate arcs before exact optimization.

The most useful framing is often **GNN-guided optimization**, not "GNN replaces optimization." Exact feasibility checks, local search, dynamic programming or MILP machinery may still provide the optimization backbone.

## 17.4 Neural combinatorial optimization and learning to construct solutions

Neural combinatorial optimization trains a model to construct or improve discrete solutions.

Common architectures include:

- pointer-style networks,
- attention models,
- Transformers,
- graph-based encoders,
- autoregressive policies.

For a routing problem, the model may output a sequence of customers. For scheduling, it may output dispatching choices or job-machine assignments.

Two common training modes are:

- **supervised learning** from high-quality or optimal solutions,
- **reinforcement learning** using the objective value as a reward signal.

Industrial examples:

- generating initial vehicle routes before local search,
- producing job sequences for dynamic scheduling,
- constructing packing assignments before repair,
- proposing candidate production plans for a downstream solver.

A neural constructor is usually best treated as a learned heuristic unless the full hybrid system retains a mathematical optimality certificate.

## 17.5 Learning-augmented exact and mathematical optimization

One of the most important modern patterns is to keep classical optimization machinery while learning components that influence computational search.

Learned components can support:

- branching-variable selection,
- node selection,
- cut selection,
- primal heuristic selection,
- neighborhood selection,
- decomposition decisions,
- warm starts,
- parameter configuration.

For example, a MILP solver can remain an exact framework while a learned model predicts promising branching choices. The learned policy may reduce runtime, while the solver's bounding and certification machinery still determines whether global optimality is proven.

This distinction is important:

> learning can improve the search strategy without replacing the mathematical optimization framework.

Industrial applications include repeated production-planning, crew-scheduling and network-design instances where many structurally similar models are solved over time.

## 17.6 Decision-focused learning and predict-then-optimize

A common industrial pipeline is:

```text
data → forecast → optimization → decision
```

If the predictive model is trained only for prediction accuracy, the most accurate forecast is not necessarily the forecast that produces the best downstream decision.

**Decision-focused learning** trains the predictive component with the downstream optimization objective in mind.

Examples:

- demand forecasting whose errors are weighted by inventory cost consequences,
- travel-time prediction optimized for routing quality rather than only mean squared error,
- energy-price prediction trained around dispatch cost,
- workforce-demand prediction evaluated by resulting staffing penalties.

This is a particularly strong example of AI-powered optimization because learning and optimization are coupled through the final decision objective.

## 17.7 Meta-learning, algorithm selection and adaptive configuration

Different optimization algorithms work well on different instance classes. Meta-learning uses historical problem instances and solver outcomes to learn this mapping.

Possible learned decisions include:

- which solver or algorithm to use,
- which formulation to prefer,
- parameter values,
- restart policies,
- neighborhood size,
- mutation or crossover settings,
- decomposition strategy.

An industrial scheduling platform, for example, can observe instance features such as:

- number of jobs,
- number of machines,
- due-date tightness,
- setup-time structure,
- utilization,
- precedence density,

and predict which algorithmic configuration is likely to perform well.

This is closely related to **algorithm selection**, **algorithm configuration** and **hyper-heuristics**. Not every automated parameter tuner is AI, but data-driven configuration across repeated instances is genuinely learning-enabled.

## 17.8 Transfer learning and warm-starting across optimization instances

Repeated industrial problems are rarely independent. Today's scheduling problem resembles yesterday's; one plant resembles another; one product-family design resembles the next.

Transfer can occur through:

- transferred neural weights,
- reusable embeddings,
- learned value functions,
- predicted active constraints,
- incumbent solutions,
- basis information,
- decomposition structures,
- reusable heuristic policies.

Examples:

- using a scheduling policy trained on one production line as an initialization for a related line,
- warm-starting a routing model from historical route patterns,
- transferring a surrogate model across related engineering designs,
- learning from solved MILP instances to initialize future instances.

Classical warm starts do not automatically count as machine learning. The learning-enabled version uses data from prior instances to infer what should be transferred or how it should be adapted.

## 17.9 Online and adaptive optimization

An optimization system becomes adaptive when it updates as observations arrive.

Relevant frameworks include:

- online optimization,
- online learning,
- contextual bandits,
- adaptive control,
- rolling-horizon optimization,
- Model Predictive Control with learned models,
- Reinforcement Learning.

Examples:

- dynamic pricing that updates demand-response estimates,
- real-time production control reacting to machine conditions,
- traffic routing that adapts to current congestion,
- inventory policies updating demand distributions,
- energy dispatch adapting to renewable-generation forecasts.

The distinction matters:

- **dynamic optimization** means decisions or states are time-coupled;
- **online optimization** means information is revealed sequentially;
- **learning-enabled optimization** means estimates, policies or strategies are updated from data or experience.

A system can belong to all three categories, but they are not synonyms.

## 17.10 Active learning and sequential experimentation

Sometimes the main optimization problem is not only "find the best setting" but also "decide what to measure next."

Active-learning and sequential-design methods choose experiments that are informative for the final decision.

Examples:

- selecting which manufacturing parameter combination to test next,
- choosing prototype designs for physical experiments,
- deciding which simulation scenarios deserve expensive evaluation,
- selecting measurements that reduce uncertainty around feasibility boundaries.

Bayesian Optimization is a central example when the goal is directly to optimize an expensive black-box objective. More general active learning may instead prioritize model uncertainty or classification boundaries.

## 17.11 Multi-agent learning and distributed decision systems

A multi-agent system contains multiple decision-making entities that interact.

Learning becomes relevant when agents adapt policies from repeated interaction.

Examples:

- machines or workcells learning decentralized dispatching rules,
- warehouse robots learning congestion-aware coordination,
- distributed energy resources learning bidding or control policies,
- supply-chain actors adapting inventory or replenishment decisions.

Important distinction:

- a method can be **multi-agent** without using machine learning;
- a distributed optimizer can coordinate mathematically without agents learning;
- **multi-agent Reinforcement Learning** is specifically learning-based.

Therefore "multi-agent" and "AI-powered" should not be treated as synonyms.

## 17.12 Neuroevolution

Neuroevolution combines evolutionary search with neural networks.

Evolution may optimize:

- neural-network weights,
- architecture,
- activation choices,
- connectivity,
- controller parameters,
- learning rules.

Representative ideas include NEAT-style topology evolution and evolutionary architecture search.

Industrial uses can include controllers for robots, process-control policies or learned heuristics where gradients are unavailable, unreliable or inconvenient.

Neuroevolution is learning-enabled, but it should still be classified on the usual optimization axes: population-based, usually stochastic, derivative-free and generally without a finite-time global-optimality certificate.

## 17.13 A practical industrial-engineering map

| Industrial problem | Learning-enabled layer | Optimization layer |
|---|---|---|
| Production scheduling | GNN/Transformer dispatch scores | CP, MILP, local search, RL |
| Vehicle routing | learned edge/route proposals | routing heuristics, LNS, MILP |
| Process parameter tuning | neural or GP surrogate | Bayesian/black-box optimization |
| Inventory control | learned demand model/value function | stochastic control, DP, RL |
| Facility/network design | learned demand/edge representations | MILP, decomposition, heuristics |
| Workforce planning | learned demand/absence model | integer programming |
| Energy dispatch | learned forecasts/dynamics | MPC, stochastic/robust optimization |
| Repeated MILPs | learned branching/warm starts | Branch and Bound / Branch and Cut |

The strongest systems are often hybrid. Learning handles prediction, representation or search guidance; optimization enforces feasibility, trade-offs, constraints and—in exact frameworks—certification.

## 17.14 What should and should not be called AI-powered optimization?

Strong cases:

- a policy improves from interaction,
- a surrogate is repeatedly updated from new evaluations,
- a learned model changes solver search decisions,
- a model transfers knowledge across optimization instances,
- an online decision rule updates as new data arrive,
- predictions are trained against downstream decision quality.

Weak or misleading cases:

- a static optimization model is merely wrapped in an AI interface,
- a neural network predicts inputs but is never retrained or coupled to the decision objective,
- a stochastic heuristic is called AI only because it uses randomness,
- an evolutionary algorithm is relabeled "learning" without any adaptation beyond its standard search dynamics,
- a solver is described as intelligent without identifying any learned component.

A precise description should say **what is learned, from what data, how often it updates, and how that learned object changes optimization decisions**.

## 17.15 Final classification rule

"AI-powered" is not a new mutually exclusive optimization family. It is an architectural property that can cut across many existing families.

A method can simultaneously be:

```text
surrogate-based
+ online
+ stochastic
+ learning-enabled
+ constrained
+ multi-objective
+ distributed
```

The useful question is therefore not:

> "Is this optimizer AI?"

but:

> "Which part of the optimization loop learns, what information does it learn from, and how does that learning change future decisions?"
