import pandas as pd
import os
import shutil
import matplotlib.pyplot as plt
import sys
import numpy as np

try:
  saveOrShow = sys.argv[1]
except:
  saveOrShow = "show"
if saveOrShow == "save":
  pass
else:
  saveOrShow = "show"

statisticsFiles = ['02.1_Stats.csv', '02.2_Stats.csv', '02.3_Stats.csv', '02.4_Stats.csv', '02.5_Stats.csv']
MethodName = ['Lin. Regr.', 'Polyn. Regr.', 'RF Regr.', 'GP Regr.', 'NN Perceptron']
sumMethods = ['Polyn. Regr.', 'RF Regr.', 'GP Regr.', 'NN Perceptron']
colors = ['#f781bf', '#377eb8', '#ff7f00', '#984ea3', '#4daf4a']

top = 500
minMETRIC1 = 0.00
maxMETRIC1 = 0.13
minMETRIC2 = 0.35
maxMETRIC2 = 1.05
minMETRIC1sum = 0.012
maxMETRIC1sum = 0.019
minMETRIC2sum = 0.90
maxMETRIC2sum = 0.98
mark1 = 'x'
mark2 = 'o'
                               
minMAPEMAPE = []
minMAPER2 = []
maxR2MAPE = []
maxR2R2 = []

minMAPEMAPEInterp = []
minMAPER2Interp = []
maxR2MAPEInterp = []
maxR2R2Interp = []
for nMethod in range(0, len(statisticsFiles)):
  thisMinMAPEMAPE = []
  thisMinMAPER2 = []
  thisMaxR2MAPE = []
  thisMaxR2R2 = []
  
  thisMinMAPEMAPEInterp = []
  thisMinMAPER2Interp = []
  thisMaxR2MAPEInterp = []
  thisMaxR2R2Interp = []
  
  statisticsFile = statisticsFiles[nMethod]
  topStatisticsFile = f'{statisticsFile.split(".csv")[0]}Top{top}.csv'
  #print(f'{topStatisticsFile}')

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

  ## min MAPE
  dfThisStatistics = dfStatistics
  minMapeIDXs = []

  dfTopModels = pd.DataFrame({"ratio": [],
                              "rndint": [],
                              "dataset": [],
                              "mape_test": [],
                              "r2_test": [],
                              "mape_interpolation": [],
                              "r2_interpolation": []})
                             
  thisTop = 0
  isLabeled = False
  #print(f'MinMAPE Models:')
  while True:
    idxMinMAPE = dfThisStatistics['mape_test'].idxmin()
    #print(f'{idxMinMAPE}')
    #minMAPE = dfThisStatistics['mape_test'].min()
    #print(f'{minMAPE}')
    minMAPERow = dfThisStatistics.loc[idxMinMAPE]
    #print(f'Min MAPE Entry:\n{minMAPERow}\n')
    dfThisStatistics = dfThisStatistics.drop([idxMinMAPE]) 
    if minMAPERow.dataset == "Grid1296" or minMAPERow.dataset == "Grid2401":
      #print(f'would have been Grid1296 or Grid2401')
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
                                     "mape_test": [minMAPERow.mape_test],
                                     "r2_test": [minMAPERow.r2_test],
                                     "mape_interpolation": [minMAPERow.mape_interpolation],
                                     "r2_interpolation": [minMAPERow.r2_interpolation]})
      dfTopModels = pd.concat([dfTopModels, dfThisTopModel], ignore_index=True)
      
      thisMinMAPEMAPE.append(minMAPERow.mape_test)
      thisMinMAPER2.append(minMAPERow.r2_test)
      thisMinMAPEMAPEInterp.append(minMAPERow.mape_interpolation)
      thisMinMAPER2Interp.append(minMAPERow.r2_interpolation)
      
