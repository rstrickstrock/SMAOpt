### imports ###
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from sklearn.gaussian_process.kernels import Matern
from sklearn.gaussian_process.kernels import RationalQuadratic as RQ
from sklearn.gaussian_process.kernels import ExpSineSquared as ESS

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import mean_absolute_percentage_error as skmape

import pandas as pd
import numpy as np
import os
import shutil

import pickle

testmode = True

rndInts = [678, 147, 561, 237, 588, 951, 490, 395, 877, 297, 721, 711, 985, 171, 75, 16, 669, 530, 999, 794, 936, 111, 816, 968, 48, 986, 829, 996, 272, 759, 390, 930, 633, 928, 854, 554, 562, 78, 222, 294, 725, 582, 731, 249, 791, 35, 180, 510, 593, 634]

testSizes = [0.10, 0.90]

statisticsFileName = 'Stats-1.csv'



pwd = os.getcwd()
### create current working directory ###
cwd = os.path.join(pwd, "trainedModels")
#print(f'{cwd}')
if os.path.exists(cwd):
  if testmode:
    pass
    #shutil.rmtree(cwd)
  else:
    print(f'\nPATH \'{cwd}\' already exists. \n\nExiting without starting or changing anything.\n')
    exit()
else:
  os.mkdir(cwd)
#os.mkdir(cwd)

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
                             "kernel": [],
                             "length_scale": [],
                             "nu": [],
                             "alpha": [],
                             "periodicity": [],
                             "rmse": [],
                             "mape": [],
                             "r2": [],
                             "rmse_all": [],
                             "mape_all": [],
                             "r2_all": []})

n_restarts = 9

