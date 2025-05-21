import os
import shutil
import pandas as pd
import numpy as np

parameter_file = "parameter_sample.csv"
experiments_directory = "experiments"

current_working_directory = os.getcwd()
cwd = os.path.join(current_working_directory, experiments_directory)

##############
#### functions
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


def create_simdir(simdir):
  #print(f'simdir: {simdir}')
  try:
    os.mkdir(simdir)
  except:
    print(f'Could not create simdir ({simdir}). Check this. Exit setup.')
    #exit()


def make_density_simdir(current_working_directory, simdir, parameters):
  density_dir = os.path.join(current_working_directory, "density")
  #print(f'density_dir: {density_dir}')
  simdir = os.path.join(simdir, "density")
  #print(f'simdir: {simdir}')
  os.mkdir(simdir)

  ## copy files ##
  ## force-field directory
  shutil.copytree(os.path.join(density_dir, "force-field.ff"),os.path.join(simdir, "force-field.ff"))
  ## topology file
  shutil.copy(os.path.join(density_dir, "00_topol.top"), simdir)
  ## geometrie file
  shutil.copy(os.path.join(density_dir, "00_octane_box.gro"), simdir)
  ## MDP files
  shutil.copy(os.path.join(density_dir, "01_emin.mdp"), simdir)
  shutil.copy(os.path.join(density_dir, "02_nvt.mdp"), simdir)
  shutil.copy(os.path.join(density_dir, "03_npt.mdp"), simdir)
  shutil.copy(os.path.join(density_dir, "04_prod.mdp"), simdir)
  
  ## slurm simulation files
  shutil.copy(os.path.join(density_dir, "01_batch_slurm_emin.sh"), simdir)
  shutil.copy(os.path.join(density_dir, "02_batch_slurm_nvt.sh"), simdir)
  shutil.copy(os.path.join(density_dir, "03_batch_slurm_npt.sh"), simdir)
  shutil.copy(os.path.join(density_dir, "04_batch_slurm_prod.sh"), simdir)
  
  ## slurm evaluation file
  shutil.copy(os.path.join(density_dir, "05_batch_slurm_eval_density.sh"), simdir)
  
  ## python file to run the simulations
  shutil.copy(os.path.join(density_dir, "run_sim_chain.py"), simdir)
  ## for testing!
  #shutil.copy(os.path.join(density_dir, "run_sim_chain-2.py"), simdir)
  
  ## change parameters in topol.top
  topology_file = os.path.join(simdir, "00_topol.top")
  #print(f'topology_file: {topology_file}')
  tmp_topology_file = os.path.join(simdir, "00_topol.tmp")

  with open(topology_file, "rt") as fin:
    with open(tmp_topology_file, "wt") as fout:
      for line in fin:
        fout.write(line.replace('opls_135 opls_135    1',f'opls_135 opls_135    1    {parameters[0]}    {parameters[2]}'))

  with open(tmp_topology_file, "rt") as fin:
    with open(topology_file, "wt") as fout:
      for line in fin:
        fout.write(line.replace('opls_136 opls_136    1',f'opls_136 opls_136    1    {parameters[0]}    {parameters[2]}'))

  with open(topology_file, "rt") as fin:
    with open(tmp_topology_file, "wt") as fout:
      for line in fin:
        fout.write(line.replace('opls_140 opls_140    1',f'opls_140 opls_140    1    {parameters[1]}    {parameters[3]}'))

  shutil.copy(tmp_topology_file, topology_file)
  os.remove(tmp_topology_file)

#### end
##############

## check if directory exists. If true: exit to prevent data loss
if os.path.exists(cwd):
#  print(f'Directory {cwd} already exists. Exit setup.')
  shutil.rmtree(cwd)
  
os.mkdir(cwd)

## get the parameter combinations from csv file
parameters = read_parameter_file(parameter_file)

## for every permutaion create a density simulation directory
#i = 1
for pars in parameters:
  #print(f'permuation: {permutation}')
  dirname = ""
  for value in pars:
    dirname = dirname + str(value) + "_"
  dirname = dirname[:-1]
  #print(f'dirname = {dirname}')

  ## create directory for simulations
  simdir = os.path.join(cwd, dirname)
  create_simdir(simdir)

  make_density_simdir(current_working_directory, simdir, pars)
  #make_energy_simdir(current_working_directory, simdir, pars)
  #print(f'Prepared permuation folder {i}.')
  #i = i + 1
  #if i == 15:
  #  break
print(f'\nDone preparing simulation directories. They can be started now (with a different script)')
























