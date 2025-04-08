#! /bin/bash
#SBATCH --partition=hpc1,hpc3
#SBATCH --nodes=1
#SBATCH --mem 5G
#SBATCH --time=00:10:00
#SBATCH --job-name=eval_density

module load gcc/13.2.0
module load gromacs/default

echo -e "density\n" | gmx energy -f 14_prod.edr -o density
