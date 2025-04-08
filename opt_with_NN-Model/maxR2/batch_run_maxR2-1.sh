#!/bin/bash
#SBATCH --partition=hpc,hpc1,hpc3
#SBATCH --nodes=1
#SBATCH --mem 1G
#SBATCH --time=72:00:00
#SBATCH --job-name=mR2-1

./run_maxR2-1.sh
