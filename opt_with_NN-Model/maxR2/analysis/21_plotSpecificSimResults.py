import os
#import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import glob
from natsort import natsorted

pwd = "/home/rstric2s/current_sim/Paper_Octane-3_NN-predictor/opt_with_NN-Model/maxR2"
runs = [2, 4, 6, 8, 9]
#runs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
thisDir = os.path.basename(pwd)

try:
  saveOrShow = sys.argv[1]
except:
  saveOrShow = "show"
if saveOrShow == "save":
  pass
else:
  saveOrShow = "show"

for run in runs:
  thisRunDir = os.path.join(pwd, f'{thisDir}-{run}')
  #print(f'{thisRunDir}')
  thisPhysPropDir = os.path.join(thisRunDir, 'PhysProp')
  thisQMMMDir = os.path.join(thisRunDir, 'QMMM')
  thisDensityDir = natsorted(glob.glob(os.path.join(thisPhysPropDir,'g.*.0')))[-1]
  #print(f'{thisDensityDir}')
  thisEnergyDir = natsorted(glob.glob(os.path.join(thisQMMMDir,'g.*.0')))[-1]
  #print(f'{thisEnergyDir}')
  thisDensityPredictionFile = natsorted(glob.glob(os.path.join(thisDensityDir, 'slurm-*')))[-1]
  #print(f'{thisDensityPredictionFile}')
  
  with open(thisDensityPredictionFile, 'r') as f:
    lines = f.readlines()
  thisDensityPrediction = None
  for l in range(0, len(lines)):
    #print(f'{lines[l]}')
    if "this_prediction" in lines[l]:
      thisDensityPrediction = float(lines[l+1])
      break
  #print(f'{thisDensityPrediction}')
  
  thisTargetEnergyFile = os.path.join(thisEnergyDir, 'bindir', '00_qm_opt', 'target.txt')
  #print(f'{thisTargetEnergyFile}')
  thisSimEnergyFile = os.path.join(thisEnergyDir, 'output', 'Energy.rel.extrm.txt')
  #print(f'{thisSimEnergyFile}')
  
  with open(thisTargetEnergyFile, 'r') as f:
    lines = f.readlines()
  thisTargetEnergies = []
  for line in lines:
    #print(f'{line}')
    if len(line) > 0:
      thisTargetEnergies.append(float(line))
  thisTargetEnergies = np.array(thisTargetEnergies)
  #print(f'{thisTargetEnergies}')
  
  with open(thisSimEnergyFile, 'r') as f:
    lines = f.readlines()
  thisSimEnergies = []
  for line in lines:
    #print(f'{line}')
    if len(line) > 0:
      thisSimEnergies.append(float(line.split(" ")[1]))
  thisSimEnergies = np.array(thisSimEnergies)
  #print(f'{thisSimEnergies}')
  
  #print(f'{len(thisTargetEnergies)}')
  thisAvgMAPE = 0.0
  for i in range(0,len(thisTargetEnergies)):
    #print(f'{thisTargetEnergies[i]}')
    #print(f'{thisSimEnergies[i]}')
    diff = thisTargetEnergies[i] - thisSimEnergies[i]
    #print(f'{diff}')
    if thisTargetEnergies[i] == 0:
      reldiff = 0
    else:
      reldiff = diff/thisTargetEnergies[i]
    sqreldiff = np.square(reldiff)
    #print(f'{sqreldiff}')
    sqrtsqreldiff = np.sqrt(sqreldiff)
    #print(f'{sqrtsqreldiff}')
    #print(f'')
    thisAvgMAPE = thisAvgMAPE + sqrtsqreldiff
  thisAvgMAPE = thisAvgMAPE/len(thisTargetEnergies)
  #print(f'{thisAvgMAPE}')

  plt.figure()
  plt.plot(thisTargetEnergies, thisTargetEnergies, '-', color='#000000')
  plt.plot(thisTargetEnergies, thisSimEnergies, 'x', label=f'{thisDir}-{run}, avg. MAPE: {thisAvgMAPE}, DensityPred: {thisDensityPrediction:.2f}')
  
  plt.xlabel("target rel. conf. energy [kcal/mol]")
  plt.ylabel("calculated rel. conf. energy [kcal/mol]")
  plt.legend()
  plt.tight_layout()
  
  if saveOrShow == "save":
    plt.savefig(f'CalcEnergies-vs-Targets_{thisDir}-{run}.png', dpi=300, format='png')
  
if saveOrShow == "show":
  plt.show()









