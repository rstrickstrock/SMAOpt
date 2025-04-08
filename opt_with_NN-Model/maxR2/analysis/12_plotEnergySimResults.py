import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

pwd = "/home/rstric2s/current_sim/Paper_Octane-3_NN-predictor/opt_with_NN-Model/maxR2"
thisDir = os.path.basename(pwd)

statisticsFileName = os.path.join(pwd, "StatsEnergies.csv")
avgRMSEFileName = os.path.join(pwd, "AvgRMSEEnergies.csv")

try:
  saveOrShow = sys.argv[1]
except:
  saveOrShow = "show"
if saveOrShow == "save":
  pass
else:
  saveOrShow = "show"

dfStats = pd.read_csv(statisticsFileName)
dfStats = dfStats.drop(dfStats.columns[0], axis=1)
#print(f'{dfStats}')
dfAvgRMSEs = pd.read_csv(avgRMSEFileName)
dfAvgRMSEs = dfAvgRMSEs.drop(dfAvgRMSEs.columns[0], axis=1)
#print(f'{dfAvgRMSEs}')

targets = dfStats["target"].to_numpy()
#print(f'{targets}')
sortIDX = targets.argsort()
#print(f'{sortIDX}')
sortedTargets = []
for idx in sortIDX:
  sortedTargets.append(targets[idx])
#print(f'{sortedTargets}')

plt.plot(sortedTargets, sortedTargets, '-', color='#000000')
#1plt.plot(targets, targets, '-', color='#000000')
#plt.show()

for i in range(0, 12): #hardcoded :(
  thisRun = f'{thisDir}-{i}'
  thisEnergies = dfStats[thisRun].to_numpy()
  thisSortedEnergies = []
  for idx in sortIDX:
    thisSortedEnergies.append(thisEnergies[idx])
  
  thisAvgRMSE = np.round(float(dfAvgRMSEs.loc[i].to_numpy()[0]), 4)
  plt.plot(sortedTargets,thisSortedEnergies, 'x', label=f'{thisDir}-{i}, avg. RMSE: {thisAvgRMSE}')
  #1plt.plot(targets,thisEnergies, 'x', label=f'{thisDir}-{i}, avg. RMSE: {thisAvgRMSE}')

plt.legend()  
plt.xlabel("target rel. conf. energy [kcal/mol]")
plt.ylabel("calculated rel. conf. energy [kcal/mol]")
plt.tight_layout()

if saveOrShow == "save":
  plt.savefig(f'optedEnergies-vs-Targets_{thisDir}.png', dpi=300, format='png')
  #break
if saveOrShow == "show":
  plt.show()

