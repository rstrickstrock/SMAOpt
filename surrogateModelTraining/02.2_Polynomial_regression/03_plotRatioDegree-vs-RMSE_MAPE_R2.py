import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import os
import glob
import sys



statisticsFile = 'Stats.csv'
#metric1 = "rmse"
metric1 = "mape"
metric2 = "r2"
#metric2 = "mape"

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


if metric1 is "rmse":
  metric1All = "rmse_all"
  xLabel = "RMSE"
  xLabelAll = "RMSE_ALL"
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
  maxMETRIC1 = 100
elif metric1 is "mape":
  metric1All = "mape_all"
  xLabel = "MAPE"
  xLabelAll = "MAPE_ALL"
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
  maxMETRIC1 = 0.10 
elif metric1 is "r2":
  metric1All = "r2_all"
  xLabel = "R2"
  xLabelAll = "R2_ALL"
  maxMETRIC1 = 1.05
  minMETRIC1 = 0.0
else:
  print(f'Please set \'metric1\' to "rmse", "r2" or "mape". (Is: {metric1}). Exit.')
  exit()
  
if metric2 is "rmse":
  metric2All = "rmse_all"
  yLabel = "RMSE"
  yLabelAll = "RMSE_ALL"
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
  maxMETRIC2 = 100
elif metric2 is "mape":
  metric2All = "mape_all"
  yLabel = "MAPE"
  yLabelAll = "MAPE_ALL"
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
  maxMETRIC2 = 0.10
elif metric2 is "r2":
  metric2All = "r2_all"
  yLabel = "R2"
  yLabelAll = "R2_ALL"
  maxMETRIC2 = 1.05
  minMETRIC2 = 0.0
else:
  print(f'Please set \'metric2\' to "rmse", "r2" or "mape". (Is: {metric2}). Exit.')
  exit()

subsetGrid1296 = dfStatistics[dfStatistics["dataset"] == "Grid1296"]
#print(f'Grid1296')
#print(f'mean RMSE: {np.mean(subsetGrid1296["rmse"].to_numpy())}')
#print(f'stddev RMSE: {np.std(subsetGrid1296["rmse"].to_numpy())}')
#print(f'mean R2: {np.mean(subsetGrid1296["r2"].to_numpy())}')
#print(f'stddev R2: {np.std(subsetGrid1296["r2"].to_numpy())}\n')
#print(f'mean RMSE: {np.mean(subsetGrid1296["rmse"].to_numpy())}')
subsetGrid2401 = dfStatistics[dfStatistics["dataset"] == "Grid2401"]
#print(f'Grid2401')
#print(f'mean RMSE: {np.mean(subsetGrid2401["rmse"].to_numpy())}')
#print(f'stddev RMSE: {np.std(subsetGrid2401["rmse"].to_numpy())}')
#print(f'mean R2: {np.mean(subsetGrid2401["r2"].to_numpy())}')
#print(f'stddev R2: {np.std(subsetGrid2401["r2"].to_numpy())}\n')
subsetSobol1 = dfStatistics[dfStatistics["dataset"] == "Sobol1"]
#print(f'Sobol1')
#print(f'mean RMSE: {np.mean(subsetSobol1["rmse"].to_numpy())}')
#print(f'stddev RMSE: {np.std(subsetSobol1["rmse"].to_numpy())}')
#print(f'mean R2: {np.mean(subsetSobol1["r2"].to_numpy())}')
#print(f'stddev R2: {np.std(subsetSobol1["r2"].to_numpy())}\n')
subsetSobol2 = dfStatistics[dfStatistics["dataset"] == "Sobol2"]
#print(f'Sobol2')
#print(f'mean RMSE: {np.mean(subsetSobol2["rmse"].to_numpy())}')
#print(f'stddev RMSE: {np.std(subsetSobol2["rmse"].to_numpy())}')
#print(f'mean R2: {np.mean(subsetSobol2["r2"].to_numpy())}')
#print(f'stddev R2: {np.std(subsetSobol2["r2"].to_numpy())}\n')
if False:
  print(f'Grid1296')
  for d in range(1, 11):  # Loop through degrees 1 to 10
    print(
        f'& {d} & '
        f'{np.round(np.mean(subsetGrid1296[subsetGrid1296["degree"] == d]["mape"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid1296[subsetGrid1296["degree"] == d]["mape"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetGrid1296[subsetGrid1296["degree"] == d]["r2"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid1296[subsetGrid1296["degree"] == d]["r2"].to_numpy()), 4):.5f} \\\\'
    )
  print('')
  print(f'Grid2401')
  for d in range(1, 11):  # Loop through degrees 1 to 10
    print(
        f'& {d} & '
        f'{np.round(np.mean(subsetGrid2401[subsetGrid2401["degree"] == d]["mape"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid2401[subsetGrid2401["degree"] == d]["mape"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetGrid2401[subsetGrid2401["degree"] == d]["r2"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid2401[subsetGrid2401["degree"] == d]["r2"].to_numpy()), 4):.5f} \\\\'
    )
  print('')
  print(f'Sobol1')
  for d in range(1, 11):  # Loop through degrees 1 to 10
    print(
        f'& {d} & '
        f'{np.round(np.mean(subsetSobol1[subsetSobol1["degree"] == d]["mape"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol1[subsetSobol1["degree"] == d]["mape"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetSobol1[subsetSobol1["degree"] == d]["r2"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol1[subsetSobol1["degree"] == d]["r2"].to_numpy()), 4):.5f} \\\\'
    )
  print('')
  print(f'Sobol2')
  for d in range(1, 11):  # Loop through degrees 1 to 10
    print(
        f'& {d} & '
        f'{np.round(np.mean(subsetSobol2[subsetSobol2["degree"] == d]["mape"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol2[subsetSobol2["degree"] == d]["mape"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetSobol2[subsetSobol2["degree"] == d]["r2"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol2[subsetSobol2["degree"] == d]["r2"].to_numpy()), 4):.5f} \\\\'
    )
  print('')

