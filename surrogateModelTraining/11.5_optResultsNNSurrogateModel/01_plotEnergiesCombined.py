import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys


#runs = ['minMAPE-10', 'maxR2-9']
runs = ['maxR2-9', 'minMAPE-10']
colors = ['#377eb8', '#4daf4a']
figDPI = 300

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

dfEnergyStatsMaxR2 = pd.read_csv('maxR2/StatsEnergies.csv')
dfEnergyStatsMaxR2 = dfEnergyStatsMaxR2.drop('Unnamed: 0', axis=1)
#print(f'{dfEnergyStatsMaxR2}')
targetEnergies = dfEnergyStatsMaxR2['target'].to_numpy()
#print(f'{targetEnergies}')
dfEnergyStatsMinMAPE = pd.read_csv('minMAPE/StatsEnergies.csv')
dfEnergyStatsMinMAPE = dfEnergyStatsMinMAPE.drop('Unnamed: 0', axis=1)
#print(f'{dfEnergyStatsMinMAPE}')

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

plt.plot(targetEnergies, targetEnergies, '-', color='#000000')
plt.plot(targetEnergies, prevOptEnergies, 'x', label=f'PrevOpt RCE (avg. MAPE: 9.75)', color='#ff7f00', markersize=7.5)

for run in range(0, len(runs)):
  if runs[run].startswith('max'):
    dfEnergyStats = dfEnergyStatsMaxR2
  if runs[run].startswith('min'):
    dfEnergyStats = dfEnergyStatsMinMAPE
    
  runEnergies = dfEnergyStats[f'{runs[run]}'].to_numpy()
  #print(f'{runEnergies}')
  thisAvgMAPE = calcThisAvgMAPE(targetEnergies, runEnergies)

  plt.plot(targetEnergies, runEnergies, 'x', label=f'SMAOpt-{run+1} RCE (avg. MAPE: {thisAvgMAPE:.2f})', color=colors[run], markersize=7.5)

  
plt.xlabel("Target Rel. Conf. Energy (RCE) [kcal/mol]", weight='bold')
plt.ylabel("Reproduced Rel. Conf. Energy (RCE) [kcal/mol]", weight='bold')
plt.legend()
plt.tight_layout()
  
if saveOrShow == "save":
  plt.savefig(f'CalcEnergies-vs-Targets_AllInOne.png', dpi=figDPI, format='png')
if saveOrShow == "show":
  plt.show()
