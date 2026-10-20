# Smooth mathematical optimization: foundations and optimality

This companion note bridges the [method taxonomy](../README.md) and the mathematical prerequisites behind continuous optimization. It is a **conceptual reference**, not a claim that every algorithm below has a verified implementation in this repository.

## Scope and notation

For a decision vector \(x\in\mathbb R^n\), consider

\[
\min_{x\in C} f(x),\qquad
C=\{x:g_i(x)\le 0\ (i=1,\ldots,m),\ h_j(x)=0\ (j=1,\ldots,p)\}.
\]

Here \(f\) is the objective, \(C\) the feasible set, and feasible points satisfy **all** constraints. A local minimum need not be global; an infimum need not be attained. An optimizer exists, for example, if \(f\) is continuous and \(C\) is nonempty and compact. More generally, lower semicontinuity plus suitable level-set compactness (often via coercivity) can ensure existence.

**Conventions:** \(\nabla f\) is the gradient, \(\nabla^2 f\) the Hessian, \(\|\cdot\|\) the Euclidean norm, and \(A\succeq0\) denotes a symmetric positive-semidefinite matrix.

## Prerequisite roadmap

| Topic | Why it matters |
|---|---|
| Linear algebra: eigenvalues, quadratic forms, positive definiteness | Curvature, conditioning, Newton steps |
| Multivariate calculus: directional derivatives, gradients, Hessians, Taylor expansion | Stationarity and local models |
| Norms, closedness, compactness, continuity | Existence and convergence arguments |
| Convex sets, separating hyperplanes, convex functions | Global optimality and duality |
| Tangent and normal cones | Constrained first-order geometry |

For a twice differentiable function, Taylor's expansion near \(x\) gives
\[
f(x+d)=f(x)+\nabla f(x)^Td+\tfrac12d^T\nabla^2f(x)d+o(\|d\|^2).
\]
Positive definite Hessians imply strictly positive local quadratic curvature; they are **not** a general test for global convexity at only one point.

## Convexity and optimality

A set \(C\) is convex if \(\theta x+(1-\theta)y\in C\) for all \(x,y\in C\), \(0\le\theta\le1\). A differentiable \(f\) is convex on a convex domain if
\[
f(y)\ge f(x)+\nabla f(x)^T(y-x).
\]
If \(f\) is twice differentiable on an open convex domain, a positive-semidefinite Hessian everywhere characterizes convexity.

At an unconstrained differentiable **interior** local optimum, \(\nabla f(x^*)=0\) is necessary. A positive-semidefinite Hessian is a necessary second-order condition when the Hessian exists; a positive-definite Hessian at a stationary point is sufficient for a strict local minimum. None of these conditions alone proves global optimality for a nonconvex function.

For differentiable convex \(f\) on convex \(C\), the variational inequality
\[
\nabla f(x^*)^T(y-x^*)\ge0\quad\text{for all }y\in C
\]
is both necessary and sufficient for global optimality.

**Worked example.** Minimize \(x_1^2+x_2^2\) subject to \(x_1+x_2=1\). Substitution produces \(2x_1^2-2x_1+1\); the unique minimizer is \((1/2,1/2)\) with objective \(1/2\). The positive-definite quadratic objective and affine feasible set establish global optimality.

## Algorithms: distinct guarantees and assumptions

| Family | Typical direction/update | Main caveat |
|---|---|---|
| Steepest/gradient descent | \(d_k=-\nabla f(x_k)\) | Step-size rules and conditioning govern progress |
| Newton | Solve \(\nabla^2f(x_k)d_k=-\nabla f(x_k)\) | Indefinite/singular Hessians require safeguards |
| Quasi-Newton (BFGS/L-BFGS) | Update curvature approximations | Curvature safeguards and line search matter |
| Nonlinear conjugate gradient | Combine current negative gradient with prior direction | Restart and line-search choices affect behavior |
| Trust region | Minimize a local model within \(\|d\|\le\Delta\) | Acceptance ratio controls trust-region radius |
| Projected gradient | \(x_{k+1}=P_C(x_k-\alpha_k\nabla f(x_k))\) | Projection must be well defined/computable |
| SQP | Solve sequential quadratic local subproblems | Constraint regularity and globalization matter |
| Interior point / penalty | Handle constraints through barriers or penalties | Barrier/penalty parameter strategy is essential |

A descent direction and a line search alone do **not** imply convergence to a global minimizer. Global convergence in numerical optimization commonly means convergence (or subsequential convergence) to a **stationary point** from a broad set of starting points, under stated assumptions. Scaling, stopping tolerances and numerical conditioning must be reported with experiments.

## Constrained optimality and duality

With inequalities \(g_i(x)\le0\) and equalities \(h_j(x)=0\), define
\[
L(x,\lambda,\nu)=f(x)+\sum_i\lambda_i g_i(x)+\sum_j\nu_j h_j(x).
\]
The Karush–Kuhn–Tucker conditions are primal feasibility, dual feasibility \(\lambda_i\ge0\), complementary slackness \(\lambda_i g_i(x)=0\), and stationarity \(\nabla_xL=0\). At a local optimum they are necessary only under an appropriate **constraint qualification** (for example LICQ or MFCQ). For convex differentiable problems with affine equality constraints, KKT conditions are sufficient when they hold; strong duality and existence of multipliers require additional assumptions such as Slater's condition in common settings.

The dual function \(q(\lambda,\nu)=\inf_x L(x,\lambda,\nu)\) supplies a lower bound on the primal minimum for \(\lambda\ge0\) (weak duality). A primal-dual gap is informative only when the corresponding primal and dual candidates are feasible and the numerical conventions are documented.

## Practical verification checklist

1. State variable domains, units, objective direction and every constraint.
2. Distinguish feasibility, stationarity, local optimality and global certificates.
3. Identify convexity and any constraint qualification actually used.
4. Report primal residuals, projected-gradient/KKT residuals and duality gap when applicable.
5. State solver status, initialization, scaling, stopping rule and tolerances.
6. For numerical comparisons, separate solution quality from runtime and verify against suitable baselines.

## Further reading and attribution

- Kunal Kumar, [*A Primer to Mathematical Optimization*](https://kthinks.vercel.app/posts/a-primer-to-mathematical-optimization/index.html) (lecture-based conceptual overview; inspiration for this independent summary).
- Jorge Nocedal and Stephen J. Wright, *Numerical Optimization* (2nd ed.).
- Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*.

This note deliberately does not duplicate the linked author's lecture text and does not claim tested code coverage.
