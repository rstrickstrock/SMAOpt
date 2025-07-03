REPOSITORY CONTENTS:
 - fflow/
   - contains the optimization workflow
   - run the optimization workflow by calling:
     python /path/to/main.py fflow_config_file.cfg [-d] [-v]

     example fflow_config_file.cfg in fflow/
     
     use -v for verbose-mode: print essential notifications
     
     use -d for debug-mode: print everything

 - opt_with_NN-Model/
   - contains the optimizations' working direcotries and result directories
   - can be rerun by calling maxR2/run-all.sh or minMAPE/run-all.sh
     *NOTE: adaptions to the batch- and steering-scripts might be necessary, depending on the used hardware/software (see "RUNNING AN OPTIMIZATION" below)

      Software toolkits Gromacs and AmberTools are required. For the results herein Gromacs 2024.1 and AmberTools18 were used. The queueing software for the used computing cluster is slurm 23.11.0.
   - maxR2-results and minMAPE-results contain the result data presented in the manuscript 


 - surrogateModelTraining/
   - contains the scripts to train the models as presented in the manuscript
     *NOTE: adaptions to the batch- or pythonscripts for the automatized MD simulation steering might be necessary. Gromacs 2024.1 and slurm 23.11.0 were used.

 - trainingdata_acquisition/
   - contains the scripts to create the data used for the surrogate model training
     *NOTE: adaptions to the batch- or pythonscripts for the automatized MD simulation steering might be necessary. Gromacs 2024.1 and slurm 23.11.0 were used.



RUNNING AN OPTIMIZATION:
