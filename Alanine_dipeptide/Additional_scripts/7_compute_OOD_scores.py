import numpy as np
from tsdar.model import TSDAR, TSDARLayer, TSDAREstimator, TSDARModel

lobe.load_state_dict(torch.load('./model.pt', map_location=torch.device('cpu')))
tsdar_model = TSDARModel(lobe=lobe)

# Initialize the TS-DAR Estimator to compute metastable state centers
tsdar_estimator = TSDAREstimator(tsdar_model)

# Compute Out-of-Distribution (OOD) scores
ood_scores = tsdar_estimator.fit(data).ood_scores

# Extract the hyperspherical embeddings (transformed feature representation)
features = tsdar_model.transform(data,return_type='hypersphere_embs')

# Compute the state center vectors for metastable states on the hypersphere
state_centers = tsdar_estimator.fit(data).state_centers

# Compute pairwise anglular distances between metastable state centers
sim_mat = np.arccos(state_centers.dot(state_centers.T))
np.fill_diagonal(sim_mat,val=np.pi)

# OOD Threshold Computation:

# Theoretical threshold (based on minimum angle between state centers)
thres = -np.cos(sim_mat.min()/2)+1

# Empirical threshold (based on maximum OOD score)
#thres = np.max(np.concatenate(ood_scores))

