import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_percentage_error as skmape

import pandas as pd
import os
import time
import shutil

n_epochs = 200
learning_rate = 0.001
architecture = f'4-128-64-32-1'
hiddenLayer = 3

trainingDatasetNames = ["Grid1296", "Grid2401", "Sobol1", "Sobol2"]
rndInts = [593, 634]
trainRatios = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]
testmode = True

class thisModel3(nn.Module):
  def __init__(self, architecture):
    super().__init__()
    try:
      inputdim = int(architecture.split('-')[0])
    except:
      print(f'Can not get input dim from {architecture}')
    try:
      firstlayerdim = int(architecture.split('-')[1])
    except:
      print(f'Can not get firstlayer dim from {architecture}')
    try:
      secondlayerdim = int(architecture.split('-')[2])
    except:
      print(f'Can not get secondlayer dim from {architecture}')
    try:
      thirdlayerdim = int(architecture.split('-')[3])
    except:
      print(f'Can not get thirdlayer dim from {architecture}')
    try:
      outputdim = int(architecture.split('-')[4])
    except:
      print(f'Can not get outputs dim from {architecture}')
      
    self.hidden1 = nn.Linear(inputdim, firstlayerdim)
    self.act1 = nn.LeakyReLU()
    self.hidden2 = nn.Linear(firstlayerdim, secondlayerdim)
    self.act2 = nn.LeakyReLU()
    self.hidden3 = nn.Linear(secondlayerdim, thirdlayerdim)
    self.act3 = nn.LeakyReLU()
    self.output = nn.Linear(thirdlayerdim, outputdim)
    self.act_output = nn.LeakyReLU()

  def forward(self, x):
    x = self.act1(self.hidden1(x))
    x = self.act2(self.hidden2(x))
    x = self.act3(self.hidden3(x))
    x = self.act_output(self.output(x))
    return x

pwd = os.getcwd()
cwd = os.path.join(pwd, "trainedModels")
#print(f'{cwd}')
if os.path.exists(cwd):
  if testmode:
    #shutil.rmtree(cwd)
    pass
  else:
    print(f'\nPATH \'{cwd}\' already exists. \n\nExiting without starting or changing anything.\n')
    exit()
else:
  os.mkdir(cwd)


datasetGrid1296 = pd.read_csv('CLEANED_gridsearch_1296.csv')
datasetGrid1296 = datasetGrid1296.drop(datasetGrid1296.columns[0], axis=1)
XGrid1296 = datasetGrid1296.drop('density', axis=1)
YGrid1296 = datasetGrid1296['density']

datasetGrid2401 = pd.read_csv('CLEANED_gridsearch_2401.csv')
datasetGrid2401 = datasetGrid2401.drop(datasetGrid2401.columns[0], axis=1)
XGrid2401 = datasetGrid2401.drop('density', axis=1)
YGrid2401 = datasetGrid2401['density']

datasetSobol1 = pd.read_csv('CLEANED_sobolsampling-2048.csv')
datasetSobol1 = datasetSobol1.drop(datasetSobol1.columns[0], axis=1)
XSobol1 = datasetSobol1.drop('density', axis=1)
YSobol1 = datasetSobol1['density']

datasetSobol2 = pd.read_csv('CLEANED_sobolsampling-2048-2.csv')
datasetSobol2 = datasetSobol2.drop(datasetSobol2.columns[0], axis=1)
XSobol2 = datasetSobol2.drop('density', axis=1)
YSobol2 = datasetSobol2['density']


XInterpolation = np.concatenate((XGrid1296.to_numpy(), XGrid2401.to_numpy(), XSobol1.to_numpy(), XSobol2.to_numpy()), axis=0)
YInterpolation = np.concatenate((YGrid1296.to_numpy(), YGrid2401.to_numpy(), YSobol1.to_numpy(), YSobol2.to_numpy()), axis=0)
XInterpolation = torch.tensor(XInterpolation, dtype=torch.float32)
YInterpolation = torch.tensor(YInterpolation, dtype=torch.float32).reshape(-1, 1)


