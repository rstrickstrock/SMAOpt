#! /bin/bash
eval_cwd=$1
#echo "eval_cwd: $eval_cwd"

cd $eval_cwd
#sbatch batch_slurm_eval_PhysProp.sh
echo "this_prediction:" >> slurm-xyz.txt
echo $(tail -1 this_prediction.csv | cut -f 2 -d ",") >> slurm-xyz.txt

