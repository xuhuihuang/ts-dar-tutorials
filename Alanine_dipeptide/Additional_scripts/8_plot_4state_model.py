import numpy as np
import matplotlib.pyplot as plt

fig,ax = plt.subplots(1,1,figsize=(6,4))
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2)
ax.set_aspect('equal')

cb=ax.scatter(np.concatenate(dihedral)[:,0],np.concatenate(dihedral)[:,1],c=np.concatenate(ood_scores),cmap='coolwarm',s=1,alpha=1)
cb.set_clim(0.0,thres)

ccc = fig.colorbar(cb)
ccc.ax.tick_params(labelsize=15,length=5,width=1.5)
ccc.set_label('OOD score',fontsize=18)

ax.set_xlim(-np.pi,np.pi)
ax.set_ylim(-np.pi,np.pi)

# Set axis labels with phi (ϕ) and psi (ψ) symbols
ax.set_xlabel(r'$\phi$', fontsize=20)
ax.set_ylabel(r'$\psi$', fontsize=20)

ax.set_xticks([-np.pi,0,np.pi],[-180,0,180])
ax.set_yticks([-np.pi,0,np.pi],[-180,0,180])

cs = ax.contour(X, Y, Z,
            colors='black',
            linewidths=1,
            levels=np.linspace(0, 12, 20), alpha=0.6,
            zorder=1, vmin=0, vmax=12)
ax.tick_params(axis="both",labelsize=17.5,direction='out',length=7.5,width=2.5)

r=0.1
g=0.1
b=0.2
ax.patch.set_facecolor((r,g,b,.15))

# Save the plot
plt.savefig("4state_free_energy_landscape.png", dpi=300)

r = 1
pi = np.pi
cos = np.cos
sin = np.sin
phi, theta = np.mgrid[0.0:pi:100j, 0.0:2.0*pi:100j]
x = r*sin(phi)*cos(theta)
y = r*sin(phi)*sin(theta)
z = r*cos(phi)


plt.rcParams['figure.figsize'] = (6,4)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(
   x, y, z,  rstride=2, cstride=2, color='c', alpha=0.1, linewidth=100,antialiased=False)

ax.plot([0,state_centers[0,0]],[0,state_centers[0,1]],[0,state_centers[0,2]],linewidth=2,color='black',linestyle='--')
ax.plot([0,state_centers[1,0]],[0,state_centers[1,1]],[0,state_centers[1,2]],linewidth=2,color='black',linestyle='--')
ax.plot([0,state_centers[2,0]],[0,state_centers[2,1]],[0,state_centers[2,2]],linewidth=2,color='black',linestyle='--')
ax.plot([0,state_centers[3,0]],[0,state_centers[3,1]],[0,state_centers[3,2]],linewidth=2,color='black',linestyle='--')

cb = ax.scatter(np.concatenate(features)[:,0],np.concatenate(features)[:,1],np.concatenate(features)[:,2],c=ood_scores[:],s=1,alpha=1,cmap='coolwarm')
cb.set_clim(0.0,thres)

ccc = fig.colorbar(cb)
ccc.ax.tick_params(labelsize=10,length=3,width=1.5)
ccc.set_label('OOD score',fontsize=18)

ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])
ax.set_xticks([-1,-0.5,0,0.5,1])
ax.set_yticks([-1,-0.5,0,0.5,1])
ax.set_zticks([-1,-0.5,0,0.5,1],[-1,-0.5,0,0.5,1])
ax.set_aspect("equal")
ax.tick_params(axis="both",labelsize=10,direction='out',length=7.5,width=2.5)

ax.set_xlabel('z1',fontsize=15)
ax.set_ylabel('z2',fontsize=15)
ax.set_zlabel('z3',fontsize=15)

ax.view_init(elev=20, azim=50)

# Save the plot
plt.savefig("4state_hypersphere.png", dpi=300)
