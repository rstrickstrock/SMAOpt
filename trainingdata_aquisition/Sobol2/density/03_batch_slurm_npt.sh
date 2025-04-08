#!/bin/bash
#SBATCH --partition=hpc1,hpc3
#SBATCH --nodes=1
#SBATCH --mem 25G
#SBATCH --time=10:00:00
#SBATCH --job-name=npt

module load gcc/13.2.0
module load gromacs/default

gmx grompp -f 03_npt.mdp -c 12_nvt.gro -t 12_nvt.cpt -p 00_topol.top -o 13_npt.tpr

gmx mdrun -v -deffnm 13_npt

