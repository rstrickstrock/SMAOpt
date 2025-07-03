REPOSITORY CONTENTS:
- FFLOW_FOR_EXAMPLE/
  - contains the optimization workflow to run the example in OPTIMIZATION_EXAMPLE/
    *NOTE: This Code can only be used to run the example. The code is altered to enable the example to be run with only a python3 installation (no Gromacs, Amber, slurm required)

- OPTIMIZATION_EXAMPLE/
  - contains the files for the example optimization
    *NOTE: This optimization is an example and it's purpose is to demonstrate the workflow. The Energy calculations are replaced by a dummy output and are not real values. Thus, the resulting force field parameters are meaningless.
  - run the example by:
    - change "cwd" in EXAMPLE_FILES/octane_hybrid_new.cfg to the location of octane_hybrid_new.cfg (e.g. /path/to/EXAMPLE_FILES/)
    - change "cwd" in run_EXAMPLE.sh to the location of octane_hybrid_new.cfg (e.g. /path/to/EXAMPLE_FILES/)
    - run run_EXAMPLE.sh
    
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
