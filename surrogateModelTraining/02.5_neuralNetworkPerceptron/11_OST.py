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

pwd = os.getcwd()
modelsDir = os.path.join(pwd, "trainedModels")

rndInts = [678, 147, 561, 237, 588, 951, 490, 395, 877, 297, 721, 711, 985, 171, 75, 16, 669, 530, 999, 794, 936, 111, 816, 968, 48, 986, 829, 996, 272, 759, 390, 930, 633, 928, 854, 554, 562, 78, 222, 294, 725, 582, 731, 249, 791, 35, 180, 510, 593, 634]

testSizes = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]

trainingDatasetNames = ["Grid1296", "Grid2401", "Sobol1", "Sobol2"]

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

dfStatistics = pd.DataFrame({"ratio": [],
                             "rndint": [],
                             "dataset": [],
                             "mape_ist": [],
                             "r2_ist": [],
                             "mape_ost": [],
                             "r2_ost": []})

for thisRatio in testSizes:
  tmp_cwd = os.path.join(modelsDir, str(thisRatio))
  os.chdir(tmp_cwd)
    
  for rndInt in rndInts:
    XGrid1296Train, XGrid1296Test, YGrid1296Train, YGrid1296Test = train_test_split(XGrid1296, YGrid1296, test_size=thisRatio, random_state=rndInt)
    XGrid1296Test_IST = torch.tensor(XGrid1296Test.to_numpy(), dtype=torch.float32)
    YGrid1296Test_IST = torch.tensor(YGrid1296Test.to_numpy(), dtype=torch.float32).reshape(-1, 1)
    XGrid1296Test_OST = np.concatenate((XGrid2401.to_numpy(), XSobol1.to_numpy(), XSobol2.to_numpy()), axis=0)
    YGrid1296Test_OST = np.concatenate((YGrid2401.to_numpy(), YSobol1.to_numpy(), YSobol2.to_numpy()), axis=0)
    XGrid1296Test_OST = torch.tensor(XGrid1296Test_OST, dtype=torch.float32)
    YGrid1296Test_OST = torch.tensor(YGrid1296Test_OST, dtype=torch.float32).reshape(-1, 1)
      
    XGrid2401Train, XGrid2401Test, YGrid2401Train, YGrid2401Test = train_test_split(XGrid2401, YGrid2401, test_size=thisRatio, random_state=rndInt)
    XGrid2401Test_IST = torch.tensor(XGrid2401Test.to_numpy(), dtype=torch.float32)
    YGrid2401Test_IST = torch.tensor(YGrid2401Test.to_numpy(), dtype=torch.float32).reshape(-1, 1)
    XGrid2401Test_OST = np.concatenate((XGrid1296.to_numpy(), XSobol1.to_numpy(), XSobol2.to_numpy()), axis=0)
    YGrid2401Test_OST = np.concatenate((YGrid1296.to_numpy(), YSobol1.to_numpy(), YSobol2.to_numpy()), axis=0)
    XGrid2401Test_OST = torch.tensor(XGrid2401Test_OST, dtype=torch.float32)
    YGrid2401Test_OST = torch.tensor(YGrid2401Test_OST, dtype=torch.float32).reshape(-1, 1)
    
    XSobol1Train, XSobol1Test, YSobol1Train, YSobol1Test = train_test_split(XSobol1, YSobol1, test_size=thisRatio, random_state=rndInt)
    XSobol1Test_IST = torch.tensor(XSobol1Test.to_numpy(), dtype=torch.float32)
    YSobol1Test_IST = torch.tensor(YSobol1Test.to_numpy(), dtype=torch.float32).reshape(-1, 1)
    XSobol1Test_OST = np.concatenate((XGrid1296.to_numpy(), XGrid2401.to_numpy(), XSobol2.to_numpy()), axis=0)
    YSobol1Test_OST = np.concatenate((YGrid1296.to_numpy(), YGrid2401.to_numpy(), YSobol2.to_numpy()), axis=0)
    XSobol1Test_OST = torch.tensor(XSobol1Test_OST, dtype=torch.float32)
    YSobol1Test_OST = torch.tensor(YSobol1Test_OST, dtype=torch.float32).reshape(-1, 1)
    
    XSobol2Train, XSobol2Test, YSobol2Train, YSobol2Test = train_test_split(XSobol2, YSobol2, test_size=thisRatio, random_state=rndInt)
    XSobol2Test_IST = torch.tensor(XSobol2Test.to_numpy(), dtype=torch.float32)
    YSobol2Test_IST = torch.tensor(YSobol2Test.to_numpy(), dtype=torch.float32).reshape(-1, 1)
    XSobol2Test_OST = np.concatenate((XGrid1296.to_numpy(), XGrid2401.to_numpy(), XSobol1.to_numpy()), axis=0)
    YSobol2Test_OST = np.concatenate((YGrid1296.to_numpy(), YGrid2401.to_numpy(), YSobol1.to_numpy()), axis=0)
    XSobol2Test_OST = torch.tensor(XSobol2Test_OST, dtype=torch.float32)
    YSobol2Test_OST = torch.tensor(YSobol2Test_OST, dtype=torch.float32).reshape(-1, 1)
    
    fileGrid1296 = f'trainedModel_{thisRatio}_{rndInt}_Grid1296.pth'
    model1296 = thisModel3(architecture)
    if os.path.isfile(fileGrid1296):
      model1296.load_state_dict(torch.load(fileGrid1296, weights_only=True))
    else:
      print(f'WARNING: Model file {fileGrid1296} does not exist!')
   
    fileGrid2401 = f'trainedModel_{thisRatio}_{rndInt}_Grid2401.pth'
    model2401 = thisModel3(architecture)
    if os.path.isfile(fileGrid2401):
      model2401.load_state_dict(torch.load(fileGrid2401, weights_only=True))
    else:
      print(f'WARNING: Model file {fileGrid2401} does not exist!')
        
    fileSobol1 = f'trainedModel_{thisRatio}_{rndInt}_Sobol1.pth'
    modelSobol1 = thisModel3(architecture)
    if os.path.isfile(fileSobol1):
      modelSobol1.load_state_dict(torch.load(fileSobol1, weights_only=True))
    else:
      print(f'WARNING: Model file {fileSobol1} does not exist!')
    
    fileSobol2 = f'trainedModel_{thisRatio}_{rndInt}_Sobol2.pth'
    modelSobol2 = thisModel3(architecture)
    if os.path.isfile(fileSobol2):
      modelSobol2.load_state_dict(torch.load(fileSobol2, weights_only=True))
    else:
      print(f'WARNING: Model file {fileSobol2} does not exist!')

    Y_prediction1296_IST = model1296(XGrid1296Test_IST)
    Y_prediction2401_IST = model2401(XGrid2401Test_IST)
    Y_predictionSobol1_IST = modelSobol1(XSobol1Test_IST)
    Y_predictionSobol2_IST = modelSobol2(XSobol2Test_IST)
    
    Y_prediction1296_OST = model1296(XGrid1296Test_OST)
    Y_prediction2401_OST = model2401(XGrid2401Test_OST)
    Y_predictionSobol1_OST = modelSobol1(XSobol1Test_OST)
    Y_predictionSobol2_OST = modelSobol2(XSobol2Test_OST)
      
    YPred1296_IST = []
    YExprect1296_IST = []
    for i in range(len(Y_prediction1296_IST)):
      YPred1296_IST.append(Y_prediction1296_IST[i].item())
      YExprect1296_IST.append(YGrid1296Test_IST[i].item())
    mape1296_IST = skmape(YPred1296_IST, YExprect1296_IST)
    r21296_IST = r2_score(YPred1296_IST, YExprect1296_IST)
    YPred1296_OST = []
    YExprect1296_OST = []
    for i in range(len(Y_prediction1296_OST)):
      YPred1296_OST.append(Y_prediction1296_OST[i].item())
      YExprect1296_OST.append(YGrid1296Test_OST[i].item())
    mape1296_OST = skmape(YPred1296_OST, YExprect1296_OST)
    r21296_OST = r2_score(YPred1296_OST, YExprect1296_OST)
      
    YPred2401_IST = []
    YExprect2401_IST = []
    for i in range(len(Y_prediction2401_IST)):
      YPred2401_IST.append(Y_prediction2401_IST[i].item())
      YExprect2401_IST.append(YGrid2401Test_IST[i].item())
    mape2401_IST = skmape(YPred2401_IST, YExprect2401_IST)
    r22401_IST = r2_score(YPred2401_IST, YExprect2401_IST)
    YPred2401_OST = []
    YExprect2401_OST = []
    for i in range(len(Y_prediction2401_OST)):
      YPred2401_OST.append(Y_prediction2401_OST[i].item())
      YExprect2401_OST.append(YGrid2401Test_OST[i].item())
    mape2401_OST = skmape(YPred2401_OST, YExprect2401_OST)
    r22401_OST = r2_score(YPred2401_OST, YExprect2401_OST)
    
    YPredSobol1_IST = []
    YExprectSobol1_IST = []
    for i in range(len(Y_predictionSobol1_IST)):
      YPredSobol1_IST.append(Y_predictionSobol1_IST[i].item())
      YExprectSobol1_IST.append(YSobol1Test_IST[i].item())
    mapeSobol1_IST = skmape(YPredSobol1_IST, YExprectSobol1_IST)
    r2Sobol1_IST = r2_score(YPredSobol1_IST, YExprectSobol1_IST)
    YPredSobol1_OST = []
    YExprectSobol1_OST = []
    for i in range(len(Y_predictionSobol1_OST)):
      YPredSobol1_OST.append(Y_predictionSobol1_OST[i].item())
      YExprectSobol1_OST.append(YSobol1Test_OST[i].item())
    mapeSobol1_OST = skmape(YPredSobol1_OST, YExprectSobol1_OST)
    r2Sobol1_OST = r2_score(YPredSobol1_OST, YExprectSobol1_OST)
    
    YPredSobol2_IST = []
    YExprectSobol2_IST = []
    for i in range(len(Y_predictionSobol2_IST)):
      YPredSobol2_IST.append(Y_predictionSobol2_IST[i].item())
      YExprectSobol2_IST.append(YSobol2Test_IST[i].item())
    mapeSobol2_IST = skmape(YPredSobol2_IST, YExprectSobol2_IST)
    r2Sobol2_IST = r2_score(YPredSobol2_IST, YExprectSobol2_IST)
      
    YPredSobol2_OST = []
    YExprectSobol2_OST = []
    for i in range(len(Y_predictionSobol2_OST)):
      YPredSobol2_OST.append(Y_predictionSobol2_OST[i].item())
      YExprectSobol2_OST.append(YSobol2Test_OST[i].item())
    mapeSobol2_OST = skmape(YPredSobol2_OST, YExprectSobol2_OST)
    r2Sobol2_OST = r2_score(YPredSobol2_OST, YExprectSobol2_OST)
      
      
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Grid1296"],
                            "mape_ist": [mape1296_IST],
                             "r2_ist": [r21296_IST],
                            "mape_ost": [mape1296_OST],
                            "r2_ost": [r21296_OST]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Grid2401"],
                            "mape_ist": [mape2401_IST],
                            "r2_ist": [r22401_IST],
                            "mape_ost": [mape2401_OST],
                            "r2_ost": [r22401_OST]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Sobol1"],
                            "mape_ist": [mapeSobol1_IST],
                            "r2_ist": [r2Sobol1_IST],
                            "mape_ost": [mapeSobol1_OST],
                            "r2_ost": [r2Sobol1_OST]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Sobol2"],
                            "mape_ist": [mapeSobol2_IST],
                            "r2_ist": [r2Sobol2_IST],
                            "mape_ost": [mapeSobol2_OST],
                            "r2_ost": [r2Sobol2_OST]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)

  os.chdir(modelsDir)

os.chdir(pwd)
statisticsFileName = 'Stats_OST.csv'
if os.path.exists(statisticsFileName):
  os.remove(statisticsFileName)
  print(f'Removed existing statistics file: \'{statisticsFileName}\'.')
dfStatistics.to_csv(statisticsFileName)
print(f'Wrote statistics to file: \'{statisticsFileName}\'.')
print(f'{dfStatistics}')



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
