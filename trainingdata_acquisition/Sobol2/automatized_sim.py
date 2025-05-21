import subprocess
import time
import os
from glob import glob
import threading

time_check_intervall = 60 #seconds

max_sims = 2
idx = 0

sim_path = '/home/rstric2s/current_sim/Paper_Octane-3_NN-predictor/NN_Model_Training-Database/sobol_sampling_data/experiments/*'
## get all directories
sim_dirs = glob(sim_path)
#print(f'sim_dirs:{sim_dirs}')

def run_sim_chain(commands, cwd):
  os.chdir(cwd)
  print(f'Changed cwd to: {cwd}')
  for command in commands:
    ## start simulation     
    simulation = subprocess.Popen(command, stdout=subprocess.PIPE)
    print(f'started {command[1]}')
    print(f'in cwd: {os.getcwd()}')
    ## get std out to determine job ID
    simulation_stdout = simulation.stdout.read()
    batch_job_id = [int(s) for s in simulation_stdout.split() if s.isdigit()]
    batch_job_id = batch_job_id[0]

    # check if batch scrip terminated and wait if not
    while 1:
      if simulation.poll() == 0:
        break
      else:
        time.sleep(1)
    
    # wait for job to finish
    while 1:
      check_job_status = subprocess.Popen(['squeue', '-j', str(batch_job_id)], stdout=subprocess.PIPE)
      check_job_status = check_job_status.stdout.read()
      if str(check_job_status).find(str(batch_job_id)) > 0:
        ## job is still running, check again in time_check_intervall seconds
        time.sleep(time_check_intervall)
      else:
        ## job has finished
        break


for i in range(max_sims*idx, max_sims*(idx+1)):
  #for sim_dir in sim_dirs:
  try:
    d = sim_dirs[i]
  except IndexError:
    print(f'No more sim_dirs. Finished? Exit!')
    exit()
    
  sim_dir = os.path.join(d, 'density')
  print(f'sim_dir: {sim_dir}')
  commands =[['sbatch', f'{sim_dir}/01_batch_slurm_emin.sh'],
           ['sbatch', f'{sim_dir}/02_batch_slurm_nvt.sh'],
           ['sbatch', f'{sim_dir}/03_batch_slurm_npt.sh'],
           ['sbatch', f'{sim_dir}/04_batch_slurm_eval_density.sh'],
           ['sbatch', f'{sim_dir}/04_batch_slurm_prod.sh']]
  
  #for command in commands:
  #  print(f'{command}')   
  x = threading.Thread(target=run_sim_chain, args=(commands, sim_dir,))
  x.start()
  time.sleep(5)
    
