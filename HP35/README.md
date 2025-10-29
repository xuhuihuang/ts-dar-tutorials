# This folder contains the following:
1. The Jupyter notebook for Villin Headpiece (HP35): (./HP35.ipynb)
2. Examples of trained models ./trained_model_examples/
3. The Python code to train the TS-DAR models: (./trained_model_examples/train.py)
4. Additional scripts for those running on HPC or HTC systems.

The featurized MD trajectories are available on Zenodo: https://zenodo.org/records/17469029/files/HP35_data.zip?download=1

Note: In the notebook, the directory paths are set to ./HP35_data/ for the featurized dataset and ./trained_model_examples/ for the trained models. Keep the HP35_data/ and trained_model_examples/ folders in the same directory as the notebook. If you store them elsewhere, update the paths in the notebook before running the code. Also, for reference, it takes approximately 20 minutes to train a TS-DAR model for HP35 on an Apple M3 Mac (30 epochs total). It takes around 3 minutes to pretrain (first 15 epochs) and 17 minutes to complete training (last 15 epochs).
