from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score 
from sklearn.metrics import mean_absolute_percentage_error as skmape

import pandas as pd
import numpy as np
import os
import shutil

import pickle

testmode = True

pwd = os.getcwd()
### create current working directory ###
cwd = os.path.join(pwd, "trainedModels")
#print(f'{cwd}')
if os.path.exists(cwd):
  if testmode:
    shutil.rmtree(cwd)
  else:
    print(f'\nPATH \'{cwd}\' already exists. \n\nExiting without starting or changing anything.\n')
    exit()

os.mkdir(cwd)

rndInts = [678, 147, 561, 237, 588, 951, 490, 395, 877, 297, 721, 711, 985, 171, 75, 16, 669, 530, 999, 794, 936, 111, 816, 968, 48, 986, 829, 996, 272, 759, 390, 930, 633, 928, 854, 554, 562, 78, 222, 294, 725, 582, 731, 249, 791, 35, 180, 510, 593, 634]

testSizes = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]

## grid sampling 1296
data1296 = pd.read_csv('CLEANED_gridsearch_1296.csv')
data1296 = data1296.drop(data1296.columns[0], axis=1)
X_1296 = data1296.drop('density', axis=1)
Y_1296 = data1296['density']
#print(f'{data1296}')
#print(f'{X_1296}')
#print(f'{Y_1296}')

## grid sampling 2401
data2401 = pd.read_csv('CLEANED_gridsearch_2401.csv')
data2401 = data2401.drop(data2401.columns[0], axis=1)
X_2401 = data2401.drop('density', axis=1)
Y_2401 = data2401['density']
#print(f'{data2401}')
#print(f'{X_2401}')
#print(f'{Y_2401}')

## sobol2 sampling
data_sobol1 = pd.read_csv('CLEANED_sobolsampling-2048.csv')
data_sobol1 = data_sobol1.drop(data_sobol1.columns[0], axis=1)
X_sobol1 = data_sobol1.drop('density', axis=1)
Y_sobol1 = data_sobol1['density']
#print(f'{data_sobol1}')
#print(f'{X_sobol1}')
#print(f'{Y_sobol1}')

## sobol2 sampling
data_sobol2 = pd.read_csv('CLEANED_sobolsampling-2048-2.csv')
data_sobol2 = data_sobol2.drop(data_sobol2.columns[0], axis=1)
X_sobol2 = data_sobol2.drop('density', axis=1)
Y_sobol2 = data_sobol2['density']
#print(f'{data_sobol2}')
#print(f'{X_sobol2}')
#print(f'{Y_sobol2}')

dfStatistics = pd.DataFrame({"ratio": [],
                             "rndint": [],
                             "dataset": [],
                             "rmse": [],
                             "mape": [],
                             "r2": [],
                             "rmse_all": [],
                             "mape_all": [],
                             "r2_all": []})

