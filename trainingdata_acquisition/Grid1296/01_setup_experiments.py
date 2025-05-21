import os
import shutil
#import pandas as pd

### initial gridsearch
#start_parameters = [0.2000, 0.1820, 0.6570, 0.0800]
boundaries = 0.75 # = +/- 25%
number_of_parameter_variations = 7

### for intermediate points
start_parameters = [0.0750, 0.0683, 0.2465, 0.0300]
end_parameters = [0.3250, 0.2958, 1.0675, 0.1300]

experiments_directory = "experiments"

current_working_directory = os.getcwd()
cwd = os.path.join(current_working_directory, experiments_directory)

##############
#### functions

def create_parameter_permutations(parameters, boundaries, number_of_parameter_variations):
  """
  input: parameter vector parameters = [p1, p2, p3, ..], multiplicator for min/max value boundaries = 0.25 for +/- 25, Intervallsize for the parameter to be divided in.
  output parameter vector with permutation of all possible parameter sets consisting of min/mid/max values
  """
  max_parameters = []
  min_parameters = []

  for par in parameters:
    max_parameters.append(format(round(par + par*boundaries, 4), '.4f'))
    min_parameters.append(format(round(par - par*boundaries, 4), '.4f'))

  #print(f'max_parameters: {max_parameters}')
  #print(f'min_parameters: {min_parameters}')

  n = len(parameters)
  #print(f'n = {n}') # number of parameters
  ## get increments for every parameter:
  parameter_increments = []
  for par_idx in range(0, n):
    par_increment = round((float(max_parameters[par_idx]) - float(min_parameters[par_idx]))/(float(number_of_parameter_variations)-1), 4)
    parameter_increments.append(par_increment)
    #print(f'{par_increment}')

  list_of_parameters = []
  for i in range(0, n):
    list_of_parameters.append([min_parameters[i]])
  #print(f'{list_of_parameters}')

  for i in range(1, number_of_parameter_variations):
    for j in range(0, n):
      this_parameter = round(float(min_parameters[j]) + float(min_parameters[j])*i, 4)
      list_of_parameters[j].append(this_parameter)

  #print(f'list_of_parameters = {list_of_parameters}') 
  ## list_of_parameters_contains: [[par1_min, ..., par1_max], [par2_min, ..., par2_max], ..]

  permutations = [[i, j, k, l] for i in list_of_parameters[0] for j in list_of_parameters[1] for k in list_of_parameters[2] for l in list_of_parameters[3]]
  #print(f'permutations: \n{permutations}')
  #print(f'number of permuations: {len(permutations)}')

  return permutations



def create_intermediate_permuations(start_parameters, end_parameters, number_of_parameter_variations_intermediate):
  """
  input: start parameter vector start_parameters = [p1, p2, p3, ..], end parameter vector end_parameters = [p1, p2, p3, ..], and number of parameter varations for a single parameter (e.g. "3" means that that every p1, p2, .. will be assigned 3 values ranging from p1_start to p1_end with equi distant steplengths).
  output parameter vector with permutation of all possible parameter sets consisting of min/mid/max values
  """
  max_parameters = []
  min_parameters = []

  for par in start_parameters:
    min_parameters.append(format(round(par, 4), '.4f'))

  for par in end_parameters:
    max_parameters.append(format(round(par, 4), '.4f'))

  #print(f'max_parameters: {max_parameters}')
  #print(f'min_parameters: {min_parameters}')


  n = len(max_parameters)
  #print(f'n = {n}') # number of parameters
  ## get increments for every parameter:
  parameter_increments = []
  for par_idx in range(0, n):
    par_increment = round((float(max_parameters[par_idx]) - float(min_parameters[par_idx]))/(float(number_of_parameter_variations_intermediate)-1), 4)
    parameter_increments.append(par_increment)
    #print(f'{par_increment}')

  list_of_parameters = []
  for i in range(0, n):
    list_of_parameters.append([min_parameters[i]])
  #print(f'{list_of_parameters}')

  for i in range(1, number_of_parameter_variations_intermediate):
    for j in range(0, n):
      this_parameter = round(float(min_parameters[j]) + float(parameter_increments[j])*i, 4)
      list_of_parameters[j].append(this_parameter)

  #print(f'list_of_parameters = {list_of_parameters}') 
  ## list_of_parameters_contains: [[par1_min, ..., par1_max], [par2_min, ..., par2_max], ..]

  permutations = [[i, j, k, l] for i in list_of_parameters[0] for j in list_of_parameters[1] for k in list_of_parameters[2] for l in list_of_parameters[3]]
  #print(f'permutations: \n{permutations}')
  #print(f'number of permuations: {len(permutations)}')

  return permutations



