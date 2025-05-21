import os
import glob
import subprocess
from multiprocessing import Process
import time 
import pandas as pd

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


def get_density(filecontent):
  filecontent = filecontent.split("\n")
  i = 0
  ## check for density
  while True:
    line = filecontent[-1-i]
    if "Density" in line:
      ## density found in 'line'
      break
    else:
      ## density not found in 'line'
      i = i + 1
      if i == len(filecontent): 
        print(f'could not find the density in the file, even though it should be there ...')
        return float(0.0)
        
  line = line.split(" ")
  ## info = [Property, Value, Err.Est., RMSD, Tot-Drift, Unit]
  info = []
  for item in line:
    if len(item) > 0:
      info.append(str(item))
  
  ## return density, density_err
  return [str(info[1]), str(info[2])]


def run_script():
  subprocess.run(["sbatch","04_batch_slurm_eval_density.sh"])
  time.sleep(1)  # Adjust the delay as needed


def calc_density(cwd, simulation_directory, slurmfile=None):
  ## go to simulation working directory
  os.chdir(simulation_directory)
  #print(f'os.remove({slurmfile}).')
  ## remove 'old' slurmfile with failed calculation if not None
  if not slurmfile is None:
    os.remove(slurmfile)
  
  ## (re-)start density calculation 
  #print(f'sbatch 04_batch_slurm_eval_density.sh')
  p = Process(target=run_script)
  p.start()
  #print(f'p: {p}')
  ## wait for it to finish
  while True:
    if not p.is_alive():
      ## process finished, continue
      #print(f'p not alive, continue')
      break
    else:
      ## process not finished, check again in 3 Seconds
      #print(f'p still alive, wait 3 sec')
      time.sleep(3)
  
  ## get all slurmfiles to check for the density
  sfiles = [x for x in glob.glob("./*") if "slurm-" in x]
  #print(f'{sfiles}')
  density = 0.0
  density_err = 100.0
  for sf in sfiles:
    with open(sf, 'r') as myfile:
        filecontent = myfile.read()
    if "gmx energy -f 14_prod.edr -o density" in filecontent:
      if "Last energy frame read" in filecontent:
        ## get density
        [density, density_err] = get_density(filecontent)
      else:
        ## something went wrong here
        print(f'Could somehow not calculate density in {simulation_directory}. Please check.')
        
  ## go back to overall working directory
  os.chdir(cwd)
  return [density, density_err]


if __name__ == "__main__":
  started_simulations_filename = "started_simulations.txt"
  cwd = os.getcwd()
  #print(f'CWD: {cwd}')
  
  ## create dataframe for parameters and densites
  props = ['SigC', 'SigH', 'EpsC', 'EpsH', 'density', 'density_err']
  data = {'#': props}
  df = pd.DataFrame(data)
  #print(f'{df}')
  i = 1
  
  ## loop over all simulation directories
  simulation_directories = read_started_simulations_file(started_simulations_filename)
  #simulation_directories = ["0.0513162060640752_0.0669622149765491_0.8103976989137008_0.0238499061390757"]
  maxi = len(simulation_directories)
  for simdir in simulation_directories:
    print(f'checking results ({i}/{maxi}) ... {simdir}')
    #print(f'simdir: {simdir}')
    ## get all slurm files in simulation directory
    simulation_directory = os.path.join(cwd, "experiments", simdir, "density/*")
    slurm_files = [x for x in glob.glob(simulation_directory) if "slurm-" in x]
    
    ## create dictonary for this parameters/density
    this_dict = []
    parameters = simdir.split("_")
    SigC = parameters[0]
    SigH = parameters[1]
    EpsC = parameters[2]
    EpsH = parameters[3]
    this_dict.append(SigC) # add value for property 'SigC'
    this_dict.append(SigH) # add value for property 'SigH'
    this_dict.append(EpsC) # add value for property 'EpsC'
    this_dict.append(EpsH) # add value for property 'EpsH'
    
    ## check if density calculation already has started and finished sucessfully
    density_calc_started = False
    for f in slurm_files:
      with open(f, 'r') as myfile:
        filecontent = myfile.read()
        
        if "gmx energy -f 14_prod.edr -o density" in filecontent:
        ## density calculation was started
          ## if sucessfull - get density
          if "Last energy frame read" in filecontent:
            density_calc_started = True
            print(f'\tDensity calc started and terminated sucessfully. Getting density.')
            [this_density, this_density_err] = get_density(filecontent)
            print(f'\tDensity: {this_density, this_density_err}')
            
          ## if not sucessfull - remove slurm file, restart density calc and get density
          if "Error" in filecontent:
            density_calc_started = True
            print(f'\tDensity calc started, but not terminated sucessfully. Restart. Removing {os.path.basename(f)}.')
            [this_density, this_density_err] = calc_density(cwd, simulation_directory[:-1], os.path.basename(f))
            print(f'\tDensity: {this_density, this_density_err}')
            #print(f'cwd: {os.getcwd()}')
            
    if not density_calc_started:
      print(f'\tDensity calc not started yet, start calculation ..')
      [this_density, this_density_err] = calc_density(cwd, simulation_directory[:-1])
      print(f'\tDensity: {this_density, this_density_err}')
      
    try:
      this_dict.append(float(this_density))
    except:
      this_dict.append(float(0.0))

    if this_density_err == '--':
      this_density_err = 0.0
      
    try:
      this_dict.append(float(this_density_err))
    except:
      this_dict.append(float(100.0))

    df.insert(len(df.columns), f'{i}', this_dict, True)
    i = i + 1
    
  #print(f'{df}')
  result_CSV_file = 'RESULTS_experiments.csv'
  if os.path.isfile(result_CSV_file):
    os.remove(result_CSV_file)
    
  df.to_csv(result_CSV_file)
  #print(f'len(df): {len(df)}')

            
            
            
            
            
            
            
            
            
            
            
