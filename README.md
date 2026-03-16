# Droplet Spreading on a Rotating Disk

This project studies the spreading of a viscous droplet on a rotating disk using a thin-film lubrication model derived from the Navier–Stokes equations.  
The objective is to simulate the time evolution of the droplet height profile and investigate the stability and physical consistency of the numerical scheme.

---

## Physics Model

The governing equation is the axisymmetric thin-film equation:

∂u/∂t + (1/r) ∂/∂r ( r M(u) ∂P/∂r ) = 0

where

P = ((r u_r)_r) / r  
M(u) = u² (u + 3λ)

This model captures several important physical effects:

- capillary driven spreading
- slip boundary effects
- centrifugal forces due to disk rotation

Thin-film equations of this type commonly arise in **lubrication theory and fluid mechanics**.

---

## Numerical Method

The equation is solved numerically using:

- Finite Element Method (FEM)
- Weak variational formulation
- Implicit time integration
- Non-negativity preserving mobility scheme

The numerical scheme follows the **entropy-stable framework of Grün & Rumpf**, ensuring:

- numerical stability  
- physically consistent solutions  
- preservation of non-negative film thickness

---

## Simulation Results

### Droplet spreading simulation

![Droplet spreading](droplet_spreading.mp4)

This animation shows the evolution of the droplet height profile as it spreads radially over the disk.

---

### Droplet spreading with slip and centrifugal force

![Droplet spreading with slip](droplet_spreading_with_slip.mp4)

This simulation includes additional physical effects such as slip boundary conditions and centrifugal forces, which modify the spreading behavior of the droplet.

---

## Repository Contents

```
thinfilm_simulation.py        → Python implementation of the thin-film solver
droplet_spreading.mp4         → animation of droplet spreading
droplet_spreading_with_slip.mp4 → animation including slip and centrifugal effects
Final_Report.pdf              → full derivation and numerical analysis
```

---

## Author

Atharva Sinnarkar  
M.Sc Computational Engineering  
FAU Erlangen–Nürnberg
