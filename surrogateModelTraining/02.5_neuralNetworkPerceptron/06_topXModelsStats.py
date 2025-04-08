import pandas as pd
import os
import shutil
import matplotlib.pyplot as plt
import sys

try:
  saveOrShow = sys.argv[1]
except:
  saveOrShow = "show"
if saveOrShow == "save":
  pass
else:
  saveOrShow = "show"

statisticsFile = 'Stats.csv'
top = 12
topStatisticsFile = f'StatsTop{top}.csv'

if not os.path.isfile(statisticsFile):
  print(f'Can not find and open \'{statisticsFile}\'. Exit.')
  exit()
else:
  dfStatistics = pd.read_csv(statisticsFile)
  #print(f'{dfStatistics}')
  try:
    dfStatistics = dfStatistics.drop(columns=["Unnamed: 0"])
  except:
    print(f'Something went wrong with\'dfStatistics = dfStatistics.drop(columns=["Unnamed: 0"])\'.')
  else:
    #print(f'{dfStatistics}')
    pass


#pwd = os.getcwd()


## min MAPE
dfThisStatistics = dfStatistics
minMapeIDXs = []

dfTopModels = pd.DataFrame({"ratio": [],
                            "rndint": [],
                            "dataset": [],
                            "learning_rate": [],
                            "batchsize": [],
                            "epochs": [],
                            "loss": [],
                            "time": [],
                            "mape": [],
                            "r2": [],
                            "mape_test": [],
                            "r2_test": [],
                            "mape_interpolation": [],
                            "r2_interpolation": []})



gs_kw = dict(width_ratios=[1, 1], height_ratios=[1])
fig, axd = plt.subplot_mosaic([['minMAPE', 'maxR2']], 
                               gridspec_kw=gs_kw, figsize=(10.0, 5.0))
                               
thisTop = 0
print(f'MinMAPE Models:')
while True:
  idxMinMAPE = dfThisStatistics['mape'].idxmin()
  #print(f'{idxMinMAPE}')
  minMAPE = dfThisStatistics['mape'].min()
  #print(f'{minMAPE}')
  minMAPERow = dfThisStatistics.loc[idxMinMAPE]
  #print(f'Min MAPE Entry:\n{minMAPERow}\n')
  dfThisStatistics = dfThisStatistics.drop([idxMinMAPE]) 
  if minMAPERow.dataset == "Grid1296" or minMAPERow.dataset == "Grid2401":
    print(f'would have been Grid1296 or Grid2401')
    pass
  else:
    #print(f'Min MAPE Entry:\n{minMAPERow}\n')
    #print(f'Miau!')
    minMapeIDXs.append(idxMinMAPE)
    #srcModelPath = os.path.join(modelsDir, f'{minMAPERow.ratio}', f'trainedModel_{minMAPERow.ratio}_{int(minMAPERow.rndint)}_{minMAPERow.dataset}.pth')
    #print(f'{thisTop+1}: {srcModelPath} - MAPE: {minMAPERow.mape} (MAPE_all: {minMAPERow.mape_interpolation})')
    #dstModelPath = os.path.join(thisCWD, f'trainedModel_{minMAPERow.ratio}_{int(minMAPERow.rndint)}_{minMAPERow.dataset}.pth')
    #shutil.copy(srcModelPath, dstModelPath)
    dfThisTopModel = pd.DataFrame({"ratio": [minMAPERow.ratio],
                                   "rndint": [minMAPERow.rndint],
                                   "dataset": [minMAPERow.dataset],
                                   "learning_rate": [minMAPERow.learning_rate],
                                   "batchsize": [minMAPERow.batchsize],
                                   "epochs": [minMAPERow.epochs],
                                   "loss": [minMAPERow.loss],
                                   "time": [minMAPERow.time],
                                   "mape": [minMAPERow.mape],
                                   "r2": [minMAPERow.r2],
                                   "mape_test": [minMAPERow.mape_test],
                                   "r2_test": [minMAPERow.r2_test],
                                   "mape_interpolation": [minMAPERow.mape_interpolation],
                                   "r2_interpolation": [minMAPERow.r2_interpolation]})
    dfTopModels = pd.concat([dfTopModels, dfThisTopModel], ignore_index=True)
    
    axd["minMAPE"].scatter(minMAPERow.mape_test, minMAPERow.r2_test, label="", c="#332288", marker='o')#, edgecolor="#44AA99")
    
    thisTop = thisTop + 1
    if thisTop == top:
      print(f'')
      break