for thisRatio in testSizes:
  trainSize = 1-thisRatio
  print(f'Training GPR Models with {trainSize}% of the dataset.\n')
  tmp_cwd = os.path.join(cwd, str(thisRatio))
  os.mkdir(tmp_cwd)
  os.chdir(tmp_cwd)
  
  for rndInt in rndInts:
    #print(f'.')
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
    
    kernel1 = RBF()
    kernel2 = Matern()
    kernel3 = RQ()
    kernel4 = ESS()
    
    model1Grid1296 = GaussianProcessRegressor(kernel=kernel1, optimizer='fmin_l_bfgs_b', n_restarts_optimizer=n_restarts, random_state=rndInt)
    model2Grid1296 = GaussianProcessRegressor(kernel=kernel2, optimizer='fmin_l_bfgs_b', n_restarts_optimizer=n_restarts, random_state=rndInt)
    model3Grid1296 = GaussianProcessRegressor(kernel=kernel3, optimizer='fmin_l_bfgs_b', n_restarts_optimizer=n_restarts, random_state=rndInt)
    model4Grid1296 = GaussianProcessRegressor(kernel=kernel4, optimizer='fmin_l_bfgs_b', n_restarts_optimizer=n_restarts, random_state=rndInt)
    
    model1Grid2401 = GaussianProcessRegressor(kernel=kernel1, optimizer='fmin_l_bfgs_b', n_restarts_optimizer=n_restarts, random_state=rndInt)
    model2Grid2401 = GaussianProcessRegressor(kernel=kernel2, optimizer='fmin_l_bfgs_b', n_restarts_optimizer=n_restarts, random_state=rndInt)
    model3Grid2401 = GaussianProcessRegressor(kernel=kernel3, optimizer='fmin_l_bfgs_b', n_restarts_optimizer=n_restarts, random_state=rndInt)
    model4Grid2401 = GaussianProcessRegressor(kernel=kernel4, optimizer='fmin_l_bfgs_b', n_restarts_optimizer=n_restarts, random_state=rndInt)
    
    model1Sobol1 = GaussianProcessRegressor(kernel=kernel1, optimizer='fmin_l_bfgs_b', n_restarts_optimizer=n_restarts, random_state=rndInt)
    model2Sobol1 = GaussianProcessRegressor(kernel=kernel2, optimizer='fmin_l_bfgs_b', n_restarts_optimizer=n_restarts, random_state=rndInt)
    model3Sobol1 = GaussianProcessRegressor(kernel=kernel3, optimizer='fmin_l_bfgs_b', n_restarts_optimizer=n_restarts, random_state=rndInt)
    model4Sobol1 = GaussianProcessRegressor(kernel=kernel4, optimizer='fmin_l_bfgs_b', n_restarts_optimizer=n_restarts, random_state=rndInt)
    
    model1Sobol2 = GaussianProcessRegressor(kernel=kernel1, optimizer='fmin_l_bfgs_b', n_restarts_optimizer=n_restarts, random_state=rndInt)
    model2Sobol2 = GaussianProcessRegressor(kernel=kernel2, optimizer='fmin_l_bfgs_b', n_restarts_optimizer=n_restarts, random_state=rndInt)
    model3Sobol2 = GaussianProcessRegressor(kernel=kernel3, optimizer='fmin_l_bfgs_b', n_restarts_optimizer=n_restarts, random_state=rndInt)
    model4Sobol2 = GaussianProcessRegressor(kernel=kernel4, optimizer='fmin_l_bfgs_b', n_restarts_optimizer=n_restarts, random_state=rndInt)
    
    model1Grid1296.fit(X_TRAIN1296, Y_TRAIN1296)
    model2Grid1296.fit(X_TRAIN1296, Y_TRAIN1296)
    model3Grid1296.fit(X_TRAIN1296, Y_TRAIN1296)
    model4Grid1296.fit(X_TRAIN1296, Y_TRAIN1296)
    
    model1Grid2401.fit(X_TRAIN2401, Y_TRAIN2401)
    model2Grid2401.fit(X_TRAIN2401, Y_TRAIN2401)
    model3Grid2401.fit(X_TRAIN2401, Y_TRAIN2401)
    model4Grid2401.fit(X_TRAIN2401, Y_TRAIN2401)
    
    model1Sobol1.fit(X_TRAINSobol1, Y_TRAINSobol1)
    model2Sobol1.fit(X_TRAINSobol1, Y_TRAINSobol1)
    model3Sobol1.fit(X_TRAINSobol1, Y_TRAINSobol1)
    model4Sobol1.fit(X_TRAINSobol1, Y_TRAINSobol1)
    
    model1Sobol2.fit(X_TRAINSobol2, Y_TRAINSobol2)
    model2Sobol2.fit(X_TRAINSobol2, Y_TRAINSobol2)
    model3Sobol2.fit(X_TRAINSobol2, Y_TRAINSobol2)
    model4Sobol2.fit(X_TRAINSobol2, Y_TRAINSobol2)
    
    pickle.dump(model1Grid1296, open(f'trained_modelGrid1296_{thisRatio}_{rndInt}_RBF.sav', 'wb'))
    pickle.dump(model2Grid1296, open(f'trained_modelGrid1296_{thisRatio}_{rndInt}_Matern.sav', 'wb'))
    pickle.dump(model3Grid1296, open(f'trained_modelGrid1296_{thisRatio}_{rndInt}_RQ.sav', 'wb'))
    pickle.dump(model4Grid1296, open(f'trained_modelGrid1296_{thisRatio}_{rndInt}_ESS.sav', 'wb'))
    
    pickle.dump(model1Grid2401, open(f'trained_modelGrid2401_{thisRatio}_{rndInt}_RBF.sav', 'wb'))
    pickle.dump(model2Grid2401, open(f'trained_modelGrid2401_{thisRatio}_{rndInt}_Matern.sav', 'wb'))
    pickle.dump(model3Grid2401, open(f'trained_modelGrid2401_{thisRatio}_{rndInt}_RQ.sav', 'wb'))
    pickle.dump(model4Grid2401, open(f'trained_modelGrid2401_{thisRatio}_{rndInt}_ESS.sav', 'wb'))
    
    pickle.dump(model1Sobol1, open(f'trained_modelSobol1_{thisRatio}_{rndInt}_RBF.sav', 'wb'))
    pickle.dump(model2Sobol1, open(f'trained_modelSobol1_{thisRatio}_{rndInt}_Matern.sav', 'wb'))
    pickle.dump(model3Sobol1, open(f'trained_modelSobol1_{thisRatio}_{rndInt}_RQ.sav', 'wb'))
    pickle.dump(model4Sobol1, open(f'trained_modelSobol1_{thisRatio}_{rndInt}_ESS.sav', 'wb'))
    
    pickle.dump(model1Sobol2, open(f'trained_modelSobol2_{thisRatio}_{rndInt}_RBF.sav', 'wb'))
    pickle.dump(model2Sobol2, open(f'trained_modelSobol2_{thisRatio}_{rndInt}_Matern.sav', 'wb'))
    pickle.dump(model3Sobol2, open(f'trained_modelSobol2_{thisRatio}_{rndInt}_RQ.sav', 'wb'))
    pickle.dump(model4Sobol2, open(f'trained_modelSobol2_{thisRatio}_{rndInt}_ESS.sav', 'wb'))

    Y_1prediction1296 = model1Grid1296.predict(X_TEST1296)
    Y_2prediction1296 = model2Grid1296.predict(X_TEST1296)
    Y_3prediction1296 = model3Grid1296.predict(X_TEST1296)
    Y_4prediction1296 = model4Grid1296.predict(X_TEST1296)
    
    Y_1prediction2401 = model1Grid2401.predict(X_TEST2401)
    Y_2prediction2401 = model2Grid2401.predict(X_TEST2401)
    Y_3prediction2401 = model3Grid2401.predict(X_TEST2401)
    Y_4prediction2401 = model4Grid2401.predict(X_TEST2401)
    
    Y_1predictionSobol1 = model1Sobol1.predict(X_TESTSobol1)
    Y_2predictionSobol1 = model2Sobol1.predict(X_TESTSobol1)
    Y_3predictionSobol1 = model3Sobol1.predict(X_TESTSobol1)
    Y_4predictionSobol1 = model4Sobol1.predict(X_TESTSobol1)
    
    Y_1predictionSobol2 = model1Sobol2.predict(X_TESTSobol2)
    Y_2predictionSobol2 = model2Sobol2.predict(X_TESTSobol2)
    Y_3predictionSobol2 = model3Sobol2.predict(X_TESTSobol2)
    Y_4predictionSobol2 = model4Sobol2.predict(X_TESTSobol2)
    
    Y_1prediction1296_ALL = model1Grid1296.predict(X_TEST1296_ALL)
    Y_2prediction1296_ALL = model2Grid1296.predict(X_TEST1296_ALL)
    Y_3prediction1296_ALL = model3Grid1296.predict(X_TEST1296_ALL)
    Y_4prediction1296_ALL = model4Grid1296.predict(X_TEST1296_ALL)
    
    Y_1prediction2401_ALL = model1Grid2401.predict(X_TEST2401_ALL)
    Y_2prediction2401_ALL = model2Grid2401.predict(X_TEST2401_ALL)
    Y_3prediction2401_ALL = model3Grid2401.predict(X_TEST2401_ALL)
    Y_4prediction2401_ALL = model4Grid2401.predict(X_TEST2401_ALL)
    
    Y_1predictionSobol1_ALL = model1Sobol1.predict(X_TESTSobol1_ALL)
    Y_2predictionSobol1_ALL = model2Sobol1.predict(X_TESTSobol1_ALL)
    Y_3predictionSobol1_ALL = model3Sobol1.predict(X_TESTSobol1_ALL)
    Y_4predictionSobol1_ALL = model4Sobol1.predict(X_TESTSobol1_ALL)
    
    Y_1predictionSobol2_ALL = model1Sobol2.predict(X_TESTSobol2_ALL)
    Y_2predictionSobol2_ALL = model2Sobol2.predict(X_TESTSobol2_ALL)
    Y_3predictionSobol2_ALL = model3Sobol2.predict(X_TESTSobol2_ALL)
    Y_4predictionSobol2_ALL = model4Sobol2.predict(X_TESTSobol2_ALL)
    
    rmse12961 = np.sqrt(mean_squared_error(Y_TEST1296, Y_1prediction1296))
    rmse12962 = np.sqrt(mean_squared_error(Y_TEST1296, Y_2prediction1296))
    rmse12963 = np.sqrt(mean_squared_error(Y_TEST1296, Y_3prediction1296))
    rmse12964 = np.sqrt(mean_squared_error(Y_TEST1296, Y_4prediction1296))
    mape12961 = skmape(Y_TEST1296, Y_1prediction1296)
    mape12962 = skmape(Y_TEST1296, Y_2prediction1296)
    mape12963 = skmape(Y_TEST1296, Y_3prediction1296)
    mape12964 = skmape(Y_TEST1296, Y_4prediction1296)
    r212961 = r2_score(Y_TEST1296, Y_1prediction1296)
    r212962 = r2_score(Y_TEST1296, Y_2prediction1296)
    r212963 = r2_score(Y_TEST1296, Y_3prediction1296)
    r212964 = r2_score(Y_TEST1296, Y_4prediction1296)
    rmse12961_ALL = np.sqrt(mean_squared_error(Y_TEST1296_ALL, Y_1prediction1296_ALL))
    rmse12962_ALL = np.sqrt(mean_squared_error(Y_TEST1296_ALL, Y_2prediction1296_ALL))
    rmse12963_ALL = np.sqrt(mean_squared_error(Y_TEST1296_ALL, Y_3prediction1296_ALL))
    rmse12964_ALL = np.sqrt(mean_squared_error(Y_TEST1296_ALL, Y_4prediction1296_ALL))
    mape12961_ALL = skmape(Y_TEST1296_ALL, Y_1prediction1296_ALL)
    mape12962_ALL = skmape(Y_TEST1296_ALL, Y_2prediction1296_ALL)
    mape12963_ALL = skmape(Y_TEST1296_ALL, Y_3prediction1296_ALL)
    mape12964_ALL = skmape(Y_TEST1296_ALL, Y_4prediction1296_ALL)
    r212961_ALL = r2_score(Y_TEST1296_ALL, Y_1prediction1296_ALL)
    r212962_ALL = r2_score(Y_TEST1296_ALL, Y_2prediction1296_ALL)
    r212963_ALL = r2_score(Y_TEST1296_ALL, Y_3prediction1296_ALL)
    r212964_ALL = r2_score(Y_TEST1296_ALL, Y_4prediction1296_ALL)
      
    rmse24011 = np.sqrt(mean_squared_error(Y_TEST2401, Y_1prediction2401))
    rmse24012 = np.sqrt(mean_squared_error(Y_TEST2401, Y_2prediction2401))
    rmse24013 = np.sqrt(mean_squared_error(Y_TEST2401, Y_3prediction2401))
    rmse24014 = np.sqrt(mean_squared_error(Y_TEST2401, Y_4prediction2401))
    mape24011 = skmape(Y_TEST2401, Y_1prediction2401)
    mape24012 = skmape(Y_TEST2401, Y_2prediction2401)
    mape24013 = skmape(Y_TEST2401, Y_3prediction2401)
    mape24014 = skmape(Y_TEST2401, Y_4prediction2401)
    r224011 = r2_score(Y_TEST2401, Y_1prediction2401)
    r224012 = r2_score(Y_TEST2401, Y_2prediction2401)
    r224013 = r2_score(Y_TEST2401, Y_3prediction2401)
    r224014 = r2_score(Y_TEST2401, Y_4prediction2401)
    rmse24011_ALL = np.sqrt(mean_squared_error(Y_TEST2401_ALL, Y_1prediction2401_ALL))
    rmse24012_ALL = np.sqrt(mean_squared_error(Y_TEST2401_ALL, Y_2prediction2401_ALL))
    rmse24013_ALL = np.sqrt(mean_squared_error(Y_TEST2401_ALL, Y_3prediction2401_ALL))
    rmse24014_ALL = np.sqrt(mean_squared_error(Y_TEST2401_ALL, Y_4prediction2401_ALL))
    mape24011_ALL = skmape(Y_TEST2401_ALL, Y_1prediction2401_ALL)
    mape24012_ALL = skmape(Y_TEST2401_ALL, Y_2prediction2401_ALL)
    mape24013_ALL = skmape(Y_TEST2401_ALL, Y_3prediction2401_ALL)
    mape24014_ALL = skmape(Y_TEST2401_ALL, Y_4prediction2401_ALL)
    r224011_ALL = r2_score(Y_TEST2401_ALL, Y_1prediction2401_ALL)
    r224012_ALL = r2_score(Y_TEST2401_ALL, Y_2prediction2401_ALL)
    r224013_ALL = r2_score(Y_TEST2401_ALL, Y_3prediction2401_ALL)
    r224014_ALL = r2_score(Y_TEST2401_ALL, Y_4prediction2401_ALL)
    
    rmseSobol11 = np.sqrt(mean_squared_error(Y_TESTSobol1, Y_1predictionSobol1))
    rmseSobol12 = np.sqrt(mean_squared_error(Y_TESTSobol1, Y_2predictionSobol1))
    rmseSobol13 = np.sqrt(mean_squared_error(Y_TESTSobol1, Y_3predictionSobol1))
    rmseSobol14 = np.sqrt(mean_squared_error(Y_TESTSobol1, Y_4predictionSobol1))
    mapeSobol11 = skmape(Y_TESTSobol1, Y_1predictionSobol1)
    mapeSobol12 = skmape(Y_TESTSobol1, Y_2predictionSobol1)
    mapeSobol13 = skmape(Y_TESTSobol1, Y_3predictionSobol1)
    mapeSobol14 = skmape(Y_TESTSobol1, Y_4predictionSobol1)
    r2Sobol11 = r2_score(Y_TESTSobol1, Y_1predictionSobol1)
    r2Sobol12 = r2_score(Y_TESTSobol1, Y_2predictionSobol1)
    r2Sobol13 = r2_score(Y_TESTSobol1, Y_3predictionSobol1)
    r2Sobol14 = r2_score(Y_TESTSobol1, Y_4predictionSobol1)
    rmseSobol11_ALL = np.sqrt(mean_squared_error(Y_TESTSobol1_ALL, Y_1predictionSobol1_ALL))
    rmseSobol12_ALL = np.sqrt(mean_squared_error(Y_TESTSobol1_ALL, Y_2predictionSobol1_ALL))
    rmseSobol13_ALL = np.sqrt(mean_squared_error(Y_TESTSobol1_ALL, Y_3predictionSobol1_ALL))
    rmseSobol14_ALL = np.sqrt(mean_squared_error(Y_TESTSobol1_ALL, Y_4predictionSobol1_ALL))
    mapeSobol11_ALL = skmape(Y_TESTSobol1_ALL, Y_1predictionSobol1_ALL)
    mapeSobol12_ALL = skmape(Y_TESTSobol1_ALL, Y_2predictionSobol1_ALL)
    mapeSobol13_ALL = skmape(Y_TESTSobol1_ALL, Y_3predictionSobol1_ALL)
    mapeSobol14_ALL = skmape(Y_TESTSobol1_ALL, Y_4predictionSobol1_ALL)
    r2Sobol11_ALL = r2_score(Y_TESTSobol1_ALL, Y_1predictionSobol1_ALL)
    r2Sobol12_ALL = r2_score(Y_TESTSobol1_ALL, Y_2predictionSobol1_ALL)
    r2Sobol13_ALL = r2_score(Y_TESTSobol1_ALL, Y_3predictionSobol1_ALL)
    r2Sobol14_ALL = r2_score(Y_TESTSobol1_ALL, Y_4predictionSobol1_ALL)
      
    rmseSobol21 = np.sqrt(mean_squared_error(Y_TESTSobol2, Y_1predictionSobol2))
    rmseSobol22 = np.sqrt(mean_squared_error(Y_TESTSobol2, Y_2predictionSobol2))
    rmseSobol23 = np.sqrt(mean_squared_error(Y_TESTSobol2, Y_3predictionSobol2))
    rmseSobol24 = np.sqrt(mean_squared_error(Y_TESTSobol2, Y_4predictionSobol2))
    mapeSobol21 = skmape(Y_TESTSobol2, Y_1predictionSobol2)
    mapeSobol22 = skmape(Y_TESTSobol2, Y_2predictionSobol2)
    mapeSobol23 = skmape(Y_TESTSobol2, Y_3predictionSobol2)
    mapeSobol24 = skmape(Y_TESTSobol2, Y_4predictionSobol2)
    r2Sobol21 = r2_score(Y_TESTSobol2, Y_1predictionSobol2)
    r2Sobol22 = r2_score(Y_TESTSobol2, Y_2predictionSobol2)
    r2Sobol23 = r2_score(Y_TESTSobol2, Y_3predictionSobol2)
    r2Sobol24 = r2_score(Y_TESTSobol2, Y_4predictionSobol2)
    rmseSobol21_ALL = np.sqrt(mean_squared_error(Y_TESTSobol2_ALL, Y_1predictionSobol2_ALL))
    rmseSobol22_ALL = np.sqrt(mean_squared_error(Y_TESTSobol2_ALL, Y_2predictionSobol2_ALL))
    rmseSobol23_ALL = np.sqrt(mean_squared_error(Y_TESTSobol2_ALL, Y_3predictionSobol2_ALL))
    rmseSobol24_ALL = np.sqrt(mean_squared_error(Y_TESTSobol2_ALL, Y_4predictionSobol2_ALL))
    mapeSobol21_ALL = skmape(Y_TESTSobol2_ALL, Y_1predictionSobol2_ALL)
    mapeSobol22_ALL = skmape(Y_TESTSobol2_ALL, Y_2predictionSobol2_ALL)
    mapeSobol23_ALL = skmape(Y_TESTSobol2_ALL, Y_3predictionSobol2_ALL)
    mapeSobol24_ALL = skmape(Y_TESTSobol2_ALL, Y_4predictionSobol2_ALL)
    r2Sobol21_ALL = r2_score(Y_TESTSobol2_ALL, Y_1predictionSobol2_ALL)
    r2Sobol22_ALL = r2_score(Y_TESTSobol2_ALL, Y_2predictionSobol2_ALL)
    r2Sobol23_ALL = r2_score(Y_TESTSobol2_ALL, Y_3predictionSobol2_ALL)
    r2Sobol24_ALL = r2_score(Y_TESTSobol2_ALL, Y_4predictionSobol2_ALL)
    
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Grid1296"],
                            "kernel": ["RBF"],
                            "length_scale": [model1Grid1296.kernel.length_scale],
                            "nu": ["-"],
                            "alpha": ["-"],
                            "periodicity": ["-"],
                            "rmse": [rmse12961],
                            "mape": [mape12961],
                            "r2": [r212961],
                            "rmse_all": [rmse12961_ALL],
                            "mape_all": [mape12961_ALL],
                            "r2_all": [r212961_ALL]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Grid1296"],
                            "kernel": ["Matern"],
                            "length_scale": [model2Grid1296.kernel.length_scale],
                            "nu": [model2Grid1296.kernel.nu],
                            "alpha": ["-"],
                            "periodicity": ["-"],
                            "rmse": [rmse12962],
                            "mape": [mape12962],
                            "r2": [r212962],
                            "rmse_all": [rmse12962_ALL],
                            "mape_all": [mape12962_ALL],
                            "r2_all": [r212962_ALL]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Grid1296"],
                            "kernel": ["RQ"],
                            "length_scale": [model3Grid1296.kernel.length_scale],
                            "nu": ["-"],
                            "alpha": [model3Grid1296.kernel.alpha],
                            "periodicity": ["-"],
                            "rmse": [rmse12963],
                            "mape": [mape12963],
                            "r2": [r212963],
                            "rmse_all": [rmse12963_ALL],
                            "mape_all": [mape12963_ALL],
                            "r2_all": [r212963_ALL]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Grid1296"],
                            "kernel": ["ESS"],
                            "length_scale": [model4Grid1296.kernel.length_scale],
                            "nu": ["-"],
                            "alpha": ["-"],
                            "periodicity": [model4Grid1296.kernel.periodicity],
                            "rmse": [rmse12964],
                            "mape": [mape12964],
                            "r2": [r212964],
                            "rmse_all": [rmse12964_ALL],
                            "mape_all": [mape12964_ALL],
                            "r2_all": [r212964_ALL]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    #
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Grid2401"],
                            "kernel": ["RBF"],
                            "length_scale": [model1Grid2401.kernel.length_scale],
                            "nu": ["-"],
                            "alpha": ["-"],
                            "periodicity": ["-"],
                            "rmse": [rmse24011],
                            "mape": [mape24011],
                            "r2": [r224011],
                            "rmse_all": [rmse24011_ALL],
                            "mape_all": [mape24011_ALL],
                            "r2_all": [r224011_ALL]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Grid2401"],
                            "kernel": ["Matern"],
                            "length_scale": [model2Grid2401.kernel.length_scale],
                            "nu": [model2Grid2401.kernel.nu],
                            "alpha": ["-"],
                            "periodicity": ["-"],
                            "rmse": [rmse24012],
                            "mape": [mape24012],
                            "r2": [r224012],
                            "rmse_all": [rmse24012_ALL],
                            "mape_all": [mape24012_ALL],
                            "r2_all": [r224012_ALL]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Grid2401"],
                            "kernel": ["RQ"],
                            "length_scale": [model3Grid2401.kernel.length_scale],
                            "nu": ["-"],
                            "alpha": [model3Grid2401.kernel.alpha],
                            "periodicity": ["-"],
                            "rmse": [rmse24013],
                            "mape": [mape24013],
                            "r2": [r224013],
                            "rmse_all": [rmse24013_ALL],
                            "mape_all": [mape24013_ALL],
                            "r2_all": [r224013_ALL]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Grid2401"],
                            "kernel": ["ESS"],
                            "length_scale": [model4Grid2401.kernel.length_scale],
                            "nu": ["-"],
                            "alpha": ["-"],
                            "periodicity": [model4Grid2401.kernel.periodicity],
                            "rmse": [rmse24014],
                            "mape": [mape24014],
                            "r2": [r224014],
                            "rmse_all": [rmse24014_ALL],
                            "mape_all": [mape24014_ALL],
                            "r2_all": [r224014_ALL]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    #
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Sobol1"],
                            "kernel": ["RBF"],
                            "length_scale": [model1Sobol1.kernel.length_scale],
                            "nu": ["-"],
                            "alpha": ["-"],
                            "periodicity": ["-"],
                            "rmse": [rmseSobol11],
                            "mape": [mapeSobol11],
                            "r2": [r2Sobol11],
                            "rmse_all": [rmseSobol11_ALL],
                            "mape_all": [mapeSobol11_ALL],
                            "r2_all": [r2Sobol11_ALL]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Sobol1"],
                            "kernel": ["Matern"],
                            "length_scale": [model2Sobol1.kernel.length_scale],
                            "nu": [model2Sobol1.kernel.nu],
                            "alpha": ["-"],
                            "periodicity": ["-"],
                            "rmse": [rmseSobol12],
                            "mape": [mapeSobol12],
                            "r2": [r2Sobol12],
                            "rmse_all": [rmseSobol12_ALL],
                            "mape_all": [mapeSobol12_ALL],
                            "r2_all": [r2Sobol12_ALL]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Sobol1"],
                            "kernel": ["RQ"],
                            "length_scale": [model3Sobol1.kernel.length_scale],
                            "nu": ["-"],
                            "alpha": [model3Sobol1.kernel.alpha],
                            "periodicity": ["-"],
                            "rmse": [rmseSobol13],
                            "mape": [mapeSobol13],
                            "r2": [r2Sobol13],
                            "rmse_all": [rmseSobol13_ALL],
                            "mape_all": [mapeSobol13_ALL],
                            "r2_all": [r2Sobol13_ALL]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Sobol1"],
                            "kernel": ["ESS"],
                            "length_scale": [model4Sobol1.kernel.length_scale],
                            "nu": ["-"],
                            "alpha": ["-"],
                            "periodicity": [model4Sobol1.kernel.periodicity],
                            "rmse": [rmseSobol14],
                            "mape": [mapeSobol14],
                            "r2": [r2Sobol14],
                            "rmse_all": [rmseSobol14_ALL],
                            "mape_all": [mapeSobol14_ALL],
                            "r2_all": [r2Sobol14_ALL]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    #
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Sobol2"],
                            "kernel": ["RBF"],
                            "length_scale": [model1Sobol2.kernel.length_scale],
                            "nu": ["-"],
                            "alpha": ["-"],
                            "periodicity": ["-"],
                            "rmse": [rmseSobol21],
                            "mape": [mapeSobol21],
                            "r2": [r2Sobol21],
                            "rmse_all": [rmseSobol21_ALL],
                            "mape_all": [mapeSobol21_ALL],
                            "r2_all": [r2Sobol21_ALL]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Sobol2"],
                            "kernel": ["Matern"],
                            "length_scale": [model2Sobol2.kernel.length_scale],
                            "nu": [model2Sobol2.kernel.nu],
                            "alpha": ["-"],
                            "periodicity": ["-"],
                            "rmse": [rmseSobol22],
                            "mape": [mapeSobol22],
                            "r2": [r2Sobol22],
                            "rmse_all": [rmseSobol22_ALL],
                            "mape_all": [mapeSobol22_ALL],
                            "r2_all": [r2Sobol22_ALL]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Sobol2"],
                            "kernel": ["RQ"],
                            "length_scale": [model3Sobol2.kernel.length_scale],
                            "nu": ["-"],
                            "alpha": [model3Sobol2.kernel.alpha],
                            "periodicity": ["-"],
                            "rmse": [rmseSobol23],
                            "mape": [mapeSobol23],
                            "r2": [r2Sobol23],
                            "rmse_all": [rmseSobol23_ALL],
                            "mape_all": [mapeSobol23_ALL],
                            "r2_all": [r2Sobol23_ALL]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": ["Sobol2"],
                            "kernel": ["ESS"],
                            "length_scale": [model4Sobol2.kernel.length_scale],
                            "nu": ["-"],
                            "alpha": ["-"],
                            "periodicity": [model4Sobol2.kernel.periodicity],
                            "rmse": [rmseSobol24],
                            "mape": [mapeSobol24],
                            "r2": [r2Sobol24],
                            "rmse_all": [rmseSobol24_ALL],
                            "mape_all": [mapeSobol24_ALL],
                            "r2_all": [r2Sobol24_ALL]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)

  print(f'\n')
  os.chdir(cwd)

os.chdir(pwd)
if os.path.exists(statisticsFileName):
  os.remove(statisticsFileName)
  print(f'Removed existing statistics file: \'{statisticsFileName}\'.')
dfStatistics.to_csv(statisticsFileName)
print(f'Wrote statistics to file: \'{statisticsFileName}\'.')
print(f'{dfStatistics}')










