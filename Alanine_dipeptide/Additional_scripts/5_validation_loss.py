import numpy as np
import matplotlib.pyplot as plt

# Create a figure with a specific size
fig = plt.figure(figsize=(6, 4))

# Define custom colors for the line and markers
line_color = 'royalblue'
marker_face = 'white'
marker_edge = 'royalblue'

# Plot with custom colors, line width, and markers
plt.plot(tsdar.validation_vamp, color=line_color, linewidth=2, marker='o',
         markersize=6, markerfacecolor=marker_face, markeredgecolor=marker_edge)

# Set the axis labels
plt.xlabel('Training Epochs', fontsize=20)
plt.ylabel('VAMP-2 Loss', fontsize=20)
plt.ylim(0, 2.25)
plt.yticks(np.arange(0, 2.1, 0.5))
plt.xticks(np.arange(0, 25, 5))

# Customize tick parameters for readability
plt.xticks(fontsize=17.5)
plt.yticks(fontsize=17.5)
plt.gca().set_box_aspect(0.85)

# Add a dashed grid to improve the readability of the plot
plt.grid(alpha=0.3, linestyle='--')

# Adjust the layout to ensure everything fits well
plt.tight_layout()

# Display the plot
#plt.show()

# Save the plot
plt.savefig("validation_vamp.png", dpi=300)
