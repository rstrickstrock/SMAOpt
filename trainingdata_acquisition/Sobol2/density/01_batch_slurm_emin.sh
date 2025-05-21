#!/bin/bash
#SBATCH --partition=hpc1,hpc3
#SBATCH --nodes=1
#SBATCH --mem 25G
#SBATCH --time=01:00:00
#SBATCH --job-name=emin

module load gcc/13.2.0
module load gromacs/default

gmx grompp -f 01_emin.mdp -c 00_octane_box.gro -p 00_topol.top -o 11_emin.tpr

gmx mdrun -v -deffnm 11_emin