for thisRatio in testSizes:
  tmp_cwd = os.path.join(cwd, str(thisRatio))
  os.mkdir(tmp_cwd)
  os.chdir(tmp_cwd)
  
  for rndInt in rndInts:
    X_train, X_test, Y_train, Y_test = train_test_split(X_1296, Y_1296, test_size=thisRatio, random_state=rndInt)
    X_TRAIN1296 = X_train
    Y_TRAIN1296 = Y_train
    #X_test = pd.concat([X_test, X_2401, X_sobol1, X_sobol2], ignore_index=True)
    #Y_test = pd.concat([Y_test, Y_2401, Y_sobol1, Y_sobol2], ignore_index=True)
    X_TEST1296 = X_test
    Y_TEST1296 = Y_test
    X_TEST1296_ALL = pd.concat([X_test, X_2401, X_sobol1, X_sobol2], ignore_index=True)
    Y_TEST1296_ALL = pd.concat([Y_test, Y_2401, Y_sobol1, Y_sobol2], ignore_index=True)
    
    X_train, X_test, Y_train, Y_test = train_test_split(X_2401, Y_2401, test_size=thisRatio, random_state=rndInt)
    X_TRAIN2401 = X_train
    Y_TRAIN2401 = Y_train
    #X_test = pd.concat([X_test, X_1296, X_sobol1, X_sobol2], ignore_index=True)
    #Y_test = pd.concat([Y_test, Y_1296, Y_sobol1, Y_sobol2], ignore_index=True)
    X_TEST2401 = X_test
    Y_TEST2401 = Y_test
    X_TEST2401_ALL = pd.concat([X_test, X_1296, X_sobol1, X_sobol2], ignore_index=True)
    Y_TEST2401_ALL = pd.concat([Y_test, Y_1296, Y_sobol1, Y_sobol2], ignore_index=True)
    
    X_train, X_test, Y_train, Y_test = train_test_split(X_sobol1, Y_sobol1, test_size=thisRatio, random_state=rndInt)
    X_TRAINSobol1 = X_train
    Y_TRAINSobol1 = Y_train
    #X_test = pd.concat([X_test, X_1296, X_2401, X_sobol2], ignore_index=True)
    #Y_test = pd.concat([Y_test, Y_1296, Y_2401, Y_sobol2], ignore_index=True)
    X_TESTSobol1 = X_test
    Y_TESTSobol1 = Y_test
    X_TESTSobol1_ALL = pd.concat([X_test, X_1296, X_2401, X_sobol2], ignore_index=True)
    Y_TESTSobol1_ALL = pd.concat([Y_test, Y_1296, Y_2401, Y_sobol2], ignore_index=True)
    
    X_train, X_test, Y_train, Y_test = train_test_split(X_sobol2, Y_sobol2, test_size=thisRatio, random_state=rndInt)
    X_TRAINSobol2 = X_train
    Y_TRAINSobol2 = Y_train
    #X_test = pd.concat([X_test, X_1296, X_2401, X_sobol1], ignore_index=True)
    #Y_test = pd.concat([Y_test, Y_1296, Y_2401, Y_sobol1], ignore_index=True)
    X_TESTSobol2 = X_test
    Y_TESTSobol2 = Y_test
    X_TESTSobol2_ALL = pd.concat([X_test, X_1296, X_2401, X_sobol1], ignore_index=True)
    Y_TESTSobol2_ALL = pd.concat([Y_test, Y_1296, Y_2401, Y_sobol1], ignore_index=True)
    
    model1296 = LinearRegression()
    model2401 = LinearRegression()
    modelSobol1 = LinearRegression()
    modelSobol2 = LinearRegression()
    
    model1296.fit(X_TRAIN1296, Y_TRAIN1296)
    model2401.fit(X_TRAIN2401, Y_TRAIN2401)
    modelSobol1.fit(X_TRAINSobol1, Y_TRAINSobol1)
    modelSobol2.fit(X_TRAINSobol2, Y_TRAINSobol2)
    
    pickle.dump(model1296, open(f'trained_modelGrid1296_{thisRatio}_{rndInt}.sav', 'wb'))
    pickle.dump(model2401, open(f'trained_modelGrid2401_{thisRatio}_{rndInt}.sav', 'wb'))
    pickle.dump(modelSobol1, open(f'trained_modelSobol1_{thisRatio}_{rndInt}.sav', 'wb'))
    pickle.dump(modelSobol2, open(f'trained_modelSobol2_{thisRatio}_{rndInt}.sav', 'wb'))
    
    Y_prediction1296 = model1296.predict(X_TEST1296)
    Y_prediction2401 = model2401.predict(X_TEST2401)
    Y_predictionSobol1 = modelSobol1.predict(X_TESTSobol1)
    Y_predictionSobol2 = modelSobol2.predict(X_TESTSobol2)
    
    Y_prediction1296_ALL = model1296.predict(X_TEST1296_ALL)
    Y_prediction2401_ALL = model2401.predict(X_TEST2401_ALL)
    Y_predictionSobol1_ALL = modelSobol1.predict(X_TESTSobol1_ALL)
    Y_predictionSobol2_ALL = modelSobol2.predict(X_TESTSobol2_ALL)
    
    rmse1296 = np.sqrt(mean_squared_error(Y_TEST1296, Y_prediction1296))
    mape1296 = skmape(Y_TEST1296, Y_prediction1296)
    r21296 = r2_score(Y_TEST1296, Y_prediction1296)
    rmse1296_ALL = np.sqrt(mean_squared_error(Y_TEST1296_ALL, Y_prediction1296_ALL))
    mape1296_ALL = skmape(Y_TEST1296_ALL, Y_prediction1296_ALL)
    r21296_ALL = r2_score(Y_TEST1296_ALL, Y_prediction1296_ALL)
    #
    rmse2401 = np.sqrt(mean_squared_error(Y_TEST2401, Y_prediction2401))
    mape2401 = skmape(Y_TEST2401, Y_prediction2401)
    r22401 = r2_score(Y_TEST2401, Y_prediction2401)
    rmse2401_ALL = np.sqrt(mean_squared_error(Y_TEST2401_ALL, Y_prediction2401_ALL))
    mape2401_ALL = skmape(Y_TEST2401_ALL, Y_prediction2401_ALL)
    r22401_ALL = r2_score(Y_TEST2401_ALL, Y_prediction2401_ALL)
    #
    rmseSobol1 = np.sqrt(mean_squared_error(Y_TESTSobol1, Y_predictionSobol1))
    mapeSobol1 = skmape(Y_TESTSobol1, Y_predictionSobol1)
    r2Sobol1 = r2_score(Y_TESTSobol1, Y_predictionSobol1)
    rmseSobol1_ALL = np.sqrt(mean_squared_error(Y_TESTSobol1_ALL, Y_predictionSobol1_ALL))
    mapeSobol1_ALL = skmape(Y_TESTSobol1_ALL, Y_predictionSobol1_ALL)
    r2Sobol1_ALL = r2_score(Y_TESTSobol1_ALL, Y_predictionSobol1_ALL)
    #
    rmseSobol2 = np.sqrt(mean_squared_error(Y_TESTSobol2, Y_predictionSobol2))
    mapeSobol2 = skmape(Y_TESTSobol2, Y_predictionSobol2)
    r2Sobol2 = r2_score(Y_TESTSobol2, Y_predictionSobol2)
    rmseSobol2_ALL = np.sqrt(mean_squared_error(Y_TESTSobol2_ALL, Y_predictionSobol2_ALL))
    mapeSobol2_ALL = skmape(Y_TESTSobol2_ALL, Y_predictionSobol2_ALL)
    r2Sobol2_ALL = r2_score(Y_TESTSobol2_ALL, Y_predictionSobol2_ALL)
    
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Grid1296"],
                            "rmse": [rmse1296],
                            "mape": [mape1296],
                            "r2": [r21296],
                            "rmse_all": [rmse1296_ALL],
                            "mape_all": [mape1296_ALL],
                            "r2_all": [r21296_ALL]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Grid2401"],
                            "rmse": [rmse2401],
                            "mape": [mape2401],
                            "r2": [r22401],
                            "rmse_all": [rmse2401_ALL],
                            "mape_all": [mape2401_ALL],
                            "r2_all": [r22401_ALL]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Sobol1"],
                            "rmse": [rmseSobol1],
                            "mape": [mapeSobol1],
                            "r2": [r2Sobol1],
                            "rmse_all": [rmseSobol1_ALL],
                            "mape_all": [mapeSobol1_ALL],
                            "r2_all": [r2Sobol1_ALL]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Sobol2"],
                            "rmse": [rmseSobol2],
                            "mape": [mapeSobol2],
                            "r2": [r2Sobol2],
                            "rmse_all": [rmseSobol2_ALL],
                            "mape_all": [mapeSobol2_ALL],
                            "r2_all": [r2Sobol2_ALL]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)


  os.chdir(cwd)

os.chdir(pwd)
statisticsFileName = 'Stats.csv'
if os.path.exists(statisticsFileName):
  os.remove(statisticsFileName)
  print(f'Removed existing statistics file: \'{statisticsFileName}\'.')
dfStatistics.to_csv(statisticsFileName)
print(f'Wrote statistics to file: \'{statisticsFileName}\'.')
print(f'{dfStatistics}')


































