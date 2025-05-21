#!/bin/bash
#SBATCH --partition=hpc1,hpc3
#SBATCH --nodes=1
#SBATCH --mem 1G
#SBATCH --time=02:00:00
#SBATCH --job-name=get_results

python 05_calculate_results.py
