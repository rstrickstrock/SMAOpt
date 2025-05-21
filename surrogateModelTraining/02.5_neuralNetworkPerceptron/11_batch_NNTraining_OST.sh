#!/bin/bash
#SBATCH --partition=hpc,hpc1,hpc3
#SBATCH --nodes=1
#SBATCH --mem 32G
#SBATCH --time=5:00:00
#SBATCH --job-name=NNR

python 11_OST.py
