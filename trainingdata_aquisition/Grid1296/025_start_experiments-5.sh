#! /bin/bash
cd experiments/

for directory in 0.275_*; do
  #echo $directory
  cd $directory

  cd density/
  sbatch batch_slurm_prod.sh
  cd ..
  
  #cd energies/
  #sbatch batch_slurm_RCE.sh
  #cd ..

  cd ..
done
