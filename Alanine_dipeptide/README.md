# This folder contains the following:
1. The Jupyter notebook for alanine dipeptide: (./Alanine_dipeptide.ipynb)
2. Additional scripts for those running on the command line or on HPC or CHTC systems.

The featurized MD trajectories are available from Zenodo: https://zenodo.org/records/17469029/files/Alanine_dipeptide_data.zip?download=1

Note: the base_dir is set to './Alanine_dipeptide_data/' in the notebook. Keep the Alanine_dipeptide_data/ folder in the same directory as the notebook. If you decide to store the data elsewhere, update the directory path in the notebook before running the code. Also, for reference, it takes approximately 5.5 minutes to train a TS-DAR model for alanine dipeptide on an Apple M3 Mac (20 epochs total). It takes around 30 seconds to pretrain (first 10 epochs) and 5 minutes to complete training (last 10 epochs).
