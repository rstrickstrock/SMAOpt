#! /bin/bash

cwd=$(pwd)
logfile="LOG_check_finished_sucessfully-5.log"
logfile=$cwd/$logfile

if [[ -f $logfile ]]; then
  rm $logfile
fi
touch $logfile

echo $(date) >$logfile
echo "" >>$logfile

all_good=true

cd experiments
for experiment in 0.25_*; do
  cd $experiment
  echo "Checking $experiment .." >>$logfile

  cd density
  msg=$(tail -2 slurm-* | head -1)
  msg=${msg:0:19}
  if [[ $msg == "GROMACS reminds you" ]]; then
    # sucessfully terminated
    echo -e "+\tterminated sucessfully (MD)" >>$logfile
  else
    # maybe a problem
    echo -e "!!!\tPROBLEM in MD run?" >>$logfile
    all_good=false
  fi
  cd ..

  cd energies
  msg=$(tail -2 slurm-* | head -1)
  msg=${msg:0:22}
  if [[ $msg == "Minimization finished." ]]; then
    # sucessfully terminated
    echo -e "+\tterminated sucessfully (MM)" >>$logfile
  else
    # maybe a problem
    echo -e "!!!\tPROBLEM in MM run?" >>$logfile
    all_good=false
  fi
  cd ..

  cd ..
done

if $all_good; then
  echo -e "Everything terminated sucessfully.\nDone."
  echo -e "\n\nEverything terminated sucessfully.\nDone." >>$logfile
else
  echo -e "!!! There were some Errors.\nDone."
  echo -e "\n\n!!! There were some Errors.\nDone." >>$logfile
fi