if False:
  print(f'Grid1296')
  for d in range(1, 11):  # Loop through degrees 1 to 10
    print(
        f'& {d} & '
        f'{np.round(np.mean(subsetGrid1296[subsetGrid1296["degree"] == d]["mape_all"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid1296[subsetGrid1296["degree"] == d]["mape_all"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetGrid1296[subsetGrid1296["degree"] == d]["r2_all"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid1296[subsetGrid1296["degree"] == d]["r2_all"].to_numpy()), 4):.5f} \\\\'
    )
  print('')
  print(f'Grid2401')
  for d in range(1, 11):  # Loop through degrees 1 to 10
    print(
        f'& {d} & '
        f'{np.round(np.mean(subsetGrid2401[subsetGrid2401["degree"] == d]["mape_all"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid2401[subsetGrid2401["degree"] == d]["mape_all"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetGrid2401[subsetGrid2401["degree"] == d]["r2_all"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid2401[subsetGrid2401["degree"] == d]["r2_all"].to_numpy()), 4):.5f} \\\\'
    )
  print('')
  print(f'Sobol1')
  for d in range(1, 11):  # Loop through degrees 1 to 10
    print(
        f'& {d} & '
        f'{np.round(np.mean(subsetSobol1[subsetSobol1["degree"] == d]["mape_all"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol1[subsetSobol1["degree"] == d]["mape_all"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetSobol1[subsetSobol1["degree"] == d]["r2_all"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol1[subsetSobol1["degree"] == d]["r2_all"].to_numpy()), 4):.5f} \\\\'
    )
  print('')
  print(f'Sobol2')
  for d in range(1, 11):  # Loop through degrees 1 to 10
    print(
        f'& {d} & '
        f'{np.round(np.mean(subsetSobol2[subsetSobol2["degree"] == d]["mape_all"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol2[subsetSobol2["degree"] == d]["mape_all"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetSobol2[subsetSobol2["degree"] == d]["r2_all"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol2[subsetSobol2["degree"] == d]["r2_all"].to_numpy()), 4):.5f} \\\\'
    )
  print('')

