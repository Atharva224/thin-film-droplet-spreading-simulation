# Droplet Spreading on a Rotating Disk

This project studies the spreading of a viscous droplet on a rotating disk using a thin-film lubrication model derived from the Navier–Stokes equations. The goal is to simulate the evolution of the droplet height profile and investigate the stability and physical consistency of the numerical scheme.

---

## Physics Model

The governing equation is the axisymmetric thin film equation:

∂u/∂t + (1/r) ∂/∂r ( r M(u) ∂P/∂r ) = 0

where

P = ( (r u_r)_r ) / r  
M(u) = u² (u + 3λ)

This equation captures important physical effects such as:

- capillary driven spreading
- slip effects
- centrifugal forces due to disk rotation

The model is commonly used in lubrication theory and thin-film fluid mechanics.

---

## Numerical Method

The equation is solved numerically using:

- Finite Element Method (FEM)
- Weak variational formulation
- Implicit time integration
- Non-negativity preserving mobility scheme

The numerical approach follows the entropy-stable framework proposed by **Grün & Rumpf**, which ensures physically consistent solutions and avoids negative film thickness.

---

## Simulation Result

The simulation produces the time evolution of the droplet height profile as the fluid spreads radially over the rotating disk.

The repository includes an animation showing the spreading process.

---

## Repository Contents

thinfilm_simulation.py  
Python implementation of the thin-film numerical solver.

droplet_spreading.mp4  
Animation showing the droplet spreading over time.

Final_Report.pdf  
Detailed derivation of the governing equations, numerical formulation, and simulation results.

---

## Author

Atharva Sinnarkar  
M.Sc Computational Engineering  
FAU Erlangen–Nürnberg
