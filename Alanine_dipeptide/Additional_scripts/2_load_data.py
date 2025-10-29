import numpy as np

# Initialize lists to store trajectory data
data = []
dihedral = []

# Define base directory path (Modify as needed)
base_dir = './Alanine_dipeptide_data/'

# Load 3D atomic coordinates (trajectories)
for i in range(3):
    data_file_path = f'{base_dir}xyz_traj{i}.npy'  # Construct file path
    data.append(np.load(data_file_path))  # Load and append trajectory

# Load dihedral angles (Backbone torsion angles)
for i in range(3):
    d_file_path = f'{base_dir}dihedral_traj{i}.npy'  # Construct file path
    dihedral.append(np.load(d_file_path))  # Load and append trajectory

# Print dataset shapes to confirm loading
print(f"Loaded {len(data)} XYZ trajectories with shapes: {[d.shape for d in data]}")
print(f"Loaded {len(dihedral)} dihedral trajectories with shapes: {[d.shape for d in dihedral]}")
