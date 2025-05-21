import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import os
import glob
import sys

statisticsFile = 'Stats_OST.csv'
figDPI = 300
printTable = False

xLabel = "MAPE"
xLabelAll = "MAPE (OST)"
yLabel = "R²"
yLabelAll = "R² (OST)"

metric1_ist = "mape_ist"
metric2_ist = "r2_ist"
metric1_ost = "mape_ost"
metric2_ost = "r2_ost"

try:
  saveOrShow = sys.argv[1]
except:
  saveOrShow = "show"
if saveOrShow == "save":
  pass
else:
  saveOrShow = "show"

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


ratioTicks = [0.05, 0.25, 0.45, 0.65, 0.85]
ratioLabels = ["5", "25", "45", "65", "85"]
minMAPE = -0.005
maxMAPE = 0.175
MAPETicks = [0.0, 0.05, 0.10, 0.15]
MAPETickLabels = ["0", "5", "10", "15"]
minR2 = -0.05
maxR2 = 1.05
R2Ticks = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
R2TickLabels = ["0.0", "0.2", "0.4", "0.6", "0.8", "1.0"]

subsetGrid1296 = dfStatistics[dfStatistics["dataset"] == "Grid1296"]
subsetGrid2401 = dfStatistics[dfStatistics["dataset"] == "Grid2401"]
subsetSobol1 = dfStatistics[dfStatistics["dataset"] == "Sobol1"]
subsetSobol2 = dfStatistics[dfStatistics["dataset"] == "Sobol2"]

if printTable:
  print(f'Grid1296')
  print(
      f'& {np.round(np.mean(subsetGrid1296["mape_ist"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetGrid1296["mape_ist"].to_numpy()), 4):.5f} & '
      f'{np.round(np.mean(subsetGrid1296["r2_ist"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetGrid1296["r2_ist"].to_numpy()), 4):.5f} \\\\'
  )
  print('')
  print(f'Grid2401')
  print(
      f'& {np.round(np.mean(subsetGrid2401["mape_ist"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetGrid2401["mape_ist"].to_numpy()), 4):.5f} & '
      f'{np.round(np.mean(subsetGrid2401["r2_ist"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetGrid2401["r2_ist"].to_numpy()), 4):.5f} \\\\'
  )
  print('')
  print(f'Sobol1')
  print(
      f'& {np.round(np.mean(subsetSobol1["mape_ist"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetSobol1["mape_ist"].to_numpy()), 4):.5f} & '
      f'{np.round(np.mean(subsetSobol1["r2_ist"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetSobol1["r2_ist"].to_numpy()), 4):.5f} \\\\'
  )
  print('')
  print(f'Sobol2')
  print(
      f'& {np.round(np.mean(subsetSobol2["mape_ist"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetSobol2["mape_ist"].to_numpy()), 4):.5f} & '
      f'{np.round(np.mean(subsetSobol2["r2_ist"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetSobol2["r2_ist"].to_numpy()), 4):.5f} \\\\'
  )
  print('')
  
