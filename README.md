# Droplet Spreading on a Rotating Disk

This project studies the spreading of a viscous droplet on a rotating disk using a thin-film lubrication model derived from the Navier–Stokes equations. The goal is to simulate the time evolution of the droplet height profile and analyze the stability of the numerical scheme.

The model captures the physics of thin liquid films and is commonly used in lubrication theory and fluid mechanics.

---

# Physics Model

The governing equation is the axisymmetric thin-film equation

∂u/∂t + (1/r) ∂/∂r ( r M(u) ∂P/∂r ) = 0

where

P = ((r u_r)_r) / r  
M(u) = u² (u + 3λ)

This model captures important physical effects such as

• capillary driven spreading  
• slip boundary conditions  
• centrifugal forces due to disk rotation  

Thin-film equations of this type arise in many engineering problems including coating flows, lubrication, and droplet spreading.

---

# Numerical Method

The equation is solved using

• Finite Element Method (FEM)  
• Weak variational formulation  
• Implicit time integration  
• Non-negativity preserving mobility scheme  

The numerical scheme follows the entropy-stable framework proposed by **Grün & Rumpf**, ensuring

• numerical stability  
• physically consistent solutions  
• preservation of non-negative film thickness  

---

# Simulation Results

## Droplet spreading simulation

<video src="droplet_spreading.mp4" controls width="650"></video>

This animation shows the evolution of the droplet height profile as the fluid spreads radially across the disk.

---

## Droplet spreading with slip and centrifugal force

<video src="droplet_spreading_with_slip.mp4" controls width="650"></video>

This simulation includes additional physical effects such as slip boundary conditions and centrifugal forces, which modify the spreading behavior of the droplet.

---

# Repository Contents

thinfilm_simulation.py  
Python implementation of the thin-film numerical solver.

droplet_spreading.mp4  
Animation showing the droplet spreading over time.

droplet_spreading_with_slip.mp4  
Simulation including slip boundary conditions and centrifugal effects.

Final_Report.pdf  
Detailed derivation of the governing equations, numerical formulation, and simulation results.

---

# Author

Atharva Sinnarkar  
M.Sc Computational Engineering  
FAU Erlangen–Nürnberg
