import numpy as np
import torch
from torch.utils.data.dataloader import DataLoader
from torch.utils.data import random_split

from tsdar.utils import set_random_seed
from tsdar.loss import Prototypes
from tsdar.model import TSDAR, TSDARLayer, TSDAREstimator
from tsdar.dataprocessing import Preprocessing

pre = Preprocessing(dtype=np.float32)
dataset = pre.create_dataset(lag_time=1,data=data) #The lag_time used to create the dataset consisting of time-instant and time-lagged data

# Ensure reproducibility by setting a fixed random seed
set_random_seed(10)

# Split dataset: 90% training, 10% validation
val = int(len(dataset)*0.10) #compute validation size
train_data, val_data = torch.utils.data.random_split(dataset, [len(dataset)-val, val]) # randomly split the data

loader_train = DataLoader(train_data, batch_size=1000, shuffle=True) # load data in batches and shuffle data
loader_val = DataLoader(val_data, batch_size=len(val_data), shuffle=False) # single batch

# Initialize the TS-DAR model with specific network architecture
lobe = TSDARLayer([30,30,30,30,10,2],n_states=2)

# Define device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Move model to appropriate device (CPU/GPU)
lobe = lobe.to(device=device)

# Initialize TS-DAR model for training
tsdar = TSDAR(lobe = lobe, learning_rate = 1e-3, device = device, mode = 'regularize', beta=0.01, feat_dim=2, n_states=2, pretrain=10)
tsdar_model = tsdar.fit(loader_train, n_epochs=20, validation_loader=loader_val).fetch_model()

validation_vamp = tsdar.validation_vamp
validation_dis = tsdar.validation_dis
validation_prototypes = tsdar.validation_prototypes

training_vamp = tsdar.training_vamp
training_dis = tsdar.training_dis

np.save(('validation_vamp.npy'),validation_vamp)
np.save(('validation_dis.npy'),validation_dis)
np.save(('validation_prototypes.npy'),validation_prototypes)

np.save(('training_vamp.npy'),training_vamp)
np.save(('training_dis.npy'),training_dis)

hypersphere_embs = tsdar_model.transform(data=data,return_type='hypersphere_embs')
metastable_states = tsdar_model.transform(data=data,return_type='states')

tsdar_estimator = TSDAREstimator(tsdar_model)
ood_scores = tsdar_estimator.fit(data).ood_scores
state_centers = tsdar_estimator.fit(data).state_centers

hypersphere_embs = np.array(hypersphere_embs,dtype=object)
metastable_states = np.array(metastable_states,dtype=object)
ood_scores = np.array(ood_scores,dtype=object)

np.save(('hypersphere_embs.npy'), hypersphere_embs, allow_pickle=True)
np.save(('metastable_states.npy'), metastable_states, allow_pickle=True)
np.save(('ood_scores.npy'), ood_scores, allow_pickle=True)
np.save(('state_centers.npy'), state_centers)

torch.save(tsdar_model.lobe.state_dict(), 'model.pt')