if printTable:
  print(f'Grid1296')
  print(
      f'& {np.round(np.mean(subsetGrid1296["mape_ost"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetGrid1296["mape_ost"].to_numpy()), 4):.5f} & '
      f'{np.round(np.mean(subsetGrid1296["r2_ost"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetGrid1296["r2_ost"].to_numpy()), 4):.5f} \\\\'
  )
  print('')
  print(f'Grid2401')
  print(
      f'& {np.round(np.mean(subsetGrid2401["mape_ost"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetGrid2401["mape_ost"].to_numpy()), 4):.5f} & '
      f'{np.round(np.mean(subsetGrid2401["r2_ost"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetGrid2401["r2_ost"].to_numpy()), 4):.5f} \\\\'
  )
  print('')
  print(f'Sobol1')
  print(
      f'& {np.round(np.mean(subsetSobol1["mape_ost"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetSobol1["mape_ost"].to_numpy()), 4):.5f} & '
      f'{np.round(np.mean(subsetSobol1["r2_ost"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetSobol1["r2_ost"].to_numpy()), 4):.5f} \\\\'
  )
  print('')
  print(f'Sobol2')
  print(
      f'& {np.round(np.mean(subsetSobol2["mape_ost"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetSobol2["mape_ost"].to_numpy()), 4):.5f} & '
      f'{np.round(np.mean(subsetSobol2["r2_ost"].to_numpy()), 4):.5f} $\pm$ '
      f'{np.round(np.std(subsetSobol2["r2_ost"].to_numpy()), 4):.5f} \\\\'
  )
  print('')


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
      
    tmpRMSE = np.mean(thisDataSubsetRatio[f'{metric1_ist}'].to_numpy())
    thisRMSE.append(tmpRMSE)  
    #thisRMSEerr.append(np.std(thisDataSubsetRatio[f'{metric1_ist}'].to_numpy()))
    thisUpperRMSEerr = np.std(thisDataSubsetRatio[f'{metric1_ist}'].to_numpy())
    if tmpRMSE - thisUpperRMSEerr <= 0.0:
      thisLowerRMSEerr = tmpRMSE
    else:
      thisLowerRMSEerr = thisUpperRMSEerr
    thisRMSEerr.append([thisLowerRMSEerr, thisUpperRMSEerr])
      
    tmpR2 = np.mean(thisDataSubsetRatio[f'{metric2_ist}'].to_numpy())
    thisR2.append(tmpR2)
    #thisR2err.append(np.std(thisDataSubsetRatio[f'{metric2_ist}'].to_numpy()))
    thisLowerR2err = np.std(thisDataSubsetRatio[f'{metric2_ist}'].to_numpy())
    if tmpR2 + thisLowerR2err <= 1.0:
      thisUpperR2err = thisLowerR2err
    else:
      thisUpperR2err = 1.0 - tmpR2
    thisR2err.append([thisLowerR2err, thisUpperR2err])
      
    tmpRMSEAll = np.mean(thisDataSubsetRatio[f'{metric1_ost}'].to_numpy())
    thisRMSEAll.append(tmpRMSEAll)
    #thisRMSEerrAll.append(np.std(thisDataSubsetRatio[f'{metric1_ost}'].to_numpy()))
    thisUpperRMSEerrAll = np.std(thisDataSubsetRatio[f'{metric1_ost}'].to_numpy())
    if tmpRMSEAll - thisUpperRMSEerrAll <= 0.0:
      thisLowerRMSEerrAll = tmpRMSEAll
    else:
      thisLowerRMSEerrAll = thisUpperRMSEerrAll
    thisRMSEerrAll.append([thisLowerRMSEerrAll, thisUpperRMSEerrAll])
      
    tmpR2All = np.mean(thisDataSubsetRatio[f'{metric2_ost}'].to_numpy())
    thisR2All.append(tmpR2All)
    #thisR2errAll.append(np.std(thisDataSubsetRatio[f'{metric2_ost}'].to_numpy()))
    thisLowerR2errAll = np.std(thisDataSubsetRatio[f'{metric2_ost}'].to_numpy())
    if tmpR2All + thisLowerR2errAll <= 1.0:
      thisUpperR2errAll = thisLowerR2errAll
    else:
      thisUpperR2errAll = 1.0 - tmpR2All
    thisR2errAll.append([thisLowerR2errAll, thisUpperR2errAll])
    
  thisRMSEerr = np.array(thisRMSEerr).transpose() 
  thisR2err = np.array(thisR2err).transpose()
  thisRMSEerrAll = np.array(thisRMSEerrAll).transpose()
  thisR2errAll = np.array(thisR2errAll).transpose()
      
  axd['METRIC1'].errorbar(thisX, thisRMSE, yerr=thisRMSEerr, label=f'{DatasetNames[nSubset]}', marker=markers[nSubset], color=colors[nSubset], ls='dotted', capsize=4.0)
  axd['METRIC2'].errorbar(thisX, thisR2, yerr=thisR2err, label=f'{DatasetNames[nSubset]}', marker=markers[nSubset], color=colors[nSubset], ls='dotted', capsize=4.0)
  axd["METRIC1ALL"].errorbar(thisX, thisRMSEAll, yerr=thisRMSEerrAll, label=f'{DatasetNames[nSubset]}', marker=markers[nSubset], color=colors[nSubset], ls='dotted', capsize=4.0)
  axd["METRIC2ALL"].errorbar(thisX, thisR2All, yerr=thisR2errAll, label=f'{DatasetNames[nSubset]}', marker=markers[nSubset], color=colors[nSubset], ls='dotted', capsize=4.0)
   
  axd["METRIC1"].legend()
  axd["METRIC1"].set_ylabel(f'{xLabel} [%]', fontweight='bold', fontsize=18)
  #axd["METRIC1"].set_xlabel("% of Dataset used for Training", fontweight='bold')
  axd["METRIC1"].set_title(f'In-sample Test (IST)', fontweight='bold', color='gray', fontsize=15)
  axd["METRIC1"].set_ylim([minMAPE, maxMAPE])
  axd["METRIC1"].set_yticks(MAPETicks)
  axd["METRIC1"].set_yticklabels(MAPETickLabels, fontsize=15)
  axd["METRIC1"].set_xticks(ratioTicks)
  axd["METRIC1"].set_xticklabels(ratioLabels, fontsize=15)
  axd["METRIC1"].grid(color='lightgray', linestyle='dotted')
  #
  axd["METRIC2"].legend()
  #axd["METRIC2"].set_xlabel("% of Dataset used for Training", fontweight='bold')
  axd["METRIC2"].set_ylabel(f'{yLabel}', fontweight='bold', fontsize=18)
  axd["METRIC2"].set_title(f'In-sample Test (IST)', fontweight='bold', color='gray', fontsize=15)
  axd["METRIC2"].set_ylim([minR2, maxR2])
  axd["METRIC2"].set_yticks(R2Ticks)
  axd["METRIC2"].set_yticklabels(R2TickLabels, fontsize=15)
  axd["METRIC2"].set_xticks(ratioTicks)
  axd["METRIC2"].set_xticklabels(ratioLabels, fontsize=15)
  axd["METRIC2"].grid(color='lightgray', linestyle='dotted')
  
  axd["METRIC1ALL"].legend()
  axd["METRIC1ALL"].set_ylabel(f'{xLabel} [%]', fontweight='bold', fontsize=18)
  axd["METRIC1ALL"].set_xlabel("Dataset ratio used for Training [%]", fontweight='bold', fontsize=15)
  axd["METRIC1ALL"].set_title(f'Out-of-sample Test (OST)', fontweight='bold', color='gray', fontsize=15)
  axd["METRIC1ALL"].set_ylim([minMAPE, maxMAPE])
  axd["METRIC1ALL"].set_ylim([minMAPE, maxMAPE])
  axd["METRIC1ALL"].set_yticks(MAPETicks)
  axd["METRIC1ALL"].set_yticklabels(MAPETickLabels, fontsize=15)
  axd["METRIC1ALL"].set_xticks(ratioTicks)
  axd["METRIC1ALL"].set_xticklabels(ratioLabels, fontsize=15)
  axd["METRIC1ALL"].grid(color='lightgray', linestyle='dotted')
  #
  axd["METRIC2ALL"].legend()
  axd["METRIC2ALL"].set_xlabel("Dataset ratio used for Training [%]", fontweight='bold', fontsize=15)
  axd["METRIC2ALL"].set_ylabel(f'{yLabel}', fontweight='bold', fontsize=18)
  axd["METRIC2ALL"].set_title(f'Out-of-sample Test (OST)', fontweight='bold', color='gray', fontsize=15)
  axd["METRIC2ALL"].set_ylim([minR2, maxR2])
  axd["METRIC2ALL"].set_yticks(R2Ticks)
  axd["METRIC2ALL"].set_yticklabels(R2TickLabels, fontsize=15)
  axd["METRIC2ALL"].set_xticks(ratioTicks)
  axd["METRIC2ALL"].set_xticklabels(ratioLabels, fontsize=15)
  axd["METRIC2ALL"].grid(color='lightgray', linestyle='dotted')
  
  plt.tight_layout()


if saveOrShow == "show":
  plt.show()
elif saveOrShow == "save":
  plt.savefig(f'Ratios-vs-MAPE_R2.png', dpi=figDPI, format='png')























