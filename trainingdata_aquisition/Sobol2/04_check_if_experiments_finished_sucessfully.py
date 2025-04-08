import os
import glob

def read_started_simulations_file(filename):
  with open(filename, 'r') as f:
    lines = f.readlines()
  
  simulation_directories = []
  for line in lines:
    #print(f'{line}')
    line = line.split("\n")[0]
    line = line.split(",")
    dirname = ""
    for item in line:
      dirname = dirname + str(item[1:]) + "_"
    dirname = dirname[:-2]
    #print(f'dirname: {dirname}')
    simulation_directories.append(dirname)
    
  return simulation_directories
  

def create_logfile(filename):
  if os.path.isfile(filename):
    os.remove(filename)
  with open(filename, 'w') as f:
    f.write("Checking if production runs are terminated sucessfully.\n")
    

def write_log(filename, msg):
  with open(filename, 'a') as f:
    f.write(str(msg) + "\n")


def create_rerun_script(filename):
  if os.path.isfile(filename):
    os.remove(filename)
  with open(filename, 'w') as f:
    f.write(f'# rerun follwing setups:\n')
    

def write_to_rerun_script(filename, msg):
  with open(filename, 'a') as f:
    f.write(str(msg) + "\n")
   
     
if __name__ == "__main__":  
  ## set bool to check if some simulations did not terminate correctly
  all_good = True
  
  cwd = os.getcwd()
  #print(f'CWD: {cwd}')

  ## create logfile
  logfile = os.path.join(cwd, "14_check_if_finished.log")
  create_logfile(logfile)
  write_log(logfile, cwd)
  
  logfile_timelimit = os.path.join(cwd, "14_cancelled_due_to_time_limit.log")
  create_logfile(logfile_timelimit)
  write_log(logfile_timelimit, cwd)
  
  rerun_script = os.path.join(cwd, "14_rerun_cancelled_due_to_time_limit.sh")
  create_rerun_script(rerun_script)
  remove_rerun_script = True ## remove at the end of script, if not used
  
  ## get/loop over all simulation directories
  started_simulations_filename = "started_simulations.txt"
  simulation_directories = read_started_simulations_file(started_simulations_filename)
  #print(f'simulation directories: \n{simulation_directories}')
  
  for simdir in simulation_directories:
    write_log(logfile, f'checking: {simdir}')
    simulation_directory = os.path.join(cwd, "experiments", simdir, "density/*")
    #print(f'simulation directory: {simulation_directory}')
    
    ## get all slurm files in simulation directory
    slurm_files = [x for x in glob.glob(simulation_directory) if "slurm-" in x]
    ## check for production run
    for f in slurm_files:
      #print(f'slurmfile: \n{f}')
      with open(f, 'r') as myfile:
        filecontent = myfile.read()
        #print(f'filecontent:\n{filecontent.split("\n")}')
        #print(f'len(filecontent):\n{len(filecontent)}')
        #sprint(f'type(filecontent):\n{type(filecontent)}')
        #filecontent = filecontent.split("\n")
        #print(f'filecontent:\n{filecontent}')
        #print(f'filecontent[-1]:\n{filecontent[-1]}')

        if "gmx grompp -f 04_prod.mdp" in filecontent:
          ## if True - production run:
          #print(f'{f}\ncontains information about the production run')
          write_log(logfile, f'\tslurmfile: {os.path.basename(f)}')
          ## check if final coordinates are written:
          if "Writing final coordinates." in filecontent:
            ## if True - everything terminated correctly
            write_log(logfile, f'\tFinal coordinates written.')
            #pass
          else:
            ## if False - something went wrong?
            all_good = False
            write_log(logfile, f'!! WARNING: check {f} !!')
            #print(f'WARNING: Check {f}\n')
            if "CANCELLED" in filecontent and "TIME LIMIT" in filecontent:
              ## job cancelled due to time limit. Consider restart
              write_log(logfile_timelimit, f'{simdir} got cancelled due to time limit.')
              ## write to rerun script and prevent deleting it
              remove_rerun_script = False
              rerun_msg = f'cd {simulation_directory[:-1]}\npython run_sim_chain.py\nsleep 1\ncd {cwd}\n'
              write_to_rerun_script(rerun_script, rerun_msg)
            else:
              i = 0
              filecontent = filecontent.split("\n")
              while True:
                line = filecontent[-1-i]
                if len(line) > 0:
                  if "will finish" in line or "remaining wall clock time" in line:
                    write_log(logfile, f'\tSim still running?!')
                  else:
                    write_log(logfile, f'\t{line}')
                    write_log(logfile, f'\tERROR?!')
                  break
                else:
                  i = i + 1
        #else:
        #  write_log(logfile, f'\tprod not started, yet.')

  if not all_good:
    print(f'Probably not all production runs termianted sucessfully. Check logfile:\n{logfile}')
  else:
    print(f'Seems like everything terminated sucessfully.')
  
  if remove_rerun_script:
    os.remove(rerun_script)
    