axd["minMAPE"].legend()
axd["minMAPE"].set_xlabel(f'MAPE', fontweight='bold')
axd["minMAPE"].set_ylabel(f'R²', fontweight='bold')
axd["minMAPE"].set_title(f'top {top} minMAPE models', fontweight='bold')

#print(f'{minMapeIDXs}')

## max R2
dfThisStatistics = dfStatistics
maxR2IDXs = []

thisTop = 0
print(f'MaxR2 Models:')
while True:
  idxMaxR2 = dfThisStatistics['r2'].idxmax()
  #print(f'{idxMaxR2}')
  #maxR2 = dfThisStatistics['r2'].max()
  #print(f'{maxR2}')
  maxR2Row = dfThisStatistics.loc[idxMaxR2]
  #print(f'Max R2 Entry:\n{maxR2Row}\n')
  dfThisStatistics = dfThisStatistics.drop([idxMaxR2])
  if maxR2Row.dataset == "Grid1296" or maxR2Row.dataset == "Grid2401":
    print(f'would have been Grid1296 or Grid2401')
    pass
  else:
    #print(f'Max R2 Entry:\n{maxR2Row}\n')
    maxR2IDXs.append(idxMaxR2)
    #srcModelPath = os.path.join(modelsDir, f'{maxR2Row.ratio}', f'trainedModel_{maxR2Row.ratio}_{int(maxR2Row.rndint)}_{maxR2Row.dataset}.pth')
    #print(f'{thisTop+1}: {srcModelPath} - R2: {maxR2Row.r2} (R2_all: {maxR2Row.r2_interpolation})')
    #dstModelPath = os.path.join(thisCWD, f'trainedModel_{maxR2Row.ratio}_{int(maxR2Row.rndint)}_{maxR2Row.dataset}.pth')
    #shutil.copy(srcModelPath, dstModelPath)
    dfThisTopModel = pd.DataFrame({"ratio": [maxR2Row.ratio],
                                   "rndint": [maxR2Row.rndint],
                                   "dataset": [maxR2Row.dataset],
                                   "learning_rate": [maxR2Row.learning_rate],
                                   "batchsize": [maxR2Row.batchsize],
                                   "epochs": [maxR2Row.epochs],
                                   "loss": [maxR2Row.loss],
                                   "time": [maxR2Row.time],
                                   "mape": [maxR2Row.mape],
                                   "r2": [maxR2Row.r2],
                                   "mape_test": [maxR2Row.mape_test],
                                   "r2_test": [maxR2Row.r2_test],
                                   "mape_interpolation": [maxR2Row.mape_interpolation],
                                   "r2_interpolation": [maxR2Row.r2_interpolation]})
    dfTopModels = pd.concat([dfTopModels, dfThisTopModel], ignore_index=True)
    
    axd["maxR2"].scatter(maxR2Row.mape_test, maxR2Row.r2_test, label="", c="#332288", marker='o')#, edgecolor="#44AA99")
    
    thisTop = thisTop + 1
    if thisTop == top:
      print(f'')
      break

axd["maxR2"].legend()
axd["maxR2"].set_xlabel(f'MAPE', fontweight='bold')
axd["maxR2"].set_ylabel(f'R²', fontweight='bold')
axd["maxR2"].set_title(f'top {top} minMAPE models', fontweight='bold')

if os.path.exists(topStatisticsFile):
  os.remove(topStatisticsFile)
  print(f'Removed existing top{top} statistics file: \'{topStatisticsFile}\'.')
dfTopModels.to_csv(topStatisticsFile)
print(f'Wrote statistics to file: \'{topStatisticsFile}\'.')
print(f'{dfTopModels}')
    
plt.tight_layout()

if saveOrShow == "show":
  plt.show()
elif saveOrShow == "save":
  plt.savefig(f'top{top}Models_MAPE-vs-R2.png', dpi=100, format='png')    
    
    
    
    
    
    
    