def create_simdir(simdir):
  #print(f'simdir: {simdir}')
  try:
    os.mkdir(simdir)
  except:
    print(f'Could not create simdir ({simdir}). Check this. Exit setup.')
###    exit()



def parameters_GMX2AMB(parameters):
  """
  converts parameters with gromacs units to amber units
  expects a parameter vector p=[sigma1, sigma2, epsilon1, epsilon2]
  """
  if not len(parameters) == 4:
    print(f'ERROR: Parameters {parameters} must be of size 4 containing: parameters=[sigma1, sigma2, epsilon1, epsilon2]. Exit Setup.')
    exit()

  sigma1_gmx = parameters[0]
  #print(f'sigma1_gmx: {sigma1_gmx}')
  #print(type(sigma1_gmx))
  sigma2_gmx = parameters[1]
  #print(f'sigma2_gmx: {sigma2_gmx}')
  epsilon1_gmx = parameters[2]
  #print(f'epsilon1_gmx: {epsilon1_gmx}')
  epsilon2_gmx = parameters[3]
  #print(f'epsilon2_gmx: {epsilon2_gmx}')

  sigma1_amb = round((float(sigma1_gmx)*10*2**(1.0/6.0))/2, 8)
  sigma2_amb = round((float(sigma2_gmx)*10*2**(1.0/6.0))/2, 8)
  epsilon1_amb = round(float(epsilon1_gmx)/4.1868, 8)
  epsilon2_amb = round(float(epsilon2_gmx)/4.1868, 8)

  #print(f'sigma1: gmx={sigma1_gmx}, amb={sigma1_amb}')
  #print(f'sigma2: gmx={sigma2_gmx}, amb={sigma2_amb}')
  #print(f'epsilon1: gmx={epsilon1_gmx}, amb={epsilon1_amb}')
  #print(f'epsilon2: gmx={epsilon2_gmx}, amb={epsilon2_amb}')

  parameters_amb = [sigma1_amb, sigma2_amb, epsilon1_amb, epsilon2_amb]

  return parameters_amb



def make_density_simdir(current_working_directory, simdir, parameters):
  density_dir = os.path.join(current_working_directory, "density")
  simdir = os.path.join(simdir, "density")
  os.mkdir(simdir)
  #print(f'density_dir: {density_dir}')
  #print(f'simdir: {simdir}')

  ## copy files ##
  ## force-field.ff
  shutil.copytree(os.path.join(density_dir, "force-field.ff"),os.path.join(simdir, "force-field.ff"))
  ## topol.top
  shutil.copy(os.path.join(density_dir, "equilibrated", "topol.top"), simdir)
  ## equilibrated.cpt
  shutil.copy(os.path.join(density_dir, "equilibrated", "equilibrated.cpt"), simdir)
  ## equilibrated.gro
  shutil.copy(os.path.join(density_dir, "equilibrated", "equilibrated.gro"), simdir)
  ## prod.mdp
  shutil.copy(os.path.join(density_dir, "prod.mdp"), simdir)

  ## batch_slurm_prod.sh
  shutil.copy(os.path.join(density_dir, "batch_slurm_prod.sh"), simdir)
  ## batch_slurm_eval_density.sh
  shutil.copy(os.path.join(density_dir, "batch_slurm_eval_density.sh"), simdir)

  ## change parameters in topol.top
  topology_file = os.path.join(simdir, "topol.top")
  #print(f'topology_file: {topology_file}')
  tmp_topology_file = os.path.join(simdir, "topol.tmp")

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


def make_energy_simdir(current_working_directory, simdir, parameters):
  energy_dir = os.path.join(current_working_directory, "energies")
  simdir = os.path.join(simdir, "energies")
