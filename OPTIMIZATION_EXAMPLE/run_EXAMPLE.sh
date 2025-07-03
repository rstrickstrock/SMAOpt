#! /bin/bash
cwd="/home/rstric3m/current_sim/SMAOpt/OPTIMIZATION_EXAMPLE/EXAMPLE_FILES"
if [[ -d $cwd/PhysProp ]]; then
  rm -rf $cwd/PhysProp
fi
if [[ -d $cwd/QMMM ]]; then
  rm -rf $cwd/QMMM
fi
if [[ -f $cwd/example.log ]]; then
  rm $cwd/example.log
fi

miscffoptiw="python /home/rstric3m/current_sim/SMAOpt/FFLOW_FOR_EXAMPLE/main.py"

$miscffoptiw $cwd/octane_hybrid_new.cfg -d
