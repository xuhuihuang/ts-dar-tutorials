import numpy as np
import matplotlib.pyplot as plt

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(6, 4))

# Customize axis
for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(2)

# Ensure equal aspect ratio (important for angles)
ax.set_aspect('equal')

# Concatenate dihedral angles and OOD scores for easier handling
all_dihedral = np.concatenate(dihedral)
all_ood = np.concatenate(ood_scores)

# Main scatter plot (background) – small points colored by OOD scores
cb = ax.scatter(all_dihedral[:, 0], all_dihedral[:, 1],
                c=all_ood, cmap='coolwarm', s=5, alpha=1)

# Set colorbar range (thres is the OOD score cutoff)
cb.set_clim(0.0, thres)

# Add a colorbar with formatted ticks
ccc = fig.colorbar(cb)
ccc.ax.tick_params(labelsize=15, length=5, width=1.5)
ccc.set_label('OOD score',fontsize=18)

# Set axis limits (full range of dihedral angles)
ax.set_xlim(-np.pi, np.pi)
ax.set_ylim(-np.pi, np.pi)

# Set axis labels with phi (ϕ) and psi (ψ) symbols
ax.set_xlabel(r'$\phi$', fontsize=20)
ax.set_ylabel(r'$\psi$', fontsize=20)

# Convert tick labels from radians to degrees
ax.set_xticks([-np.pi, 0, np.pi])
ax.set_xticklabels([-180, 0, 180])
ax.set_yticks([-np.pi, 0, np.pi])
ax.set_yticklabels([-180, 0, 180])

# Add contour lines for free energy landscape
cs = ax.contour(X, Y, Z,
                colors='black',
                linewidths=1,
                levels=np.linspace(0, 12, 20),
                alpha=0.6,
                zorder=1, vmin=0, vmax=12)

# Customize tick labels and styling
ax.tick_params(axis="both", labelsize=17.5, direction='out', length=7.5, width=2.5)

# Set a background color for the axis
r, g, b = 0.1, 0.1, 0.2
ax.patch.set_facecolor((r, g, b, 0.15))

# Highlight certain points in bright red:
# Example condition: OOD scores above 0.5 * thres. You can try different values.
highlight_mask = all_ood >= 0.5 * thres

ax.scatter(all_dihedral[highlight_mask, 0],
           all_dihedral[highlight_mask, 1],
           s=10,                # Increase the size for emphasis
           facecolors='red', # Fill color
           edgecolors='red',  # Outline color
           linewidth=1.5,       # Outline thickness
           alpha=0.8,
           zorder=5)           # Ensure these circles appear on top

#plt.show()
# Save the plot
plt.savefig("2state_free_energy_landscape.png", dpi=300)

fig,ax = plt.subplots(1,1,figsize=(6,4))
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2)
ax.set_aspect('equal')

cb=ax.scatter(np.concatenate(features)[:,0],np.concatenate(features)[:,1],c=np.concatenate(ood_scores),cmap='coolwarm',s=1,alpha=1)
cb.set_clim(0.0,thres)

ccc = fig.colorbar(cb)
ccc.ax.tick_params(labelsize=15,length=5,width=1.5)
ccc.set_label('OOD score',fontsize=18)

ax.plot([0,state_centers[0,0]],[0,state_centers[0,1]],linewidth=2,color='black',linestyle='--')
ax.plot([0,state_centers[1,0]],[0,state_centers[1,1]],linewidth=2,color='black',linestyle='--')

ax.set_xlim(-1.1,1.1)
ax.set_ylim(-1.1,1.1)

ax.set_xticks([-1,0,1])
ax.set_yticks([-1,0,1])

# Set axis labels with phi (ϕ) and psi (ψ) symbols
ax.set_xlabel(r'$z_1$', fontsize=20)
ax.set_ylabel(r'$z_2$', fontsize=20)

ax.tick_params(axis="both",labelsize=17.5,direction='out',length=7.5,width=2.5)

r=0.1
g=0.1
b=0.2
ax.patch.set_facecolor((r,g,b,.15))

# Save the plot
plt.savefig("2state_hyperspherical_embeddings.png", dpi=300)