## plots
degs = [5, 5, 6, 6]
mindegs = [2, 2, 3, 3]
maxdegs = [9, 9, 9, 9]
datasetSubsets = [subsetGrid1296, subsetGrid2401, subsetSobol1, subsetSobol2]
#print(f'{datasetSubsets[0]}')
colors = ['#377eb8', '#ff7f00', '#4daf4a', '#f781bf', '#a65628', '#984ea3', '#999999', '#e41a1c', '#dede00']
markers = ['1', '2', '3', '4', 'x', '+', '.', '*', 's']
DatasetNames = ['Grid1296', 'Grid2401', 'Sobol1', 'Sobol2']
for deg in range(0, len(degs)):
  #print(f'deg: {deg}')
  thisDataSubset = datasetSubsets[deg]
  gs_kw = dict(width_ratios=[1, 1, 1], height_ratios=[1, 1])
  fig, axd = plt.subplot_mosaic([['METRIC1', 'METRIC2', 'AvgByDegree'],
                                 ['METRIC1ALL', 'METRIC2ALL', 'AvgByDegreeALL']],  
                                 gridspec_kw=gs_kw, figsize=(15.0, 10.0))

  DegreesForPlotting = []
  
  AvgRMSE = []
  AvgRMSEerr = []
  AvgR2 = []
  AvgR2err = []
  
  AvgRMSEAll = []
  AvgRMSEerrAll = []
  AvgR2All = []
  AvgR2errAll = []
  for d in range(1, maxdegs[deg]+1):
    thisSubsetDegree = thisDataSubset[thisDataSubset["degree"] == d]
    #print(f'{thisSubsetDegree}')
    DegreesForPlotting.append(d)
    
    AvgRMSE.append(np.mean(thisSubsetDegree[f'{metric1}'].to_numpy()))
    AvgRMSEerr.append(np.std(thisSubsetDegree[f'{metric1}'].to_numpy()))
    AvgR2.append(np.mean(thisSubsetDegree[f'{metric2}'].to_numpy()))
    AvgR2err.append(np.std(thisSubsetDegree[f'{metric2}'].to_numpy()))
    
    AvgRMSEAll.append(np.mean(thisSubsetDegree[f'{metric1All}'].to_numpy()))
    AvgRMSEerrAll.append(np.std(thisSubsetDegree[f'{metric1All}'].to_numpy()))
    AvgR2All.append(np.mean(thisSubsetDegree[f'{metric2All}'].to_numpy()))
    AvgR2errAll.append(np.std(thisSubsetDegree[f'{metric2All}'].to_numpy()))
    
    thisX = []
    
    thisRMSE = []
    thisRMSEerr = []
    thisR2 = []
    thisR2err = []
    
    thisRMSEAll = []
    thisRMSEerrAll = []
    thisR2All = []
    thisR2errAll = []
    
    for ratio in thisSubsetDegree["ratio"].unique():
      thisX.append(1-ratio)
      
      thisSubsetDegreeRatio = thisSubsetDegree[thisSubsetDegree["ratio"] == ratio]
      
      thisRMSE.append(np.mean(thisSubsetDegreeRatio[f'{metric1}'].to_numpy()))
      thisRMSEerr.append(np.std(thisSubsetDegreeRatio[f'{metric1}'].to_numpy()))
      thisR2.append(np.mean(thisSubsetDegreeRatio[f'{metric2}'].to_numpy()))
      thisR2err.append(np.std(thisSubsetDegreeRatio[f'{metric2}'].to_numpy()))
      
      thisRMSEAll.append(np.mean(thisSubsetDegreeRatio[f'{metric1All}'].to_numpy()))
      thisRMSEerrAll.append(np.std(thisSubsetDegreeRatio[f'{metric1All}'].to_numpy()))
      thisR2All.append(np.mean(thisSubsetDegreeRatio[f'{metric2All}'].to_numpy()))
      thisR2errAll.append(np.std(thisSubsetDegreeRatio[f'{metric2All}'].to_numpy()))
    
    if d >= mindegs[deg] and d <= degs[deg]:  
      axd['METRIC1'].errorbar(thisX, thisRMSE, yerr=thisRMSEerr, label=f'polyn. deg. = {d}', marker=markers[d-1], color=colors[d-1], ls='-.')
      axd['METRIC2'].errorbar(thisX, thisR2, yerr=thisR2err, label=f'polyn. deg. = {d}', marker=markers[d-1], color=colors[d-1], ls='-.')
      axd['METRIC1ALL'].errorbar(thisX, thisRMSEAll, yerr=thisRMSEerrAll, label=f'polyn. deg. = {d}, interpol.', marker=markers[d-1], color=colors[d-1], ls='-.')
      axd['METRIC2ALL'].errorbar(thisX, thisR2All, yerr=thisR2errAll, label=f'polyn. deg. = {d}, interpol.', marker=markers[d-1], color=colors[d-1], ls='-.')

  axd["METRIC1"].legend()
  axd["METRIC1"].set_ylabel(f'{xLabel}', fontweight='bold')
  #axd["METRIC1"].set_xlabel("% of Dataset used for Training", fontweight='bold')
  axd["METRIC1"].set_title(f'Testdata: from {DatasetNames[deg]}')#, fontweight='bold')
  axd["METRIC1"].set_ylim([minMETRIC1, maxMETRIC1])
  axd["METRIC2"].legend()
  #axd["METRIC2"].set_xlabel("% of Dataset used for Training", fontweight='bold')
  axd["METRIC2"].set_ylabel(f'{yLabel}', fontweight='bold')
  axd["METRIC2"].set_title(f'Testdata: from {DatasetNames[deg]}')#, fontweight='bold')
  axd["METRIC2"].set_ylim([minMETRIC2, maxMETRIC2])
  
  axd["METRIC1ALL"].legend()
  axd["METRIC1ALL"].set_ylabel(f'{xLabel}', fontweight='bold')
  axd["METRIC1ALL"].set_xlabel("% of Dataset used for Training", fontweight='bold')
  axd["METRIC1ALL"].set_title(f'Interpolation Test')#, fontweight='bold')
  axd["METRIC1ALL"].set_ylim([minMETRIC1, maxMETRIC1])
  axd["METRIC2ALL"].legend()
  axd["METRIC2ALL"].set_xlabel("% of Dataset used for Training", fontweight='bold')
  axd["METRIC2ALL"].set_ylabel(f'{yLabel}', fontweight='bold')
  axd["METRIC2ALL"].set_title(f'Interpolation Test')#, fontweight='bold')
  axd["METRIC2ALL"].set_ylim([minMETRIC2, maxMETRIC2])
  
  axd['AvgByDegree'].errorbar(DegreesForPlotting, AvgRMSE, yerr=AvgRMSEerr, label=f'avg. MAPE', marker='o', color='#069AF3', ls='-.')
  axd['AvgByDegree'].legend(bbox_to_anchor=(0.22,0.05), loc='center')
  axd["AvgByDegree"].set_ylabel(f'{xLabel}', c="#069AF3", fontweight='bold')
  #axd["AvgByDegree"].set_xlabel("Polynomial Degree", fontweight='bold')
  axd["AvgByDegree"].set_title(f'Testdata: from {DatasetNames[deg]}')#, fontweight='bold')
  axd["AvgByDegree"].set_xticks(DegreesForPlotting)
  axd["AvgByDegree"].tick_params(axis='y', color="#069AF3", which='both')
  axd["AvgByDegree"].spines['left'].set_color("#069AF3")
  axd["AvgByDegree"].set_ylim([minMETRIC1, maxMETRIC1])
  axd2 = axd["AvgByDegree"].twinx()
  axd2.errorbar(DegreesForPlotting, AvgR2, yerr=AvgR2err, label=f'avg. R²', marker='o', color='#F97306', ls='-.')
  axd2.legend(bbox_to_anchor=(0.8,0.05), loc='center')
  axd2.set_ylabel(f'{yLabel}', c="#F97306", fontweight='bold')
  axd2.set_ylim([minMETRIC2, maxMETRIC2])
  axd2.spines['left'].set_color("#069AF3")
  axd2.spines['right'].set_color("#F97306")
  axd2.tick_params(axis='y', color="#F97306", which='both')
  
  axd['AvgByDegreeALL'].errorbar(DegreesForPlotting, AvgRMSEAll, yerr=AvgRMSEerrAll, label=f'avg. MAPE, interpol.', marker='o', color='#069AF3', ls='-.')
  axd['AvgByDegreeALL'].legend(bbox_to_anchor=(0.22,0.05), loc='center')
  axd["AvgByDegreeALL"].set_ylabel(f'{xLabel}', c="#069AF3", fontweight='bold')
  axd["AvgByDegreeALL"].set_xlabel("Polynomial Degree", fontweight='bold')
  axd["AvgByDegreeALL"].set_title(f'Interpolation Test')#, fontweight='bold')
  axd["AvgByDegreeALL"].set_xticks(DegreesForPlotting)
  axd["AvgByDegreeALL"].tick_params(axis='y', color="#069AF3", which='both')
  axd["AvgByDegreeALL"].spines['left'].set_color("#069AF3")
  axd["AvgByDegreeALL"].set_ylim([minMETRIC1, maxMETRIC1])
  axd2 = axd["AvgByDegreeALL"].twinx()
  axd2.errorbar(DegreesForPlotting, AvgR2All, yerr=AvgR2errAll, label=f'avg. R², interpol.', marker='o', color='#F97306', ls='-.')
  axd2.legend(bbox_to_anchor=(0.8,0.05), loc='center')
  axd2.set_ylabel(f'{yLabel}', c="#F97306", fontweight='bold')
  axd2.set_ylim([minMETRIC2, maxMETRIC2])
  axd2.spines['left'].set_color("#069AF3")
  axd2.spines['right'].set_color("#F97306")
  axd2.tick_params(axis='y', color="#F97306", which='both')
  
  #fig.suptitle(f'Avg. {xLabel} / avg. {yLabel} per Training-/Testdata split or per polyn. degree - Trainingdataset: {DatasetNames[deg]}', fontweight='bold')
  plt.tight_layout()
  if saveOrShow == "save":
    plt.savefig(f'Ratios_Degrees-vs-MAPE_R2_{DatasetNames[deg]}.png', dpi=100, format='png')
  #break
  
if saveOrShow == "show":
  plt.show()
























