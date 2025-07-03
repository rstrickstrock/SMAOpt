#! /bin/bash
#SBATCH --partition=hpc,hpc1,hpc3
#SBATCH --nodes=1
#SBATCH --mem 1G
#SBATCH --time=00:01:00
#SBATCH --job-name=eval_density

echo "this_prediction:"
tail -1 this_prediction.csv | cut -f 2 -d ","