#  os.mkdir(simdir)
  #print(f'density_dir: {energy_dir}')
  #print(f'simdir: {simdir}')

  ## convert parameters from Gromacs units to Amber units
  #parameters = [0.127668747165553, 0.25415906133572486, 0.655268898590931, 0.0772235439912527] #test parameterset
  #parameters = [0.1500, 0.1365, 0.4928, 0.0600] #test parameterset
  parameters = parameters_GMX2AMB(parameters)

  ## copy files ##
  ## bindir/
  shutil.copytree(os.path.join(energy_dir, "bindir"),os.path.join(simdir, "bindir"))
  ## ExTrM.template.dat
  shutil.copy(os.path.join(energy_dir, "ExTrM.template.dat"), simdir)
  ## replace_placeholders.sh
  shutil.copy(os.path.join(energy_dir, "replace_placeholders.sh"), simdir)
  ## molec.extrm.bcc.mol2
  shutil.copy(os.path.join(energy_dir, "molec.extrm.bcc.mol2"), simdir)
  ## leaprc.extrm
  shutil.copy(os.path.join(energy_dir, "leaprc.extrm"), simdir)
  ## leaprc.extrm.w2p
  shutil.copy(os.path.join(energy_dir, "leaprc.extrm.w2p"), simdir)
  ## grow_sander_ff_opt.py
  shutil.copy(os.path.join(energy_dir, "grow_sander_ff_opt.py"), simdir)
  ## run_mm.sh
  shutil.copy(os.path.join(energy_dir, "run_mm.sh"), simdir)

  ## batch_slurm_RCE.sh
  shutil.copy(os.path.join(energy_dir, "batch_slurm_RCE.sh"), simdir)
  ## batch_slurm_eval_RCE.sh
  shutil.copy(os.path.join(energy_dir, "batch_slurm_eval_RCE.sh"), simdir)
  ## qmmm_eval.py
  shutil.copy(os.path.join(energy_dir, "qmmm_eval.py"), simdir)

  ## change parameters in run_mm.sh
  run_file = os.path.join(simdir, "run_mm.sh")
  #print(f'topology_file: {topology_file}')
  tmp_run_file = os.path.join(simdir, "run_mm.tmp")

  with open(run_file, "rt") as fin:
    with open(tmp_run_file, "wt") as fout:
      for line in fin:
        fout.write(line.replace('s1=SIGMA1 #A',f's1={parameters[0]} #A'))

  with open(tmp_run_file, "rt") as fin:
    with open(run_file, "wt") as fout:
      for line in fin:
        fout.write(line.replace('s2=SIGMA2 #A',f's2={parameters[1]} #A'))

  with open(run_file, "rt") as fin:
    with open(tmp_run_file, "wt") as fout:
      for line in fin:
        fout.write(line.replace('e1=EPSILON1 #K',f'e1={parameters[2]} #K'))

  with open(tmp_run_file, "rt") as fin:
    with open(run_file, "wt") as fout:
      for line in fin:
        fout.write(line.replace('e2=EPSILON2 #K',f'e2={parameters[2]} #K'))

  os.remove(tmp_run_file)
#### end
##############


## check if directory exists. If true: exit to prevent data loss
if os.path.exists(cwd):
  print(f'Directory {cwd} already exists. Exit setup.')
  #shutil.rmtree(cwd)
  exit()
else:
  #print(f'does not exist. create.')
  os.mkdir(cwd)

## get all permuations based on input parameters

#permutations = create_parameter_permutations(start_parameters, boundaries, number_of_parameter_variations)
#print(f'{permutations}')
#print(f'{len(permutations)}')

number_of_parameter_variations_intermediate = number_of_parameter_variations - 1
permutations = create_intermediate_permuations(start_parameters, end_parameters, number_of_parameter_variations_intermediate)
#print(f'{permutations}')
#print(f'{len(permutations)}')

## for every permutaion create a density and energy simulation directory
i = 1
for permutation in permutations:
  #print(f'permuation: {permutation}')
  dirname = ""
  for value in permutation:
    dirname = dirname + str(value) + "_"
  dirname = dirname[:-1]
  #print(f'dirname = {dirname}')

  ## create directory for simulations
  simdir = os.path.join(cwd, dirname)
  create_simdir(simdir)

  make_density_simdir(current_working_directory, simdir, permutation)
#  make_energy_simdir(current_working_directory, simdir, permutation)
  #print(f'Prepared permuation folder {i}.')
  i = i + 1

print(f'\nDone preparing simulation directories. They can be started now (with a different script')
























