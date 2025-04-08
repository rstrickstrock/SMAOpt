import os
import pandas as pd
import shutil

experiment_directory = 'experiments/'
experiment_directory = os.fsencode(experiment_directory)
#print(f'{experiment_directory}')

props = ['SigC', 'SigH', 'EpsC', 'EpsH', 'density', 'density_err']
for i in range(1,97):
  props.append(f'conf_{i}')
data = {'#': props}

df = pd.DataFrame(data)
#print(f'{df}')

cwd = os.getcwd()
logfile = "LOG_gather_results.log"
logfile = os.path.join(cwd, logfile)

if os.path.isfile(logfile):
  os.remove(logfile)

##############
#### functions
def get_density(density_dir):
  #print(f'{density_dir}')
  thisdir = os.fsencode(density_dir)

  ## get all slurmfiles
  slurmfiles = []
  for file in os.listdir(thisdir):
    thisfile = os.fsdecode(file)
    #print(f'{thisfile}')
    if thisfile.startswith('slurm-'):
      slurmfiles.append(thisfile)
  #print(f'{slurmfiles}')
  ## get latest slurmfile
  slurmfile = "slurm-0.out"
  for filename in slurmfiles:
    if float(slurmfile.split(".")[0].split("-")[1]) < float(filename.split(".")[0].split("-")[1]):
      slurmfile = filename
  #print(f'{slurmfile}')
  slurmfile = os.path.join(density_dir, slurmfile)
  #print(f'{slurmfile}')
  
  ## read density from slurmfile
  if os.path.isfile(slurmfile):
    f = open(slurmfile, 'r')
    lines = f.readlines()
    f.close()
    if lines[-1].startswith("Density"):
      densityline = lines[-1]
    else:
      print(f'(Problem: lines[-1] -- {lines[-1]} -- does not start with DENSITY.')
    #print(f'DENSITYLINE {densityline}')
    densityline = densityline.split(" ")
    #print(f'DENSITYLINE {densityline}')
    densityinfo = []
    for item in densityline:
      if item.startswith("Density"):
        pass
      elif len(item) <= 1:
        pass
      else:
        densityinfo.append(item)
      #print(f'DENSITYINFO {densityinfo}')
    density = densityinfo[0]
    density_err = densityinfo[1]
#    density_rmsd = densityinfo[2]
#    density_totdrift = densityinfo[3]
#    density_unit = densityinfo[4]
    #print(f'DENSITY     {density}')
    #print(f'DENSITYERR  {density_err}')

    return [density, density_err]


def get_rel_energies(energy_file, experiment, logfile):
  if os.path.isfile(energy_file):
    pass
  else:
    print(f'(Problem: energyfile -- {energy_file} -- does not exists.')
    exit()

  f = open(energy_file, 'r')
  lines = f.readlines()
  f.close()
  energies = []
  i = 1
  for line in lines:
    molec_number = int(line.split(" ")[0].split("-")[1])
    #print(f'{molec_number}')
    if i == molec_number:
      energies.append(float(line.split(" ")[1]))
    else:
      energies.append(float(-10.0))
      write_to_log(logfile, f'In experiment {experiment} inserted RCE of \"-10.0\" for molecule {i}, because of missing result file.')
  #print(f'ENERGIES    {energies}')
    i = i + 1
  while i <= 96:
    energies.append(float(-10.0))
    write_to_log(logfile, f'In experiment {experiment} inserted RCE of \"-10.0\" for molecule {i}, because of missing result file.')
    i = i + 1

  return energies


def write_to_log(logfile, msg):
  with open(logfile, 'a') as myfile:
    myfile.write(f'{msg}\n')

####
##############


i = 1
print(f'Collecting results ..')
write_to_log(logfile, "Collecting results ..")

experiments = os.listdir(experiment_directory)
#print(f'{len(experiments)}')
total_number_of_experiments = len(experiments)

for experiment in experiments:
  this_dictonary = [] # store values here and insert into dataframe at the end

  this_experiment_dir = os.fsdecode(experiment)
  #print(f'{this_experiment_dir}')

  parameters = this_experiment_dir.split("_")
  #print(f'{parameters}')
  SigC = parameters[0]
  SigH = parameters[1]
  EpsC = parameters[2]
  EpsH = parameters[3]
  this_dictonary.append(SigC) # add value for property 'SigC'
  this_dictonary.append(SigH) # add value for property 'SigH'
  this_dictonary.append(EpsC) # add value for property 'EpsC'
  this_dictonary.append(EpsH) # add value for property 'EpsH'
  #print(f'{this_dictonary}')

  density_dir = os.path.join(os.fsdecode(experiment_directory), this_experiment_dir, 'density/')
  #print(f'{density_dir}')
  [this_density, this_density_err] = get_density(density_dir)
  #print(f'{this_density}')
  #print(f'{this_density_err}')
  try:
    this_dictonary.append(float(this_density))
  except:
    this_dictonary.append(float(0.0))
    write_to_log(logfile, f'for experiment {this_experiment_dir} added \"0.0\" for density.')

  try:
    this_dictonary.append(this_density_err)
  except:
    this_dictonary.append(float(100.0))
    write_to_log(logfile, f'for experiment {this_experiment_dir} added \"100.0\" for density error.')

  energy_dir = os.path.join(os.fsdecode(experiment_directory), this_experiment_dir, 'energies/', 'output/')
  #print(f'{energy_dir}')
  energy_file = os.path.join(energy_dir, "Energy.rel.extrm.txt")
  #print(f'{energy_file}')
  energies = get_rel_energies(energy_file, this_experiment_dir, logfile)
  #print(f'{energies}')
  for energy in energies:
    this_dictonary.append(energy)

  try:
    df.insert(len(df.columns), f'{i}', this_dictonary, True)
  except:
    print(f'{this_experiment_dir}')
    #print(f'{this_density}')
    #print(f'{this_density_err}')
    print(f'{len(energies)}')
    exit()
  #print(f'{df}')
  print(f'\r .. {i}/{total_number_of_experiments}', end='')
  i = i+1
  #break
print(f'', flush=True)

result_CSV_file = 'RESULTS_experiments.csv'
print(f'\nWriting results to {result_CSV_file} ..')
df.to_csv(result_CSV_file)
print(f'done.\n')



















