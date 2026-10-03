# Operations Research Software Ecosystem

This guide separates **modeling languages and modeling layers** from **solvers**, **specialized optimization engines**, and **domain-specific frameworks**. These categories are frequently mixed together even though they play different roles in an optimization stack.

## The most important distinction: modeler vs. solver

An optimization application usually has at least two layers:

1. **Modeling layer** — variables, constraints, objectives, data, scenarios, and mathematical structure are expressed here.
2. **Solver layer** — algorithms such as simplex, barrier/interior-point, branch-and-bound, branch-and-cut, spatial branch-and-bound, propagation, local search, or hybrid methods actually search for a solution.

A modeling system may connect to many solvers. A solver may be callable from many modeling systems.

### AMPL: modeling language or solver?

**AMPL is primarily an algebraic modeling language and optimization platform, not a solver.** It lets you formulate a mathematical optimization model and pass the generated problem to solvers such as Gurobi, CPLEX, HiGHS, SCIP, MOSEK, or others supported by the AMPL ecosystem.

**GAMS is conceptually similar.** GAMS is a general algebraic modeling system: it represents the model, handles data and execution workflow, and dispatches the mathematical program to an attached solver.

A compact mental model is therefore:

```text
AMPL / GAMS / Pyomo / JuMP / CVXPY
                ↓
        mathematical model
                ↓
Gurobi / CPLEX / Xpress / HiGHS / SCIP / MOSEK / BARON / ...
                ↓
             solution
```

AMPL and GAMS are closer to each other than either is to Gurobi.

## Modeling languages and algebraic modeling systems

| Tool | Type | Main role | Typical fit |
|---|---|---|---|
| **AMPL** | Algebraic modeling language + platform | Solver-independent mathematical modeling, data/model separation, deployment APIs | LP, MILP, NLP, conic and other models through connected solvers |
| **GAMS** | Algebraic modeling system | Mathematical modeling, data handling, solver orchestration | Large optimization models, energy, economics, supply chain, planning |
| **Pyomo** | Python modeling framework | Algebraic optimization modeling in Python | Research, teaching, production prototypes, solver portability |
| **JuMP** | Julia modeling language/DSL | High-performance mathematical optimization modeling | Research, decomposition, large-scale and advanced optimization |
| **CVXPY** | Python convex modeling DSL | Disciplined convex / quasiconvex modeling | Convex optimization, portfolio models, ML/OR interfaces |
| **MiniZinc** | Solver-independent constraint modeling language | Constraint satisfaction and discrete optimization modeling | CP, scheduling, combinatorial optimization |
| **AIMMS** | Commercial modeling and application-development environment | Optimization modeling plus deployment/UI workflow | Enterprise decision-support applications |
| **FICO Xpress Mosel** | Optimization modeling/programming language | Model construction and orchestration, often with Xpress Optimizer | Enterprise mathematical programming |

## General-purpose mathematical programming solvers

| Tool | Type | Strong problem classes / role |
|---|---|---|
| **Gurobi Optimizer** | Commercial solver | LP, QP/QCP, MILP/MIQP/MIQCP; general-purpose exact mathematical programming |
| **IBM CPLEX Optimizer** | Commercial solver | LP/QP/MIP family; mature enterprise mathematical programming |
| **FICO Xpress Optimizer** | Commercial solver | LP/QP/MIP family and enterprise optimization |
| **SCIP** | Open-source solver + research framework | MIP, MINLP, constraint integer programming, branch-cut-and-price research |
| **HiGHS** | Open-source solver | LP, MIP, QP; strong default open-source numerical backend |
| **CBC** | Open-source MILP solver | Classical MILP solving in the COIN-OR ecosystem |
| **GLPK** | Open-source LP/MIP toolkit | Small-to-medium LP/MIP, education, reproducible baseline models |

## Conic and convex optimization

