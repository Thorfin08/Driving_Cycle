import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
D = 1  # Pipe diameter (normalized)
R = D / 2
x_vals = np.linspace(0.01, 5, 100)  # positions along the pipe
r = np.linspace(0, R, 200)  # radial positions
R_grid, X_grid = np.meshgrid(r, x_vals)
V_profile = np.zeros_like(R_grid)

# Generate simplified velocity profile
for i, x in enumerate(x_vals):
    delta = min(R, x / 5)  # Boundary layer thickness (simplified)
    for j, rad in enumerate(r):
        if rad < R - delta:
            V_profile[i, j] = 1  # Core flow
        else:
            V_profile[i, j] = (R - rad) / delta  # Linear profile in BL

# Create the figure and axis
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, 1.1)
ax.set_ylim(0, R)
ax.set_xlabel("Velocity")
ax.set_ylabel("Radius")
ax.set_title("Velocity Profile in Pipe Entrance Region")

# Initialization function
def init():
    line.set_data([], [])
    return line,

# Animation function
def animate(i):
    line.set_data(V_profile[i], r)
    ax.set_title(f"Velocity Profile at x = {x_vals[i]:.2f} D")
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=len(x_vals), interval=80, blit=True)

plt.show()
