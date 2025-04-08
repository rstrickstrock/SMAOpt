#! /bin/bash

number_of_parameter_sets=$(ls $(pwd)/experiments/ | wc -l)
#echo $number_of_parameter_sets

number_of_started_simulations=$(cat $(pwd)/started_simulations.txt | wc -l)
#echo $number_of_started_simulations
#number_of_started_simulations=3
#number_of_parameter_sets=3
echo ""
echo "Number of parameter sets: $number_of_parameter_sets"
echo "Number of started Simulations: $number_of_started_simulations"

if [[ $number_of_started_simulations -eq $number_of_parameter_sets ]]
then
  echo -e "Everything is started.\n"
else
  echo -e "Some Simulations not yet started.\n"
fi