| Tool | Type | Main role |
|---|---|---|
| **MOSEK** | Commercial conic optimization solver | LP/QP, SOCP, exponential/power cones, SDP, mixed-integer convex optimization |
| **SCS** | Open-source first-order conic solver | Large sparse conic problems where moderate accuracy can be acceptable |
| **Clarabel** | Open-source interior-point conic solver | Convex conic optimization with modern sparse numerical methods |
| **ECOS** | Open-source conic solver | SOCP and related convex models; historically common through CVXPY |
| **CVXOPT** | Python convex optimization library | Convex optimization primitives and numerical algorithms |
| **CVXPY** | Modeling layer, not primarily a solver | Converts disciplined convex models to compatible numerical solvers |

A useful distinction is that **CVXPY describes the convex problem** while **MOSEK, SCS, Clarabel, ECOS, and similar backends solve the resulting numerical problem**.

## Global nonlinear and MINLP optimization

| Tool | Type | Main role |
|---|---|---|
| **BARON** | Commercial global optimization solver | Deterministic global optimization for nonconvex NLP/MINLP |
| **Couenne** | Open-source global MINLP solver | Spatial branch-and-bound for nonconvex MINLP |
| **SCIP** | Solver/framework | Also supports MINLP and global-search-style machinery for suitable formulations |
| **Ipopt** | Open-source local NLP solver | Large-scale smooth nonlinear programming; local, not a general global optimizer |
| **BONMIN** | Open-source MINLP solver | Convex MINLP-oriented algorithms in the COIN-OR ecosystem |

The word **global** matters here. Ipopt may be an excellent NLP solver but does not in general certify the global optimum of a nonconvex problem. BARON and Couenne are designed for deterministic global optimization.

## Constraint programming, scheduling, routing, and combinatorial optimization

| Tool | Type | Main role |
|---|---|---|
| **OR-Tools** | Optimization toolkit | CP-SAT, vehicle routing, graph/network algorithms, LP/MIP interfaces |
| **IBM CP Optimizer** | Commercial constraint-programming solver | Scheduling, sequencing, cumulative resources, logical constraints |
| **Hexaly Optimizer** | Commercial modeling + optimization engine | Combinatorial, nonlinear, set/list-based and hybrid optimization |
| **MiniZinc** | Constraint modeling language | Solver-independent CP/combinatorial models |
| **Timefold Solver** | Open-source planning solver | Employee scheduling, vehicle routing, timetabling and operational planning |
| **Choco Solver** | Java constraint-programming solver | CP research, teaching and Java applications |
| **VROOM** | Specialized routing engine | High-performance vehicle-routing optimization services |

**OptaPlanner** is important historically, but for new projects the actively developed continuation is **Timefold Solver**, which originated as a fork led by the original OptaPlanner team.

## Optimization under uncertainty

| Tool | Type | Main role |
|---|---|---|
| **RSOME** | Python modeling framework | Robust and distributionally robust optimization; reformulates models for external solvers |
| **SDDP.jl** | Julia package | Multistage stochastic optimization with stochastic dual dynamic programming |
| **mpi-sppy** | Python/Pyomo package | Scenario-based stochastic programming and decomposition |
| **GAMS EMP** | GAMS framework | Extended mathematical programming, equilibrium and uncertainty-related formulations |
| **AMPL + scenario formulations** | Modeling pattern | Two-stage and scenario-based stochastic/robust models using an external solver |

## Multi-objective and metaheuristic tooling

| Tool | Type | Main role |
|---|---|---|
| **pymoo** | Python library | Multi-objective evolutionary optimization, Pareto-front analysis |
| **DEAP** | Python evolutionary computation framework | Genetic algorithms, evolutionary programming, custom metaheuristics |
| **Nevergrad** | Python derivative-free optimization library | Black-box and derivative-free search |
| **Optuna** | Hyperparameter / black-box optimization framework | Experimental design and parameter search rather than classical algebraic OR |

