import os
import numpy as np
import torch
import torch.nn as nn

from torch.utils.data.dataloader import DataLoader
from torch.utils.data import random_split

from tsdar.utils import set_random_seed
from tsdar.loss import Prototypes
from tsdar.model import TSDAR, TSDARLayer, TSDARModel, TSDAREstimator
from tsdar.dataprocessing import Preprocessing

data = []
for i in range(153):
    filename = "../HP35_data/ftraj_%03d.npy" % i
    if os.path.exists(filename):  # Check if file exists
        data.append(np.load(filename))
    else:
        print(f"Warning: {filename} not found.")

device = torch.device('cpu')

pre = Preprocessing(dtype=np.float32)
dataset = pre.create_dataset(lag_time=100, data=data) # lag time = 20 ns

set_random_seed(50)

for k in range(5):

    val = int(len(dataset)*0.20)
    train_data, val_data = torch.utils.data.random_split(dataset, [len(dataset)-val, val])

    loader_train = DataLoader(train_data, batch_size=10000, shuffle=True)
    loader_val = DataLoader(val_data, batch_size=len(val_data), shuffle=False)

    lobe = TSDARLayer([528,200,100,50,25,10,3],n_states=4)
    lobe = lobe.to(device=device)

    tsdar = TSDAR(lobe = lobe, learning_rate = 1e-3, device = device, mode = 'regularize', beta=0.01, feat_dim=3, n_states=4, pretrain=15, print=True, save_model_interval=1)
    tsdar_model = tsdar.fit(loader_train, n_epochs=30, validation_loader=loader_val).fetch_model()

    os.makedirs(f'./new_trained_models/{k+1}', exist_ok=True)
    os.chdir(f'./new_trained_models/{k+1}')

    validation_vamp = tsdar.validation_vamp
    validation_dis = tsdar.validation_dis
    validation_prototypes = tsdar.validation_prototypes

    training_vamp = tsdar.training_vamp
    training_dis = tsdar.training_dis

    np.save('validation_vamp',validation_vamp)
    np.save('validation_dis',validation_dis)
    np.save('validation_prototypes',validation_prototypes)

    np.save('training_vamp',training_vamp)
    np.save('training_dis',training_dis)

    for i in range(len(tsdar._save_models)):
        torch.save(tsdar._save_models[i].lobe.state_dict(), 'model_{}epochs.pytorch'.format(i+1))
    os.chdir(r'../../')
