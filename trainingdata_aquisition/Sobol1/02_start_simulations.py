import subprocess
import time
from multiprocessing import Process
import os
import pandas as pd
  
  
def read_parameter_file(filepath):
  """
  reads parameter sets from csv file (column-wise listed parameters for SigC, SigH, EpsC, EpsC)
  and returns a list continaint [[SigC1, SigH1, EpsC1, EpsH1], [set2], [set3], ...] 
  """
  try:
    if os.path.isfile(filepath):
      filepath = os.path.abspath(filepath)
    else:
      print(f'File \"{filepath}\" does not exist.')
      print(f'exit.')
      exit()
  except:
    print(f'file = os.path.abspath({filepath}) does not work.')
    print(f'{exit}')
    exit()

  df_parameters = pd.read_csv(filepath)
  #print(f'{df_parameters}')
  #print(f'{df_parameters.columns}')
  df_parameters = df_parameters.drop(columns=['Unnamed: 0'])
  #print(f'{df_parameters}')
  SigC = df_parameters.loc[:,'SigC'].to_numpy()
  #print(f'{SigC}')
  SigH = df_parameters.loc[:,'SigH'].to_numpy()
  EpsC = df_parameters.loc[:,'EpsC'].to_numpy()
  EpsH = df_parameters.loc[:,'EpsH'].to_numpy()
  parameter_sets = []
  for i in range(0, len(SigC)):
    parameter_sets.append([SigC[i], SigH[i], EpsC[i], EpsH[i]])
  #print(f'{parameter_sets}')
  
  return parameter_sets
  

def write_sim_started_file(executed_simulations_file, pars):
  with open(executed_simulations_file, 'a') as f:
      f.write(f'{pars}')
      f.write(f'\n')


def check_if_parameters_already_started(executed_simulations_file, parameters):
  """
  returns True if simulations for parameters are in executed_simulation_file (a.k.a simulations have already been started)
  returns False otherwise
  """
  ## read all started parameters
  with open(executed_simulations_file, 'r') as f:
    started_sims = f.readlines()
  
  ## check if simulations for parameters pars already started:
  for started_sim in started_sims:
    started_sim = started_sim.split("\n")
    if str(parameters) == started_sim[0]:
      ## simulations arleady started - return True
      #print(f'Sims for parameters {parameters} already started. Returning True')
      return True
  ## if parameters not in started sims - return False
  #print(f'Sims for parameters {parameters} not yet started. Returning False')
  return False


def run_script(path_to_simdir):
  os.chdir(path_to_simdir)
  subprocess.run(["python","run_sim_chain.py"])
  time.sleep(1)  # Adjust the delay as needed


def main(parameters, max_jobs, executed_simulations_file, check_intervall):
  processes = []

  # Start 'max_jobs' instances of the script
  for pid in range(len(parameters)):
    ## check if sims for parameters already started
    already_started = check_if_parameters_already_started(executed_simulations_file, parameters[pid])
    if already_started:
      ## if true - sims already stared - skip
      print(f"Sims with parameters: {parameters[pid]} already started. Skipped\n")
      #increase max_jobs, to have the prev defined max_jobs eventually running
      max_jobs = max_jobs + 1
      #pass
    else:
      ## if not true - sims not started - start sims     
      ## get dir path for simdir
      dirname = str(parameters[pid][0]) + "_" + str(parameters[pid][1]) + "_" + str(parameters[pid][2]) + "_" + str(parameters[pid][3])
      path_to_simdir= os.path.join("experiments", dirname, "density")
      ## start process
      p = Process(target=run_script, args=(path_to_simdir,))
      p.start()
      processes.append(p)
      ## write parameters to file
      write_sim_started_file(executed_simulations_file, parameters[pid])
      print(f"Started Sims with parameters: {parameters[pid]}\n")
    if pid == max_jobs - 1:
      ## maximum number of parallel running jobs reached - break for loop
      break
    
  ## Monitor and restart the scripts
  while True:
    print(f'Checking running sims.')
    ## assume no process is alive
    alive = False
    
    for idx, p in enumerate(processes):
      #print(f'idx: {idx}')
      #print(f'p: {p}')
      #print(f'p.is_alive(): {p.is_alive()}')
      #print(f'debug 1')
      if not p.is_alive():
        #print(f'debug 2')
        ## Start a new instance to replace the finished one
        pid = pid + 1
        #print(f'pid = {pid}')
        if pid >= len(parameters):
          ## if pid is out of range don't start a new process
          pid = pid - 1
          print(f'pid: {pid} >= len(parameters): {len(parameters)}. Everthing is started. Exit.')
          exit()
        ## check if sims for parameters already started
        while True:
          #print(f'debug 3')
          ## test if parameters already started until already_started=False
          if check_if_parameters_already_started(executed_simulations_file, parameters[pid]):
            ## if true - already started - increase pid by 1 and test again
            pid = pid + 1
            #print(f'pid = {pid}')
            print(f"Sims with parameters: {parameters[pid]} already started. Skipped\n")
            if pid >= len(parameters):
              ## if pid is out of range don't start a new process
              pid = pid - 1
              print(f'pid: {pid} >= len(parameters): {len(parameters)}. Everthing is started. Exit.')
              exit()
          else:
            ## if false - not started - break while loop
            break
        #print(f'debug 4')
        ## get dir path for simdir
        dirname = str(parameters[pid][0]) + "_" + str(parameters[pid][1]) + "_" + str(parameters[pid][2]) + "_" + str(parameters[pid][3])
        path_to_simdir= os.path.join("experiments", dirname, "density")
        ## start new process
        new_p = Process(target=run_script, args=(path_to_simdir,))
        new_p.start()
        processes[idx] = new_p
        write_sim_started_file(executed_simulations_file, parameters[pid])
        ## new process started, so at least one is aliv
        alive = True
        print(f"Started Sims with parameters: {parameters[pid]}\n")
      else:
        ## if p is alive, set alive to True
        print(f'p: {p} still alive.')
        alive = True
    ## terminate script when no p is alive anymore AND all simulations were started
    if not alive and pid >= len(parameters):
      break
    time.sleep(check_intervall)  # Adjust the delay as needed

if __name__ == "__main__":
  executed_simulations_file = "started_simulations.txt" 
  parameter_file = "parameter_sample.csv"
  max_jobs = 50
  check_intervall = 60
  
  if not os.path.isfile(executed_simulations_file):
  #print(f'{executed_simulations_file} does not exist.')
    f = open(executed_simulations_file, 'w')
    f.close()
  
  parameters = read_parameter_file(parameter_file)
  
  main(parameters, max_jobs, executed_simulations_file, check_intervall)
