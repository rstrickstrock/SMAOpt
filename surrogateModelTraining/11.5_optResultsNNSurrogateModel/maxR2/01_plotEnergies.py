import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys


runs = ['maxR2-9']

try:
  saveOrShow = sys.argv[1]
except:
  saveOrShow = "show"
if saveOrShow == "save":
  pass
else:
  saveOrShow = "show"

def calcThisAvgMAPE(targets, sims):
  """
  returns MAPE between Target and Sim RCE in %
  """
  MAPE = abs(targets - sims)/targets
  MAPE[0] = 0.0
  #print(f'{len(MAPE)}')
  MAPE = sum(MAPE)/len(MAPE)
  #print(f'{MAPE}')
  return MAPE*100

dfEnergyStats = pd.read_csv('StatsEnergies.csv')
dfEnergyStats = dfEnergyStats.drop('Unnamed: 0', axis=1)
#print(f'{dfEnergyStats}')
targetEnergies = dfEnergyStats['target'].to_numpy()
#print(f'{targetEnergies}')

prevOptEnergies = []
prevOptFile = 'prevOptRCE.txt'
with open(prevOptFile, 'r') as myFile:
  lines = myFile.readlines()
for line in lines:
  #print(f'{line}')
  prevOptEnergies.append(float(line.split(" ")[1]))
prevOptEnergies = np.array(prevOptEnergies)
#print(f'{prevOptEnergies}')
prevOptMAPE = calcThisAvgMAPE(targetEnergies, prevOptEnergies)
#print(f'{prevOptMAPE}')


for run in runs:
  runEnergies = dfEnergyStats[f'{run}'].to_numpy()
  #print(f'{runEnergies}')
  thisAvgMAPE = calcThisAvgMAPE(targetEnergies, runEnergies)
  plt.figure()
  plt.plot(targetEnergies, targetEnergies, '-', color='#000000')
  plt.plot(targetEnergies, prevOptEnergies, 'x', label=f'PrevOpt RCE (avg. MAPE: {prevOptMAPE:.2f})', color='#ff7f00', markersize=7.5)
  plt.plot(targetEnergies, runEnergies, 'x', label=f'SMAOpt RCE (avg. MAPE: {thisAvgMAPE:.2f})', color='#377eb8', markersize=7.5)
  
  plt.xlabel("Target Rel. Conf. Energy (RCE) [kcal/mol]", weight='bold')
  plt.ylabel("Reproduced Rel. Conf. Energy (RCE) [kcal/mol]", weight='bold')
  plt.legend()
  plt.tight_layout()
  
  if saveOrShow == "save":
    plt.savefig(f'CalcEnergies-vs-Targets_{run}.png', dpi=100, format='png')
  
if saveOrShow == "show":
  plt.show()
