import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import os
import glob
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
metric1 = "mape"
metric2 = "r2"

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



if metric1 is "rmse":
  metric1All = "rmse_interpolation"
  metric1 = "rmse_test"
  xLabel = "RMSE"
  #xLabelAll = "RMSE_ALL"
  minMETRIC1 = dfStatistics[f'{metric1}'].min()
  minMETRIC1 = minMETRIC1 - 0.01*minMETRIC1
  minMETRIC1All = dfStatistics[f'{metric1All}'].min()
  minMETRIC1All = minMETRIC1All - 0.01*minMETRIC1All
  minMETRIC1 = min(minMETRIC1, minMETRIC1All)
  #maxMETRIC1 = 100
  maxMETRIC1 = dfStatistics[f'{metric1}'].max()
  maxMETRIC1 = maxMETRIC1 + 0.01*maxMETRIC1
  maxMETRIC1All = dfStatistics[f'{metric1All}'].max()
  maxMETRIC1All = maxMETRIC1All + 0.01*maxMETRIC1All
  maxMETRIC1 = max(maxMETRIC1, maxMETRIC1All)
elif metric1 is "mape":
  metric1All = "mape_interpolation"
  metric1 = "mape_test"
  xLabel = "MAPE"
  #xLabelAll = "MAPE_ALL"
  minMETRIC1 = dfStatistics[f'{metric1}'].min()
  minMETRIC1 = minMETRIC1 - 0.01*minMETRIC1
  minMETRIC1All = dfStatistics[f'{metric1All}'].min()
  minMETRIC1All = minMETRIC1All - 0.01*minMETRIC1All
  minMETRIC1 = min(minMETRIC1, minMETRIC1All)
  maxMETRIC1 = dfStatistics[f'{metric1}'].max()
  maxMETRIC1 = maxMETRIC1 + 0.01*maxMETRIC1
  maxMETRIC1All = dfStatistics[f'{metric1All}'].max()
  maxMETRIC1All = maxMETRIC1All + 0.01*maxMETRIC1All
  maxMETRIC1 = max(maxMETRIC1, maxMETRIC1All)
  maxMETRIC1 = 0.16 
  minMETRIC1 = 0.00 
elif metric1 is "r2":
  metric1All = "r2_interpolation"
  metric1 = "r2_test"
  xLabel = "R²"
  #xLabelAll = "R2_ALL"
  maxMETRIC1 = 1.05
  minMETRIC1 = -1.05
else:
  print(f'Please set \'metric1\' to "rmse", "r2" or "mape". (Is: {metric1}). Exit.')
  exit()
  
if metric2 is "rmse":
  metric2All = "rmse_interpolation"
  metric2 = "rmse_test"
  yLabel = "RMSE"
  #yLabelAll = "RMSE_ALL"
  minMETRIC2 = dfStatistics[f'{metric2}'].min()
  minMETRIC2 = minMETRIC2 - 0.01*minMETRIC2
  minMETRIC2All = dfStatistics[f'{metric2All}'].min()
  minMETRIC2All = minMETRIC2All - 0.01*minMETRIC2All
  minMETRIC2 = min(minMETRIC2, minMETRIC2All)
  #maxMETRIC2 = 100
  maxMETRIC2 = dfStatistics[f'{metric2}'].max()
  maxMETRIC2 = maxMETRIC2 + 0.01*maxMETRIC2
  maxMETRIC2All = dfStatistics[f'{metric2All}'].max()
  maxMETRIC2All = maxMETRIC2All + 0.01*maxMETRIC2All
  maxMETRIC2 = max(maxMETRIC2, maxMETRIC2All)
elif metric2 is "mape":
  metric2All = "mape_interpolation"
  metric2 = "mape_test"
  yLabel = "MAPE"
  #yLabelAll = "MAPE_ALL"
  minMETRIC2 = dfStatistics[f'{metric2}'].min()
  minMETRIC2 = minMETRIC2 - 0.01*minMETRIC2
  minMETRIC2All = dfStatistics[f'{metric2All}'].min()
  minMETRIC2All = minMETRIC2All - 0.01*minMETRIC2All
  minMETRIC2 = min(minMETRIC2, minMETRIC2All)
  maxMETRIC2 = dfStatistics[f'{metric2}'].max()
  maxMETRIC2 = maxMETRIC2 + 0.01*maxMETRIC2
  maxMETRIC2All = dfStatistics[f'{metric2All}'].max()
  maxMETRIC2All = maxMETRIC2All + 0.01*maxMETRIC2All
  maxMETRIC2 = max(maxMETRIC2, maxMETRIC2All)
  maxMETRIC2 = 0.13