for thisRatio in trainRatios:
  thisTestRatio = 1-thisRatio
  tmpCWD = os.path.join(cwd, str(thisRatio))
  if os.path.exists(tmpCWD):
    if testmode:
      #shutil.rmtree(tmpCWD)
      pass
    else:
      print(f'\nPATH \'{tmpCWD}\' already exists. \n\nExiting without starting or changing anything.\n')
      exit()
  else:
    os.mkdir(tmpCWD)
  os.chdir(tmpCWD)
    
  for rndInt in rndInts:
    XGrid1296Train, XGrid1296Test, YGrid1296Train, YGrid1296Test = train_test_split(XGrid1296, YGrid1296, test_size=thisTestRatio, random_state=rndInt)
    XGrid1296Train = torch.tensor(XGrid1296Train.to_numpy(), dtype=torch.float32)
    YGrid1296Train = torch.tensor(YGrid1296Train.to_numpy(), dtype=torch.float32).reshape(-1, 1)
    XGrid1296Test = torch.tensor(XGrid1296Test.to_numpy(), dtype=torch.float32)
    YGrid1296Test = torch.tensor(YGrid1296Test.to_numpy(), dtype=torch.float32).reshape(-1, 1)
      
    XGrid2401Train, XGrid2401Test, YGrid2401Train, YGrid2401Test = train_test_split(XGrid2401, YGrid2401, test_size=thisTestRatio, random_state=rndInt)
    XGrid2401Train = torch.tensor(XGrid2401Train.to_numpy(), dtype=torch.float32)
    YGrid2401Train = torch.tensor(YGrid2401Train.to_numpy(), dtype=torch.float32).reshape(-1, 1)
    XGrid2401Test = torch.tensor(XGrid2401Test.to_numpy(), dtype=torch.float32)
    YGrid2401Test = torch.tensor(YGrid2401Test.to_numpy(), dtype=torch.float32).reshape(-1, 1)
    
    XSobol1Train, XSobol1Test, YSobol1Train, YSobol1Test = train_test_split(XSobol1, YSobol1, test_size=thisTestRatio, random_state=rndInt)
    XSobol1Train = torch.tensor(XSobol1Train.to_numpy(), dtype=torch.float32)
    YSobol1Train = torch.tensor(YSobol1Train.to_numpy(), dtype=torch.float32).reshape(-1, 1)
    XSobol1Test = torch.tensor(XSobol1Test.to_numpy(), dtype=torch.float32)
    YSobol1Test = torch.tensor(YSobol1Test.to_numpy(), dtype=torch.float32).reshape(-1, 1)
    
    XSobol2Train, XSobol2Test, YSobol2Train, YSobol2Test = train_test_split(XSobol2, YSobol2, test_size=thisTestRatio, random_state=rndInt)
    XSobol2Train = torch.tensor(XSobol2Train.to_numpy(), dtype=torch.float32)
    YSobol2Train = torch.tensor(YSobol2Train.to_numpy(), dtype=torch.float32).reshape(-1, 1)
    XSobol2Test = torch.tensor(XSobol2Test.to_numpy(), dtype=torch.float32)
    YSobol2Test = torch.tensor(YSobol2Test.to_numpy(), dtype=torch.float32).reshape(-1, 1)
    
    dfStatistics = pd.DataFrame({"ratio": [],
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

    for trainingDatasetName in trainingDatasetNames:
      if hiddenLayer == 3:
        model = thisModel3(architecture)
      else:
        print(f'hiddenLayer needs to be 3 (is {hiddenLayer}). Exit.')
        exit()
      
      loss_fn = nn.L1Loss()
      optimizer = optim.Adam(model.parameters(), lr=learning_rate)
        
      if trainingDatasetName == "Grid1296":
        XTrain = XGrid1296Train
        YTrain = YGrid1296Train
        XTest = XGrid1296Test
        YTest = YGrid1296Test
      elif trainingDatasetName == "Grid2401":
        XTrain = XGrid2401Train
        YTrain = YGrid2401Train
        XTest = XGrid2401Test
        YTest = YGrid2401Test
      elif trainingDatasetName == "Sobol1":
        XTrain = XSobol1Train
        YTrain = YSobol1Train
        XTest = XSobol1Test
        YTest = YSobol1Test
      elif trainingDatasetName == "Sobol2":
        XTrain = XSobol2Train
        YTrain = YSobol2Train
        XTest = XSobol2Test
        YTest = YSobol2Test
      else:
        print(f'trainingDatasetName needs to be Grid1296/Grid2401/Sobol1/Sobol2 (is {trainingDatasetName}). Exit.')
        exit()
        
      batch_size = 5
      while True:
        if len(XTrain)%batch_size == 0:
          break
        else:
          batch_size = batch_size + 1

  
      startTime = time.time()
      for epoch in range(n_epochs):
        for i in range(0, len(XTrain), batch_size):
          Xbatch = XTrain[i:i+batch_size]
          Ypred = model(Xbatch)
          Ybatch = YTrain[i:i+batch_size]
          loss = loss_fn(Ypred, Ybatch)
          optimizer.zero_grad()
          loss.backward()
          optimizer.step()
        
      thisTrainingTime = time.time() - startTime
      torch.save(model.state_dict(), f'trainedModel_{thisRatio}_{rndInt}_{trainingDatasetName}.pth')
      
      YpredTrain = model(XTrain)
      YpredTest = model(XTest)
      YpredInterpolation = model(XInterpolation)
      
      YpredictionsTrain = []
      YexpectationsTrain = []
      for i in range(len(YpredTrain)):
        YpredictionsTrain.append(YpredTrain[i].item())
        YexpectationsTrain.append(YTrain[i].item())
      thisMAPETrain = skmape(YpredictionsTrain, YexpectationsTrain)
      thisR2Train = r2_score(YpredictionsTrain, YexpectationsTrain)
        
      YpredictionsTest = []
      YexpectationsTest = []
      for i in range(len(YpredTest)):
        YpredictionsTest.append(YpredTest[i].item())
        YexpectationsTest.append(YTest[i].item())
      thisMAPETest = skmape(YpredictionsTest, YexpectationsTest)
      thisR2Test = r2_score(YpredictionsTest, YexpectationsTest)
        
      YpredictionsInterpolation = []
      YexpectationsInterpolation = []
      for i in range(len(YpredInterpolation)):
        YpredictionsInterpolation.append(YpredInterpolation[i].item())
        YexpectationsInterpolation.append(YInterpolation[i].item())
      thisMAPEInterpolation = skmape(YpredictionsInterpolation, YexpectationsInterpolation)
      thisR2Interpolation = r2_score(YpredictionsInterpolation, YexpectationsInterpolation)
      
      dfThisStats = pd.DataFrame({"ratio": [thisRatio],
                                  "rndint": [rndInt],
                                  "dataset": [trainingDatasetName],
                                  "learning_rate": [learning_rate],
                                  "batchsize": [batch_size],
                                  "epochs": [n_epochs],
                                  "loss": [loss.item()],
                                  "time": [thisTrainingTime],
                                  "mape": [thisMAPETrain],
                                  "r2": [thisR2Train],
                                  "mape_test": [thisMAPETest],
                                  "r2_test": [thisR2Test],
                                  "mape_interpolation": [thisMAPEInterpolation],
                                  "r2_interpolation": [thisR2Interpolation]})
      
      dfStatistics = pd.concat([dfStatistics, dfThisStats], ignore_index=True)


    statisticsFileName = f'StatsPart_{thisRatio}_{rndInt}.csv'
    statsFilePath = os.path.join(pwd, statisticsFileName)
  
    if os.path.exists(statsFilePath):
      os.remove(statsFilePath)
      print(f'Removed existing statistics file: \'{statsFilePath}\'.')
    dfStatistics.to_csv(statsFilePath)
    print(f'Wrote statistics to file: \'{statsFilePath}\'.')
    print(f'{dfStatistics}')



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
