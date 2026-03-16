import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# -------------------------------------------------
# Parameters and setup
# -------------------------------------------------
r_min, r_max = 0.0, 1.0
N = 100
lambda_val = 4
T = 1
dt = 1e-2
steps = int(T / dt)

sigma = 1e-1

r = np.linspace(r_min, r_max, N + 1)
dr = r[1] - r[0]

# -------------------------------------------------
# Initial condition (triangle droplet)
# -------------------------------------------------
u = np.zeros_like(r)

mask1 = (r >= 0.2) & (r <= 0.4)
mask2 = (r > 0.4) & (r <= 0.6)

u[mask1] = (r[mask1] - 0.2) / (0.4 - 0.2)
u[mask2] = (0.6 - r[mask2]) / (0.6 - 0.4)

# -------------------------------------------------
# Shifted mobility
# -------------------------------------------------
def shifted_mobility(u_val, sigma):
    u_clip = np.maximum(u_val, sigma)
    return u_clip**2 * (u_clip + 3 * lambda_val)

# -------------------------------------------------
# Discrete mobility
# -------------------------------------------------
def discrete_mobility(U1, U2, sigma):

    if np.abs(U2 - U1) < 1e-15:
        return shifted_mobility(U1, sigma)

    s_vals = np.linspace(U1, U2, 50)
    m_vals = shifted_mobility(s_vals, sigma)
    m_vals = np.maximum(m_vals, 1e-12)

    inv_m = 1.0 / m_vals
    integral_inv_m = np.trapz(inv_m, s_vals)

    if integral_inv_m == 0:
        return 1e-12

    return (U2 - U1) / integral_inv_m

# -------------------------------------------------
# Lumped mass matrix
# -------------------------------------------------
def build_lumped_mass_matrix(r, dr, N):

    M_diag = np.zeros(N+1)

    for i in range(1, N):
        M_diag[i] = r[i] * dr / 3.0

    M_diag[0] = r[0] * dr / 6.0
    M_diag[-1] = r[-1] * dr / 6.0

    return np.diag(M_diag)

# -------------------------------------------------
# Stiffness matrix
# -------------------------------------------------
def assemble_stiffness_matrix(u, r, dr, sigma, N):

    K = np.zeros((N+1, N+1))

    for i in range(N):

        re = (r[i] + r[i+1]) / 2.0

        m_discrete = discrete_mobility(u[i], u[i+1], sigma)

        coef = m_discrete * re / dr

        K[i, i] += coef
        K[i, i+1] -= coef
        K[i+1, i] -= coef
        K[i+1, i+1] += coef

    return K

# -------------------------------------------------
# Build mass matrix
# -------------------------------------------------
M_matrix = build_lumped_mass_matrix(r, dr, N)

# -------------------------------------------------
# Time stepping
# -------------------------------------------------
u_old = u.copy()

u_profiles = [u.copy()]
t_vals = [0.0]

print("Running simulation...")

for step in range(1, steps + 1):

    time = step * dt

    K = assemble_stiffness_matrix(u_old, r, dr, sigma, N)

    A = M_matrix + dt * K
    b = M_matrix @ u_old

    u_new = np.linalg.solve(A, b)

    # Boundary conditions
    u_new[0] = 3*u_new[1] - 3*u_new[2] + u_new[3]
    u_new[-1] = 3*u_new[-2] - 3*u_new[-3] + u_new[-4]

    u_profiles.append(u_new.copy())
    t_vals.append(time)

    u_old = u_new.copy()

print("Simulation finished.")

# -------------------------------------------------
# Animation
# -------------------------------------------------
fig, ax = plt.subplots()

line, = ax.plot([], [], lw=2)

ax.set_xlim(r_min, r_max)
ax.set_ylim(-0.2, 1.2)

ax.set_xlabel("r")
ax.set_ylabel("u(r)")
ax.set_title("Droplet spreading on rotating disk")

def init():
    line.set_data([], [])
    return line,

def animate(i):

    line.set_data(r, u_profiles[i])
    return line,

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=len(u_profiles),
    init_func=init,
    blit=True,
    interval=200
)

plt.show()

# -------------------------------------------------
# Save animation
# -------------------------------------------------
ani.save("droplet_spreading.mp4", writer="ffmpeg", fps=10)

print("Animation saved as droplet_spreading.mp4")