elif metric2 is "r2":
  metric2All = "r2_interpolation"
  metric2 = "r2_test"
  yLabel = "R²"
  #yLabelAll = "R2_ALL"
  maxMETRIC2 = 1.25
  minMETRIC2 = -5.05
else:
  print(f'Please set \'metric2\' to "rmse", "r2" or "mape". (Is: {metric2}). Exit.')
  exit()

subsetGrid1296 = dfStatistics[dfStatistics["dataset"] == "Grid1296"]
subsetGrid2401 = dfStatistics[dfStatistics["dataset"] == "Grid2401"]
subsetSobol1 = dfStatistics[dfStatistics["dataset"] == "Sobol1"]
subsetSobol2 = dfStatistics[dfStatistics["dataset"] == "Sobol2"]

if False:
  print(f'Grid1296')
  print(
      f'& {np.round(np.mean(subsetGrid1296["mape_test"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetGrid1296["mape_test"].to_numpy()), 4):.5f} & '
      f'{np.round(np.mean(subsetGrid1296["r2_test"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetGrid1296["r2_test"].to_numpy()), 4):.5f} \\\\'
  )
  print('')
  print(f'Grid2401')
  print(
      f'& {np.round(np.mean(subsetGrid2401["mape_test"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetGrid2401["mape_test"].to_numpy()), 4):.5f} & '
      f'{np.round(np.mean(subsetGrid2401["r2_test"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetGrid2401["r2_test"].to_numpy()), 4):.5f} \\\\'
  )
  print('')
  print(f'Sobol1')
  print(
      f'& {np.round(np.mean(subsetSobol1["mape_test"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetSobol1["mape_test"].to_numpy()), 4):.5f} & '
      f'{np.round(np.mean(subsetSobol1["r2_test"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetSobol1["r2_test"].to_numpy()), 4):.5f} \\\\'
  )
  print('')
  print(f'Sobol2')
  print(
      f'& {np.round(np.mean(subsetSobol2["mape_test"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetSobol2["mape_test"].to_numpy()), 4):.5f} & '
      f'{np.round(np.mean(subsetSobol2["r2_test"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetSobol2["r2_test"].to_numpy()), 4):.5f} \\\\'
  )
  print('')
  
if False:
  print(f'Grid1296')
  print(
      f'& {np.round(np.mean(subsetGrid1296["mape_interpolation"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetGrid1296["mape_interpolation"].to_numpy()), 4):.5f} & '
      f'{np.round(np.mean(subsetGrid1296["r2_interpolation"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetGrid1296["r2_interpolation"].to_numpy()), 4):.5f} \\\\'
  )
  print('')
  print(f'Grid2401')
  print(
      f'& {np.round(np.mean(subsetGrid2401["mape_interpolation"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetGrid2401["mape_interpolation"].to_numpy()), 4):.5f} & '
      f'{np.round(np.mean(subsetGrid2401["r2_interpolation"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetGrid2401["r2_interpolation"].to_numpy()), 4):.5f} \\\\'
  )
  print('')
  print(f'Sobol1')
  print(
      f'& {np.round(np.mean(subsetSobol1["mape_interpolation"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetSobol1["mape_interpolation"].to_numpy()), 4):.5f} & '
      f'{np.round(np.mean(subsetSobol1["r2_interpolation"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetSobol1["r2_interpolation"].to_numpy()), 4):.5f} \\\\'
  )
  print('')
  print(f'Sobol2')
  print(
      f'& {np.round(np.mean(subsetSobol2["mape_interpolation"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetSobol2["mape_interpolation"].to_numpy()), 4):.5f} & '
      f'{np.round(np.mean(subsetSobol2["r2_interpolation"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetSobol2["r2_interpolation"].to_numpy()), 4):.5f} \\\\'
  )
  print('')
  exit()


## plots

datasetSubsets = [subsetGrid1296, subsetGrid2401, subsetSobol1, subsetSobol2]
#print(f'{datasetSubsets[0]}')
colors = ['#377eb8', '#ff7f00', '#4daf4a', '#f781bf', '#a65628', '#984ea3', '#999999', '#e41a1c', '#dede00']
markers = ['1', '2', '3', '4', 'x', '+']
DatasetNames = ['Grid1296', 'Grid2401', 'Sobol1', 'Sobol2']

gs_kw = dict(width_ratios=[1, 1], height_ratios=[1, 1])
fig, axd = plt.subplot_mosaic([['METRIC1', 'METRIC2'],
                               ['METRIC1ALL', 'METRIC2ALL']],  
                               gridspec_kw=gs_kw, figsize=(10.0, 10.0))

for nSubset in range(0, len(datasetSubsets)):
  #print(f'nSubset: {nSubset}')
  thisDataSubset = datasetSubsets[nSubset]