#      if not isLabeled:
#        isLabeled = True
#        axd["minMax"].scatter(minMAPERow.mape_test, minMAPERow.r2_test, label=f'{MethodName[nMethod]}, minMAPE', c=colors[nMethod], marker=mark1)#, edgecolor="#44AA99")
#        if MethodName[nMethod] in sumMethods:
#          axd["minMaxInterpRed"].scatter(minMAPERow.mape_interpolation, minMAPERow.r2_interpolation, label=f'{MethodName[nMethod]}, minMAPE, interpol. test', c=colors[nMethod], marker=mark1)
#      else:
#        axd["minMax"].scatter(minMAPERow.mape_test, minMAPERow.r2_test, c=colors[nMethod], marker=mark1)#, edgecolor="#44AA99")
#        if MethodName[nMethod] in sumMethods:
#          axd["minMaxInterpRed"].scatter(minMAPERow.mape_interpolation, minMAPERow.r2_interpolation, c=colors[nMethod], marker=mark1)
    
      thisTop = thisTop + 1
      if thisTop == top:
        #print(f'')
        break
  minMAPEMAPE.append(thisMinMAPEMAPE)
  minMAPER2.append(thisMinMAPER2)
  minMAPEMAPEInterp.append(thisMinMAPEMAPEInterp)
  minMAPER2Interp.append(thisMinMAPER2Interp)
  
  ## max R2
  dfThisStatistics = dfStatistics
  maxR2IDXs = []

  thisTop = 0
  thisSkipped = 0
  isLabeled = False
  #print(f'MaxR2 Models, {MethodName[nMethod]}:')
  while True:
    idxMaxR2 = dfThisStatistics['r2_test'].idxmax()
    #print(f'{idxMaxR2}')
    #maxR2 = dfThisStatistics['r2_test'].max()
    #print(f'{maxR2}')
    maxR2Row = dfThisStatistics.loc[idxMaxR2]
    #print(f'Max R2 Entry:\n{maxR2Row}\n')
    dfThisStatistics = dfThisStatistics.drop([idxMaxR2])
    if maxR2Row.dataset == "Grid1296" or maxR2Row.dataset == "Grid2401":
      #print(f'  would have been Grid1296 or Grid2401')
      pass
    elif idxMaxR2 in minMapeIDXs:
      #print(f'  {idxMaxR2} already in minMapeIDXs. Skipped.')
      thisSkipped = thisSkipped + 1
      thisTop = thisTop + 1
      #pass
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
                                     "mape_test": [maxR2Row.mape_test],
                                     "r2_test": [maxR2Row.r2_test],
                                     "mape_interpolation": [maxR2Row.mape_interpolation],
                                     "r2_interpolation": [maxR2Row.r2_interpolation]})
      dfTopModels = pd.concat([dfTopModels, dfThisTopModel], ignore_index=True)
      
      thisMaxR2MAPE.append(maxR2Row.mape_test)
      thisMaxR2R2.append(maxR2Row.r2_test)
      thisMaxR2MAPEInterp.append(maxR2Row.mape_interpolation)
      thisMaxR2R2Interp.append(maxR2Row.r2_interpolation)
      
#      if not isLabeled:
#        isLabeled = True
#        axd["minMax"].scatter(maxR2Row.mape_test, maxR2Row.r2_test, label=f'{MethodName[nMethod]}, maxR²', c=colors[nMethod], marker=mark2)#, edgecolor="#44AA99")
#        if MethodName[nMethod] in sumMethods:
#          axd["minMaxInterpRed"].scatter(maxR2Row.mape_interpolation, maxR2Row.r2_interpolation, label=f'{MethodName[nMethod]}, maxR², interpol. test', c=colors[nMethod], marker=mark2)
#      else:
#        axd["minMax"].scatter(maxR2Row.mape_test, maxR2Row.r2_test, c=colors[nMethod], marker=mark2)#, edgecolor="#44AA99")
#        if MethodName[nMethod] in sumMethods:
#          axd["minMaxInterpRed"].scatter(maxR2Row.mape_interpolation, maxR2Row.r2_interpolation, c=colors[nMethod], marker=mark2)
    
      thisTop = thisTop + 1
    if thisTop == top:
      print(f'{MethodName[nMethod]}: number of models in minMAPE & maxR²: {thisSkipped}')
      break
 
  maxR2MAPE.append(thisMaxR2MAPE)
  maxR2R2.append(thisMaxR2R2)
  maxR2MAPEInterp.append(thisMaxR2MAPEInterp)
  maxR2R2Interp.append(thisMaxR2R2Interp)
  
  #print(f'{minMapeIDXs}')
  if saveOrShow == "save":
    if os.path.exists(topStatisticsFile):
      os.remove(topStatisticsFile)
      print(f'Removed existing top{top} statistics file: \'{topStatisticsFile}\'.')
    dfTopModels.to_csv(topStatisticsFile)
    print(f'Wrote statistics to file: \'{topStatisticsFile}\'.')
  #print(f'{dfTopModels}')
   

