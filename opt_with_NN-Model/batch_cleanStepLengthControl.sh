#!/bin/bash
#SBATCH --partition=hpc,hpc1,hpc3
#SBATCH --nodes=1
#SBATCH --mem 5G
#SBATCH --time=12:00:00
#SBATCH --job-name=cleanup

python cleanStepLengthControl.py