#  gs_kw = dict(width_ratios=[1, 1], height_ratios=[1, 1])
#  fig, axd = plt.subplot_mosaic([['METRIC1', 'METRIC2'],
#                                 ['METRIC1ALL', 'METRIC2ALL']],  
#                                 gridspec_kw=gs_kw, figsize=(10.0, 10.0))
  
  thisX = []
    
  thisRMSE = []
  thisRMSEerr = []
  thisR2 = []
  thisR2err = []
    
  thisRMSEAll = []
  thisRMSEerrAll = []
  thisR2All = []
  thisR2errAll = []
  
  for ratio in thisDataSubset["ratio"].unique():
    thisX.append(1-ratio)
      
    thisDataSubsetRatio = thisDataSubset[thisDataSubset["ratio"] == ratio]
      
    thisRMSE.append(np.mean(thisDataSubsetRatio[f'{metric1}'].to_numpy()))
    thisRMSEerr.append(np.std(thisDataSubsetRatio[f'{metric1}'].to_numpy()))
    thisR2.append(np.mean(thisDataSubsetRatio[f'{metric2}'].to_numpy()))
    thisR2err.append(np.std(thisDataSubsetRatio[f'{metric2}'].to_numpy()))
      
    thisRMSEAll.append(np.mean(thisDataSubsetRatio[f'{metric1All}'].to_numpy()))
    thisRMSEerrAll.append(np.std(thisDataSubsetRatio[f'{metric1All}'].to_numpy()))
    thisR2All.append(np.mean(thisDataSubsetRatio[f'{metric2All}'].to_numpy()))
    thisR2errAll.append(np.std(thisDataSubsetRatio[f'{metric2All}'].to_numpy()))
  axd['METRIC1'].errorbar(thisX, thisRMSE, yerr=thisRMSEerr, label=f'trained on: {DatasetNames[nSubset]}', marker=markers[nSubset], color=colors[nSubset], ls='-.')
  axd['METRIC2'].errorbar(thisX, thisR2, yerr=thisR2err, label=f'trained on: {DatasetNames[nSubset]}', marker=markers[nSubset], color=colors[nSubset], ls='-.')
  axd["METRIC1ALL"].errorbar(thisX, thisRMSEAll, yerr=thisRMSEerrAll, label=f'trained on: {DatasetNames[nSubset]}', marker=markers[nSubset], color=colors[nSubset], ls='-.')
  axd["METRIC2ALL"].errorbar(thisX, thisR2All, yerr=thisR2errAll, label=f'trained on: {DatasetNames[nSubset]}', marker=markers[nSubset], color=colors[nSubset], ls='-.')
   
  axd["METRIC1"].legend()
  axd["METRIC1"].set_ylabel(f'{xLabel}', fontweight='bold')
  #axd["METRIC1"].set_xlabel("% of Dataset used for Training", fontweight='bold')
  axd["METRIC1"].set_title(f'Testdata: from same dataset')#, fontweight='bold')
  axd["METRIC1"].set_ylim([minMETRIC1, maxMETRIC1])
  axd["METRIC2"].legend()
  #axd["METRIC2"].set_xlabel("% of Dataset used for Training", fontweight='bold')
  axd["METRIC2"].set_ylabel(f'{yLabel}', fontweight='bold')
  axd["METRIC2"].set_title(f'Testdata: from same dataset')#, fontweight='bold')
  axd["METRIC2"].set_ylim([minMETRIC2, maxMETRIC2])
  
  axd["METRIC1ALL"].legend()
  axd["METRIC1ALL"].set_ylabel(f'{xLabel}', fontweight='bold')
  axd["METRIC1ALL"].set_xlabel("% of Dataset used for Training", fontweight='bold')
  axd["METRIC1ALL"].set_title(f'Testdata: added all other datasets')#, fontweight='bold')
  axd["METRIC1ALL"].set_ylim([minMETRIC1, maxMETRIC1])
  axd["METRIC2ALL"].legend()
  axd["METRIC2ALL"].set_xlabel("% of Dataset used for Training", fontweight='bold')
  axd["METRIC2ALL"].set_ylabel(f'{yLabel}', fontweight='bold')
  axd["METRIC2ALL"].set_title(f'Testdata: added all other datasets')#, fontweight='bold')
  axd["METRIC2ALL"].set_ylim([minMETRIC2, maxMETRIC2])
  
  #fig.suptitle(f'Dataset used for Training: {DatasetNames[nSubset]}', fontweight='bold')
  plt.tight_layout()
  #plt.savefig(f'TESTRatios_Kernels-vs-{xLabel}_{yLabel}_{DatasetNames[nSubset]}.png', dpi=300, format='png')
  #break

if saveOrShow == "show":
  plt.show()
elif saveOrShow == "save":
  plt.savefig(f'Ratios-vs-{xLabel}_R2.png', dpi=300, format='png')























