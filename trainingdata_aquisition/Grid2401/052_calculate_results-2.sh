#! /bin/bash

cd experiments
for experiment in 0.1_*; do
  cd $experiment

  cd density/
  sbatch batch_slurm_eval_density.sh
  cd ..

  cd energies/
  sbatch batch_slurm_eval_RCE.sh
  cd ..

  cd ..
done
cd ..
