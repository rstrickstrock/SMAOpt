#! /bin/bash

for file in maxR2/maxR2-*; do cp next_parameters.par $file/parameters.par; done
for file in minMAPE/minMAPE-*; do cp next_parameters.par $file/parameters.par; done
