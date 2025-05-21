from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score 
from sklearn.metrics import mean_absolute_percentage_error as skmape

import pandas as pd
import numpy as np
import os
import shutil

import pickle

pwd = os.getcwd()
modelsDir = os.path.join(pwd, "trainedModels")

rndInts = [678, 147, 561, 237, 588, 951, 490, 395, 877, 297, 721, 711, 985, 171, 75, 16, 669, 530, 999, 794, 936, 111, 816, 968, 48, 986, 829, 996, 272, 759, 390, 930, 633, 928, 854, 554, 562, 78, 222, 294, 725, 582, 731, 249, 791, 35, 180, 510, 593, 634]

testSizes = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]

## grid sampling 1296
data1296 = pd.read_csv('CLEANED_gridsearch_1296.csv')
data1296 = data1296.drop(data1296.columns[0], axis=1)
X_1296 = data1296.drop('density', axis=1)
Y_1296 = data1296['density']

## grid sampling 2401
data2401 = pd.read_csv('CLEANED_gridsearch_2401.csv')
data2401 = data2401.drop(data2401.columns[0], axis=1)
X_2401 = data2401.drop('density', axis=1)
Y_2401 = data2401['density']

## sobol2 sampling
data_sobol1 = pd.read_csv('CLEANED_sobolsampling-2048.csv')
data_sobol1 = data_sobol1.drop(data_sobol1.columns[0], axis=1)
X_sobol1 = data_sobol1.drop('density', axis=1)
Y_sobol1 = data_sobol1['density']

## sobol2 sampling
data_sobol2 = pd.read_csv('CLEANED_sobolsampling-2048-2.csv')
data_sobol2 = data_sobol2.drop(data_sobol2.columns[0], axis=1)
X_sobol2 = data_sobol2.drop('density', axis=1)
Y_sobol2 = data_sobol2['density']

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
    X_train, X_test, Y_train, Y_test = train_test_split(X_1296, Y_1296, test_size=thisRatio, random_state=rndInt)
    X_TEST1296_IST = X_test
    Y_TEST1296_IST = Y_test
    X_TEST1296_OST = pd.concat([X_2401, X_sobol1, X_sobol2], ignore_index=True)
    Y_TEST1296_OST = pd.concat([Y_2401, Y_sobol1, Y_sobol2], ignore_index=True)
    
    X_train, X_test, Y_train, Y_test = train_test_split(X_2401, Y_2401, test_size=thisRatio, random_state=rndInt)
    X_TEST2401_IST = X_test
    Y_TEST2401_IST = Y_test
    X_TEST2401_OST = pd.concat([X_1296, X_sobol1, X_sobol2], ignore_index=True)
    Y_TEST2401_OST = pd.concat([Y_1296, Y_sobol1, Y_sobol2], ignore_index=True)
    
    X_train, X_test, Y_train, Y_test = train_test_split(X_sobol1, Y_sobol1, test_size=thisRatio, random_state=rndInt)
    X_TESTSobol1_IST = X_test
    Y_TESTSobol1_IST = Y_test
    X_TESTSobol1_OST = pd.concat([X_1296, X_2401, X_sobol2], ignore_index=True)
    Y_TESTSobol1_OST = pd.concat([Y_1296, Y_2401, Y_sobol2], ignore_index=True)
    
    X_train, X_test, Y_train, Y_test = train_test_split(X_sobol2, Y_sobol2, test_size=thisRatio, random_state=rndInt)
    X_TESTSobol2_IST = X_test
    Y_TESTSobol2_IST = Y_test
    X_TESTSobol2_OST = pd.concat([X_1296, X_2401, X_sobol1], ignore_index=True)
    Y_TESTSobol2_OST = pd.concat([Y_1296, Y_2401, Y_sobol1], ignore_index=True)
    
    fileGrid1296 = f'trained_modelGrid1296_{thisRatio}_{rndInt}.sav'
    if os.path.isfile(fileGrid1296):
      with open(fileGrid1296, "rb") as input_file:
        model1296 = pickle.load(input_file)
    else:
      print(f'WARNING: Model file {fileGrid1296} does not exist!')
    
    fileGrid2401 = f'trained_modelGrid2401_{thisRatio}_{rndInt}.sav'
    if os.path.isfile(fileGrid2401):
      with open(fileGrid2401, "rb") as input_file:
        model2401 = pickle.load(input_file)
    else:
      print(f'WARNING: Model file {fileGrid2401} does not exist!')
        
    fileSobol1 = f'trained_modelSobol1_{thisRatio}_{rndInt}.sav'
    if os.path.isfile(fileSobol1):
      with open(fileSobol1, "rb") as input_file:
        modelSobol1 = pickle.load(input_file)
    else:
      print(f'WARNING: Model file {fileSobol1} does not exist!')
    
    fileSobol2 = f'trained_modelSobol2_{thisRatio}_{rndInt}.sav'
    if os.path.isfile(fileSobol2):
      with open(fileSobol2, "rb") as input_file:
        modelSobol2 = pickle.load(input_file)
    else:
      print(f'WARNING: Model file {fileSobol2} does not exist!')
    
    Y_prediction1296_IST = model1296.predict(X_TEST1296_IST)
    Y_prediction2401_IST = model2401.predict(X_TEST2401_IST)
    Y_predictionSobol1_IST = modelSobol1.predict(X_TESTSobol1_IST)
    Y_predictionSobol2_IST = modelSobol2.predict(X_TESTSobol2_IST)
    
    Y_prediction1296_OST = model1296.predict(X_TEST1296_OST)
    Y_prediction2401_OST = model2401.predict(X_TEST2401_OST)
    Y_predictionSobol1_OST = modelSobol1.predict(X_TESTSobol1_OST)
    Y_predictionSobol2_OST = modelSobol2.predict(X_TESTSobol2_OST)
    
    mape1296_IST = skmape(Y_TEST1296_IST, Y_prediction1296_IST)
    r21296_IST = r2_score(Y_TEST1296_IST, Y_prediction1296_IST)
    mape1296_OST = skmape(Y_TEST1296_OST, Y_prediction1296_OST)
    r21296_OST = r2_score(Y_TEST1296_OST, Y_prediction1296_OST)
    #
    mape2401_IST = skmape(Y_TEST2401_IST, Y_prediction2401_IST)
    r22401_IST = r2_score(Y_TEST2401_IST, Y_prediction2401_IST)
    mape2401_OST = skmape(Y_TEST2401_OST, Y_prediction2401_OST)
    r22401_OST = r2_score(Y_TEST2401_OST, Y_prediction2401_OST)
    #
    mapeSobol1_IST = skmape(Y_TESTSobol1_IST, Y_predictionSobol1_IST)
    r2Sobol1_IST = r2_score(Y_TESTSobol1_IST, Y_predictionSobol1_IST)
    mapeSobol1_OST = skmape(Y_TESTSobol1_OST, Y_predictionSobol1_OST)
    r2Sobol1_OST = r2_score(Y_TESTSobol1_OST, Y_predictionSobol1_OST)
    #
    mapeSobol2_IST = skmape(Y_TESTSobol2_IST, Y_predictionSobol2_IST)
    r2Sobol2_IST = r2_score(Y_TESTSobol2_IST, Y_predictionSobol2_IST)
    mapeSobol2_OST = skmape(Y_TESTSobol2_OST, Y_predictionSobol2_OST)
    r2Sobol2_OST = r2_score(Y_TESTSobol2_OST, Y_predictionSobol2_OST)
    
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


































