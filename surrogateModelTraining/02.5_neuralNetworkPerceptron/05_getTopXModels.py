import pandas as pd
import os
import shutil


statisticsFile = 'Stats.csv'
modelsDir = 'trainedModels'  
bestModelsDir = 'bestTrainedModels'
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


pwd = os.getcwd()
cwd = os.path.join(pwd, bestModelsDir)
#print(f'{cwd}')
if os.path.exists(cwd):
  shutil.rmtree(cwd)
os.mkdir(cwd)


## min MAPE
dfThisStatistics = dfStatistics
minMapeIDXs = []
thisBestModelsDir = 'minMAPE'

thisCWD = os.path.join(cwd, thisBestModelsDir)
os.mkdir(thisCWD)

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


thisTop = 0
print(f'MinMAPE Models:')
while True:
  idxMinMAPE = dfThisStatistics['mape'].idxmin()
  print(f'{idxMinMAPE}')
  minMAPE = dfThisStatistics['mape'].min()
  #print(f'{minMAPE}')
  minMAPERow = dfThisStatistics.loc[idxMinMAPE]
  #print(f'Min MAPE Entry:\n{minMAPERow}\n')
  dfThisStatistics = dfThisStatistics.drop([idxMinMAPE]) 
  if minMAPERow.dataset == "Grid1296" or minMAPERow.dataset == "Grid2401":
    pass
  else:
    #print(f'Min MAPE Entry:\n{minMAPERow}\n')
    #print(f'Miau!')
    minMapeIDXs.append(idxMinMAPE)
    srcModelPath = os.path.join(modelsDir, f'{minMAPERow.ratio}', f'trainedModel_{minMAPERow.ratio}_{int(minMAPERow.rndint)}_{minMAPERow.dataset}.pth')
    print(f'{thisTop+1}: {srcModelPath} - MAPE: {minMAPERow.mape} (MAPE_all: {minMAPERow.mape_interpolation})')
    dstModelPath = os.path.join(thisCWD, f'trainedModel_{minMAPERow.ratio}_{int(minMAPERow.rndint)}_{minMAPERow.dataset}.pth')
    shutil.copy(srcModelPath, dstModelPath)
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
    thisTop = thisTop + 1
    if thisTop == top:
      print(f'')
      break

#print(f'{minMapeIDXs}')

## max R2
dfThisStatistics = dfStatistics
maxR2IDXs = []
thisBestModelsDir = 'maxR2'

thisCWD = os.path.join(cwd, thisBestModelsDir)
os.mkdir(thisCWD)

thisTop = 0
print(f'MaxR2 Models:')
while True:
  idxMaxR2 = dfThisStatistics['r2'].idxmax()
  print(f'{idxMaxR2}')
  #maxR2 = dfThisStatistics['r2'].max()
  #print(f'{maxR2}')
  maxR2Row = dfThisStatistics.loc[idxMaxR2]
  #print(f'Max R2 Entry:\n{maxR2Row}\n')
  dfThisStatistics = dfThisStatistics.drop([idxMaxR2])
  if maxR2Row.dataset == "Grid1296" or maxR2Row.dataset == "Grid2401":
    pass
  else:
    #print(f'Max R2 Entry:\n{maxR2Row}\n')
    maxR2IDXs.append(idxMaxR2)
    srcModelPath = os.path.join(modelsDir, f'{maxR2Row.ratio}', f'trainedModel_{maxR2Row.ratio}_{int(maxR2Row.rndint)}_{maxR2Row.dataset}.pth')
    print(f'{thisTop+1}: {srcModelPath} - R2: {maxR2Row.r2} (R2_all: {maxR2Row.r2_interpolation})')
    dstModelPath = os.path.join(thisCWD, f'trainedModel_{maxR2Row.ratio}_{int(maxR2Row.rndint)}_{maxR2Row.dataset}.pth')
    shutil.copy(srcModelPath, dstModelPath)
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
    thisTop = thisTop + 1
    if thisTop == top:
      print(f'')
      break


if os.path.exists(topStatisticsFile):
  os.remove(topStatisticsFile)
  print(f'Removed existing top{top} statistics file: \'{topStatisticsFile}\'.')
dfTopModels.to_csv(topStatisticsFile)
print(f'Wrote statistics to file: \'{topStatisticsFile}\'.')
print(f'{dfTopModels}')
    
    
    
    
    
    
    
    
    

