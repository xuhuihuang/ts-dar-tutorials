import numpy as np
from matplotlib import pyplot as plt

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(6, 4))

# Customize axis borders (thicker for better visibility)
for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(2)

# Set aspect ratio to 1 (square plot)
ax.set_aspect(1)

# Initialize the ContourPlot2D class and plot free energy landscape
c = ContourPlot2D(shade=True, n_levels=20, vmax=12)
ax, X, Y, Z = c.plot(data=np.concatenate(dihedral), ax=ax, cbar=True)

# Set axis limits to cover the full range of torsion angles (-π to π)
ax.set_xlim(-np.pi, np.pi)
ax.set_ylim(-np.pi, np.pi)

# Convert tick labels from radians to degrees for better readability
ax.set_xticks([-np.pi, 0, np.pi], labels=[-180, 0, 180])
ax.set_yticks([-np.pi, 0, np.pi], labels=[-180, 0, 180])

# Set a background color
r, g, b = 0.1, 0.1, 0.2  # Dark blue shade
ax.patch.set_facecolor((r, g, b, 0.15))  # Semi-transparent background

# Customize tick labels: increase font size and adjust tick properties
ax.tick_params(axis="both", labelsize=17.5, direction='out', length=7.5, width=2.5)

# Set axis labels with phi (ϕ) and psi (ψ) symbols
ax.set_xlabel(r'$\phi$', fontsize=20)
ax.set_ylabel(r'$\psi$', fontsize=20)

cbar_ax = fig.axes[-1]
cbar_ax.set_ylabel('Free Energy / kT', fontsize=17.5)
cbar_ax.set_yticks([0, 2, 4, 6, 8, 10, 12])  # Adjust the list to your desired ticks

plt.tight_layout()
plt.savefig("./free_energy_2d.png", dpi=300)
