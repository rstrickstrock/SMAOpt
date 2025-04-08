#!/bin/bash
#SBATCH --partition=hpc1,hpc3
#SBATCH --nodes=1
#SBATCH --mem 1G
#SBATCH --time=72:00:00
#SBATCH --job-name=sim_steering

python 02_start_simulations.py
