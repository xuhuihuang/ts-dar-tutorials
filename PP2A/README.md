# This folder contains the following:
1. The Jupyter notebook for PP2A: (./PP2A.ipynb)
2. Examples of trained models ./trained_model_examples/

The featurized MD trajectories are avaialble on Zenodo: https://zenodo.org/records/17469029/files/PP2A_data.zip?download=1

Note: In the notebook, the directory paths are set to ./PP2A_data/ for the dataset and ./trained_model_examples/ for the trained models. Keep the PP2A_data/ and trained_model_examples/ folders in the same directory as the notebook. If you store them elsewhere, update the paths in the notebook before running the code. Also, for reference, it takes approximately 4 minutes to train a TS-DAR model for PP2A on an Apple M3 Mac (60 epochs total). It takes around 2.5 minutes to pretrain (first 50 epochs) and 1.5 minutes to complete training (last 10 epochs).
