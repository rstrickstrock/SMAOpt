#! /bin/bash
#SBATCH --partition=hpc1
#SBATCH --nodes=1
#SBATCH --mem 20G
#SBATCH --time=00:05:00
#SBATCH --job-name=eval_density

module load gcc/13.2.0
module load gromacs/default

echo -e "density\n" | gmx energy -f prod.edr -o density
