#!/bin/bash
#SBATCH --partition=hpc1,hpc3
#SBATCH --nodes=1
#SBATCH --mem 75G
#SBATCH --time=24:00:00
#SBATCH --job-name=prod

module load gcc/13.2.0
module load gromacs/default

gmx grompp -f 04_prod.mdp -c 13_npt.gro -t 13_npt.cpt -p 00_topol.top -o 14_prod.tpr

gmx mdrun -v -deffnm 14_prod