These tools belong to a different part of the optimization ecosystem than exact MILP/conic solvers. They are useful when the model is black-box, derivative-free, simulation-based, many-objective, or difficult to represent algebraically.

## How the major names relate

```text
MODEL / DSL / ORCHESTRATION
AMPL ─┐
GAMS ─┤
Pyomo ┤
JuMP ─┤
CVXPY ┤──────────────┐
RSOME ┤              │
MiniZinc             │
                     ▼
              SOLVER / ENGINE
        Gurobi | CPLEX | Xpress
        HiGHS | SCIP | CBC
        MOSEK | SCS | Clarabel
        BARON | Couenne | Ipopt
                     │
                     ▼
                 solution

SPECIALIZED / HIGHER-LEVEL ENGINES
OR-Tools | Hexaly | CP Optimizer | Timefold | VROOM

STOCHASTIC / DECOMPOSITION
SDDP.jl | mpi-sppy | custom Benders / column generation / Lagrangian methods
```

## Practical stack selection

For a Python-first OR portfolio:

- **Pyomo + HiGHS** gives a fully open-source baseline for LP/MILP.
- **Pyomo or gurobipy + Gurobi** is a strong general-purpose MILP stack.
- **OR-Tools CP-SAT** is especially useful for discrete scheduling and assignment models.
- **CVXPY + MOSEK** is a strong convex/conic stack.
- **RSOME + MOSEK/Gurobi** is useful for robust and distributionally robust optimization.
- **MiniZinc** is valuable when solver-independent constraint programming is the main abstraction.
- **Hexaly** is worth evaluating for difficult combinatorial models where set/list decisions or hybrid search are natural.
- **JuMP + SDDP.jl** is a strong research stack for multistage stochastic optimization.
- **BARON** belongs in the toolbox when deterministic global optimization of nonconvex NLP/MINLP is required.

For a solver-research portfolio:

- **SCIP + PySCIPOpt** exposes branch-and-bound, cutting, pricing, and custom plugin logic.
- **HiGHS** provides a transparent open-source LP/MIP/QP baseline.
- **Gurobi/CPLEX/Xpress** provide industrial reference implementations for mainstream mathematical programming.

## Portfolio coverage note

Before this guide was added, the portfolio already contained substantial use of **Gurobi, CPLEX, OR-Tools, Pyomo, CVXPY, GAMS, SCIP, and HiGHS**, plus targeted references to **JuMP** and **SDDP.jl**.

This guide adds explicit conceptual coverage for tools that were absent or not represented as first-class OR technologies in the research repositories, including:

- AMPL
- MOSEK
- FICO Xpress
- Hexaly as an optimization technology
- RSOME
- MiniZinc
- BARON
- Couenne
- Timefold Solver / OptaPlanner lineage
- Choco Solver
- VROOM
- SCS, Clarabel, ECOS, CVXOPT
- AIMMS
- CBC and GLPK

The presence of a tool in this taxonomy does **not** imply that a full executable example already exists for it. Conceptual coverage and implemented project coverage are tracked separately.

## Official references

- AMPL: https://ampl.com/
- GAMS: https://www.gams.com/
- Gurobi: https://www.gurobi.com/
- IBM CPLEX / CP Optimizer: https://www.ibm.com/products/ilog-cplex-optimization-studio
- FICO Xpress: https://www.fico.com/en/products/fico-xpress-optimization
- MOSEK: https://www.mosek.com/
- SCIP: https://scipopt.org/
- HiGHS: https://highs.dev/
- OR-Tools: https://developers.google.com/optimization
- Hexaly: https://www.hexaly.com/
- MiniZinc: https://www.minizinc.org/
- Timefold Solver: https://timefold.ai/
- RSOME: https://www.rsomerso.com/
- SDDP.jl: https://sddp.dev/
- BARON: https://www.minlp.com/baron-solver
- Couenne: https://github.com/coin-or/Couenne
