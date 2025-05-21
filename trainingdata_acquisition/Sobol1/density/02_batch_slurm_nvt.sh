#!/bin/bash
#SBATCH --partition=hpc1,hpc3
#SBATCH --nodes=1
#SBATCH --mem 25G
#SBATCH --time=03:00:00
#SBATCH --job-name=nvt

module load gcc/13.2.0
module load gromacs/default

gmx grompp -f 02_nvt.mdp -c 11_emin.gro -p 00_topol.top -o 12_nvt.tpr

gmx mdrun -v -deffnm 12_nvt