gs_kw = dict(width_ratios=[1, 1], height_ratios=[1])
fig, axd = plt.subplot_mosaic([['minMax', 'minMaxInterpRed']],
                               gridspec_kw=gs_kw, figsize=(10.0, 5.0))

for nMethod in range(0, len(MethodName)):
  axd["minMax"].scatter(minMAPEMAPE[nMethod], minMAPER2[nMethod], label=f'{MethodName[nMethod]}, minMAPE', c=colors[nMethod], marker=mark1)
  axd["minMax"].scatter(maxR2MAPE[nMethod], maxR2R2[nMethod], label=f'{MethodName[nMethod]}, maxR²', c=colors[nMethod], marker=mark2)
  if MethodName[nMethod] in sumMethods:
    axd["minMaxInterpRed"].scatter(minMAPEMAPEInterp[nMethod], minMAPER2Interp[nMethod], label=f'{MethodName[nMethod]}, minMAPE, interpol. test', c=colors[nMethod], marker=mark1)
    axd["minMaxInterpRed"].scatter(maxR2MAPEInterp[nMethod], maxR2R2Interp[nMethod], label=f'{MethodName[nMethod]}, maxR², interpol. test', c=colors[nMethod], marker=mark2)
    

axd["minMax"].legend()
axd["minMax"].set_xlabel(f'MAPE', fontweight='bold')
axd["minMax"].set_ylabel(f'R²', fontweight='bold')
axd["minMax"].set_title(f'Testdata: from same dataset')#, fontweight='bold')
axd["minMax"].set_xlim([minMETRIC1, maxMETRIC1])
axd["minMax"].set_ylim([minMETRIC2, maxMETRIC2])

axd["minMaxInterpRed"].legend()
axd["minMaxInterpRed"].set_xlabel(f'MAPE', fontweight='bold')
#axd["minMaxInterpRed"].set_ylabel(f'R²', fontweight='bold')
axd["minMaxInterpRed"].set_title(f'Testdata: all other datasets added')#, fontweight='bold')
axd["minMaxInterpRed"].set_xlim([minMETRIC1sum, maxMETRIC1sum])
axd["minMaxInterpRed"].set_ylim([minMETRIC2sum, maxMETRIC2sum])

plt.tight_layout()
if saveOrShow == "save":
  plt.savefig(f'top{top}Models_MAPE-vs-R2_interpRed.png', dpi=100, format='png') 
  
plt.figure()
for nMethod in range(0, len(MethodName)):
  plt.scatter(minMAPEMAPEInterp[nMethod], minMAPER2Interp[nMethod], label=f'{MethodName[nMethod]}, minMAPE, interpol. test', c=colors[nMethod], marker=mark1)
  plt.scatter(maxR2MAPEInterp[nMethod], maxR2R2Interp[nMethod], label=f'{MethodName[nMethod]}, maxR², interpol. test', c=colors[nMethod], marker=mark2)

plt.legend()
plt.xlabel(f'MAPE', fontweight='bold')
plt.ylabel(f'R²', fontweight='bold')
plt.title(f'Testdata: all other datasets added')#, fontweight='bold')
plt.xlim([minMETRIC1, maxMETRIC1])
plt.ylim([minMETRIC2, maxMETRIC2])
plt.tight_layout()
if saveOrShow == "save":
  plt.savefig(f'top{top}Models_MAPE-vs-R2_interpAll.png', dpi=100, format='png')    

if saveOrShow == "show":
  plt.show()

    
    
    
    
    
    
    

