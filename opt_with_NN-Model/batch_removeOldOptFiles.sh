#!/bin/bash
#SBATCH --partition=hpc,hpc1,hpc3
#SBATCH --nodes=1
#SBATCH --mem 1G
#SBATCH --time=01:00:00
#SBATCH --job-name=rmOldF

python removeOldOptFiles.py
