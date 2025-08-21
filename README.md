# TS-DAR Tutorials
This tutorial provides a Practical Guide to Transition State Analysis in Biomolecular Simulations with TS-DAR

![Fig_1](https://github.com/user-attachments/assets/673f7073-a74c-4c42-8580-80f6713cbae9)

### Content:
You'll find below step-by-step Jupyter notebooks that guide the construction of TS-DAR models in three systems: (a). the alanine dipeptide, (b). villin headpiece, and (c) PP2A. 

The MD trajectories as training datasets have been converted into features and are available at https://zenodo.org/records/16922765

**A. For the alanine dipeptide system:**
Featurized MD trajectories: [https://zenodo.org/records/16922765/files/Alanine_dipeptide.zip?download=1]

TS-DAR tutorial notebook for alanine dipeptide: (./Alanine-dipeptide/Alanine_dipeptide.ipynb)

**B. For the villin headpiece (HP35) system:**
Featurized MD trajectories: [https://zenodo.org/records/16922765/files/HP35.zip?download=1]

TS-DAR tutorial notebook for HP35: (./HP35/HP35.ipynb)

**C. For the PP2A system:**
Featurized MD trajectories: [https://zenodo.org/records/16922765/files/PP2A.zip?download=1]

TS-DAR tutorial notebook for PP2A: (./PP2A/PP2A.ipynb)

### Installation Guide:
#### 1. Download and install Anaconda:
wget https://repo.anaconda.com/archive/Anaconda3-2024.06-1-Linux-x86_64.sh <br>
./Anaconda3-2024.06-1-Linux-x86_64.sh
#### 2. Create a new conda environment and install the ts-dar source code locally:
conda create -n ts-dar python=3.9 <br>
conda activate ts-dar <br>
#### 3. Install dependencies
!pip install matplotlib numpy==1.26.1 scipy==1.11.4 torch==1.13.1 tqdm==4.66.1
#### 4. Clone the repository
!git clone https://github.com/xuhuihuang/ts-dar.git
#### 5. Install the package
!python -m pip install ./ts-dar

