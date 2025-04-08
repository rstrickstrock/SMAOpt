#! /bin/bash
cwd="/home/rstric2s/current_sim/Paper_Octane-3_NN-predictor/opt_with_NN-Model/minMAPE/minMAPE-7"
if [[ -d $cwd/PhysProp ]]; then
  rm -rf $cwd/PhysProp
fi
if [[ -d $cwd/QMMM ]]; then
  rm -rf $cwd/QMMM
fi
if [[ -f $cwd/minMAPE-7.log ]]; then
  rm $cwd/minMAPE-7.log
fi

miscffoptiw="python /home/rstric2s/current_sim/Paper_Octane-3_NN-predictor/fflow/main.py"

$miscffoptiw $cwd/octane_hybrid_new.cfg -d
