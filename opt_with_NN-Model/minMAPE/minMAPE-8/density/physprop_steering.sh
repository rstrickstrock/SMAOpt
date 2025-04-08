#!/bin/bash
script_path=$(dirname $0)
sim_cwd=$1
sim_type=$2
iteration=$3
direction=$4
sig1=$5
sig2=$6
eps1=$7
eps2=$8

sim_cwd=$sim_cwd/$sim_type.$iteration.$direction
#echo $sim_cwd
# create working dir and copy all necessary files
mkdir $sim_cwd
cp $script_path/batch_slurm_evalSurrogateModel.sh $script_path/loadEvalSurrogModel.py $script_path/trainedModel.pth $script_path/modelConfig.csv $sim_cwd
ln -s $script_path/trainedModel.pth $sim_cwd/trainedModel.pth

#adapt parameters
#sed 's/day/night/' <old >new
sed "s/SC,SH,EC,EH/$sig1,$sig2,$eps1,$eps2/" <$script_path/this_parameters.csv >$sim_cwd/this_parameters.csv

#copy files for simulation evaluation
cp $script_path/batch_slurm_eval_PhysProp.sh $sim_cwd

# execute simulation
cd $sim_cwd
sbatch batch_slurm_evalSurrogateModel.sh

