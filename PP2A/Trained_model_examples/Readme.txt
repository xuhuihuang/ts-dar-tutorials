This folder contains 10 trained models. The following is a brief description of the files included:

1) hypersphere_embs.npy - embedding of the trajetory frames in the hyperspherical latent space.
2) metastable_states.npy - state assignments for each frame.
3) model.pt - PyTorch trained model.
4) ood_scores.npy - the out-of-distribution scores for each frame.
5) state_centers.npy - coordinates for the metastable state centers in the latent space.
6) training_dis.npy - dispersion loss for the training set.
7) training_vamp.npy - VAMP scores for the training set.
8) validation_dis.npy - dispersion loss for the validation set.
9) validation_prototypes.npy - embeddings of representative frames in the validation set.
10) validation_vamp.npy - VAMP scores for the validation set.

The script used to train the models (train_PP2A.ipynb) is also included for your reference.
