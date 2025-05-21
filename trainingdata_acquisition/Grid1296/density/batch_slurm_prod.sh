#!/bin/bash
#SBATCH --partition=hpc1
#SBATCH --nodes=1
#SBATCH --mem 25G
#SBATCH --time=01:00:00
#SBATCH --job-name=density

module load gcc/13.2.0
module load gromacs/default

gmx grompp -f prod.mdp -c equilibrated.gro -t equilibrated.cpt -p topol.top -o prod.tpr

gmx mdrun -v -deffnm prod

