#!/bin/sh
#This file is called submit-script.sh
#SBATCH --partition=pre       # default "univ2", if not specified
#SBATCH --time=0-05:00:00       # run time in days-hh:mm:ss
#SBATCH --nodes=2               # require 2 nodes
#SBATCH --ntasks-per-node=1    # cpus per node (by default, "ntasks"="cpus")
#SBATCH --mem=128000             # RAM per node
#SBATCH --error=job.%J.err
#SBATCH --output=job.%J.out

conda activate tsdar39 #activate your environment

python train.py
