#! /bin/bash
result_cwd=$1

for file in $result_cwd/slurm-*
do
    boolReadDensity=false
    while IFS= read -r line
    do
      #echo $line
      if $boolReadDensity
      then
        #echo $line
        read -a strarr <<< $line
        echo ${strarr[0]}
        break
      fi
      
      if [[ $line == *"this_prediction:"* ]]
      then
        boolReadDensity=true
      fi
    done <$file
done
