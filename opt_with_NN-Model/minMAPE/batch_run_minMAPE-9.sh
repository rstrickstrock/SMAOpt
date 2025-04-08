#!/bin/bash
#SBATCH --partition=hpc,hpc1,hpc3
#SBATCH --nodes=1
#SBATCH --mem 1G
#SBATCH --time=72:00:00
#SBATCH --job-name=mM-9

./run_minMAPE-9.sh
