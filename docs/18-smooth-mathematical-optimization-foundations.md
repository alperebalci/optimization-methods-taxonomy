# Smooth mathematical optimization: foundations and optimality

This companion note bridges the [method taxonomy](../README.md) and the mathematics behind continuous optimization. It is a **conceptual reference**, not a claim that every algorithm below has a verified implementation here.

## Problem statement and notation

For a decision vector \(x\in\mathbb R^n\), consider

\[
\min_{x\in C} f(x),\qquad
C=\{x:g_i(x)\le 0\ (i=1,\ldots,m),\ h_j(x)=0\ (j=1,\ldots,p)\}.
\]

Here \(f\) is the objective and \(C\) the feasible set. A local minimum need not be global, and an infimum need not be attained. Existence follows, for example, if \(f\) is continuous and \(C\) is nonempty and compact; lower semicontinuity and compact sublevel sets are another common route.

**Conventions:** \(\nabla f\) is the gradient, \(\nabla^2 f\) the Hessian, \(\|\cdot\|\) the Euclidean norm, and \(A\succeq0\) indicates a symmetric positive-semidefinite matrix.

## Mathematical prerequisites

| Topic | Why it matters |
|---|---|
| Linear algebra: quadratic forms, eigenvalues, definiteness | Curvature, conditioning and Newton steps |
| Multivariable calculus: gradient, Hessian, Taylor expansion | Stationarity and local approximations |
| Continuity, closedness, compactness, coercivity | Existence and convergence |
| Convex sets and separating hyperplanes | Global optimality and duality |
| Tangent and normal cones | Constrained first-order geometry |

For twice continuously differentiable \(f\),

\[
f(x+d)=f(x)+\nabla f(x)^Td+\tfrac12d^T\nabla^2f(x)d+o(\|d\|^2).
\]

Positive definiteness of the Hessian at **one point** does not establish global convexity.

## Convexity and optimality

A set \(C\) is convex if \(\theta x+(1-\theta)y\in C\) for all \(x,y\in C\) and \(0\le\theta\le1\). Differentiable \(f\) is convex on a convex domain if

\[
f(y)\ge f(x)+\nabla f(x)^T(y-x).
\]

For twice differentiable \(f\) on an open convex domain, \(\nabla^2 f(x)\succeq0\) everywhere characterizes convexity.

At a differentiable interior local minimum, \(\nabla f(x^*)=0\) is necessary. A positive-semidefinite Hessian is necessary at a twice-differentiable interior local minimum; a positive-definite Hessian at a stationary point is sufficient for a strict **local** minimum. Neither statement proves global optimality without additional structure.

For convex differentiable \(f\) over convex \(C\), the variational inequality

\[
\nabla f(x^*)^T(y-x^*)\ge0\quad\text{for all }y\in C
\]

is necessary and sufficient for a global minimum.

**Worked example:** minimize \(x_1^2+x_2^2\) subject to \(x_1+x_2=1\). Substitution yields \(2x_1^2-2x_1+1\). The unique minimizer is \((1/2,1/2)\) with objective value \(1/2\); convexity proves global optimality.

## Algorithm families and their boundaries

| Family | Basic idea | Important qualification |
|---|---|---|
| Gradient descent | \(d_k=-\nabla f(x_k)\) | Step-size strategy and conditioning matter |
| Newton | \(\nabla^2f(x_k)d_k=-\nabla f(x_k)\) | Indefinite or singular Hessians need safeguards |
| BFGS / L-BFGS | Approximate curvature from gradient changes | Curvature conditions and line search matter |
| Nonlinear conjugate gradient | Combine current gradient with a prior direction | Restart and line-search design affect reliability |
| Trust-region methods | Optimize a local model within \(\|d\|\le\Delta\) | Accept/reject based on model agreement |
| Projected gradient | \(x_{k+1}=P_C(x_k-\alpha_k\nabla f(x_k))\) | Projection must be computable |
| SQP | Successive quadratic subproblems | Constraint qualification and globalization matter |
| Interior-point / penalty | Barrier or penalty reformulations | Parameter strategy and conditioning matter |

A descent direction and a line search do **not** guarantee a global optimum. In numerical optimization, *global convergence* often means convergence towards stationarity under specified assumptions, not global optimality. Report scaling, tolerances and stopping criteria when benchmarking.

## Constrained optimization: KKT and duality

For \(g_i(x)\le0\) and \(h_j(x)=0\), the Lagrangian is

\[
L(x,\lambda,\nu)=f(x)+\sum_i\lambda_i g_i(x)+\sum_j\nu_jh_j(x).
\]

KKT conditions are primal feasibility, multiplier nonnegativity \(\lambda_i\ge0\), complementary slackness \(\lambda_i g_i(x)=0\), and stationarity \(\nabla_xL=0\). At a local optimum, KKT necessity requires an appropriate **constraint qualification** (such as LICQ or MFCQ). In convex problems with affine equalities and differentiable convex inequality functions, a feasible point satisfying KKT is globally optimal. Existence of multipliers and strong duality need suitable assumptions; Slater's condition is a common sufficient condition in convex programming.

The dual function \(q(\lambda,\nu)=\inf_xL(x,\lambda,\nu)\) gives a lower bound on the primal minimum when \(\lambda\ge0\) (weak duality).

## Reproducibility checklist

1. Record variable domains, units, objectives and constraint conventions.
2. Separate feasibility, stationarity, local minima and certified global optima.
3. Identify convexity and constraint qualifications instead of assuming them.
4. Validate feasibility residuals, KKT residuals and primal-dual gap where available.
5. Record solver status, initialization, scaling, tolerances and stopping rules.
6. Distinguish empirical runtime/quality from mathematical guarantees.

## References

- Kunal Kumar, [*A Primer to Mathematical Optimization*](https://kthinks.vercel.app/posts/a-primer-to-mathematical-optimization/index.html) (inspiration for this original, independently written companion).
- Nocedal and Wright, *Numerical Optimization*, 2nd ed.
- Boyd and Vandenberghe, *Convex Optimization*.

This note does not reproduce the linked lecture text or imply tested code coverage.
