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
#metric1 = "rmse"
metric1 = "mape"
metric2 = "r2"
#metric2 = "mape"

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
  metric1 = 'rmse_test'
  metric1All = "rmse_interpolation"
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
  metric1 = 'mape_test'
  metric1All = "mape_interpolation"
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
  minMETRIC1 = 0.00
  maxMETRIC1 = 0.15 
elif metric1 is "r2":
  metric1 = 'r2_test'
  metric1All = "r2_interpolation"
  xLabel = "R²"
  xLabelAll = "R2_ALL"
  maxMETRIC1 = 1.05
  minMETRIC1 = -1.05
else:
  print(f'Please set \'metric1\' to "rmse", "r2" or "mape". (Is: {metric1}). Exit.')
  exit()
  
if metric2 is "rmse":
  metric2 = 'rmse_test'
  metric2All = "rmse_interpolation"
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
  metric2 = 'mape_test'
  metric2All = "mape_interpolation"
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
  maxMETRIC2 = 0.13
elif metric2 is "r2":
  metric2 = 'r2_test'
  metric2All = "r2_interpolation"
  yLabel = "R²"
  yLabelAll = "R2_ALL"
  maxMETRIC2 = 1.05
  minMETRIC2 = -1.05
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

Kernels = ['RBF', 'Matern', 'RQ', 'ESS']
#Kernels = ['RBF', 'Matern', 'RQ']
if True:
  print(f'Grid1296')
  for kernel in Kernels:  # Loop over different kernels
    print(
        f'& {kernel} & '
        f'{np.round(np.mean(subsetGrid1296[subsetGrid1296["kernel"] == kernel]["mape_test"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid1296[subsetGrid1296["kernel"] == kernel]["mape_test"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetGrid1296[subsetGrid1296["kernel"] == kernel]["r2_test"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid1296[subsetGrid1296["kernel"] == kernel]["r2_test"].to_numpy()), 4):.5f} \\\\'
    )
  print('')
  print(f'Grid2401')
  for kernel in Kernels:  # Loop over different kernels
    print(
        f'& {kernel} & '
        f'{np.round(np.mean(subsetGrid2401[subsetGrid2401["kernel"] == kernel]["mape_test"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid2401[subsetGrid2401["kernel"] == kernel]["mape_test"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetGrid2401[subsetGrid2401["kernel"] == kernel]["r2_test"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid2401[subsetGrid2401["kernel"] == kernel]["r2_test"].to_numpy()), 4):.5f} \\\\'
    )
  print('')
  print(f'Sobol1')
  for kernel in Kernels:  # Loop over different kernels
    print(
        f'& {kernel} & '
        f'{np.round(np.mean(subsetSobol1[subsetSobol1["kernel"] == kernel]["mape_test"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol1[subsetSobol1["kernel"] == kernel]["mape_test"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetSobol1[subsetSobol1["kernel"] == kernel]["r2_test"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol1[subsetSobol1["kernel"] == kernel]["r2_test"].to_numpy()), 4):.5f} \\\\'
    )
  print('')
  print(f'Sobol2')
  for kernel in Kernels:  # Loop over different kernels
    print(
        f'& {kernel} & '
        f'{np.round(np.mean(subsetSobol2[subsetSobol2["kernel"] == kernel]["mape_test"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol2[subsetSobol2["kernel"] == kernel]["mape_test"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetSobol2[subsetSobol2["kernel"] == kernel]["r2_test"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol2[subsetSobol2["kernel"] == kernel]["r2_test"].to_numpy()), 4):.5f} \\\\'
    )
  print('')
  
if True:
  print(f'Grid1296')
  for kernel in Kernels:  # Loop over different kernels
    print(
        f'& {kernel} & '
        f'{np.round(np.mean(subsetGrid1296[subsetGrid1296["kernel"] == kernel]["mape_interpolation"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid1296[subsetGrid1296["kernel"] == kernel]["mape_interpolation"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetGrid1296[subsetGrid1296["kernel"] == kernel]["r2_interpolation"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid1296[subsetGrid1296["kernel"] == kernel]["r2_interpolation"].to_numpy()), 4):.5f} \\\\'
    )
  print('')
  print(f'Grid2401')
  for kernel in Kernels:  # Loop over different kernels
    print(
        f'& {kernel} & '
        f'{np.round(np.mean(subsetGrid2401[subsetGrid2401["kernel"] == kernel]["mape_interpolation"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid2401[subsetGrid2401["kernel"] == kernel]["mape_interpolation"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetGrid2401[subsetGrid2401["kernel"] == kernel]["r2_interpolation"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid2401[subsetGrid2401["kernel"] == kernel]["r2_interpolation"].to_numpy()), 4):.5f} \\\\'
    )
  print('')
  print(f'Sobol1')
  for kernel in Kernels:  # Loop over different kernels
    print(
        f'& {kernel} & '
        f'{np.round(np.mean(subsetSobol1[subsetSobol1["kernel"] == kernel]["mape_interpolation"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol1[subsetSobol1["kernel"] == kernel]["mape_interpolation"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetSobol1[subsetSobol1["kernel"] == kernel]["r2_interpolation"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol1[subsetSobol1["kernel"] == kernel]["r2_interpolation"].to_numpy()), 4):.5f} \\\\'
    )
  print('')
  print(f'Sobol2')
  for kernel in Kernels:  # Loop over different kernels
    print(
        f'& {kernel} & '
        f'{np.round(np.mean(subsetSobol2[subsetSobol2["kernel"] == kernel]["mape_interpolation"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol2[subsetSobol2["kernel"] == kernel]["mape_interpolation"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetSobol2[subsetSobol2["kernel"] == kernel]["r2_interpolation"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol2[subsetSobol2["kernel"] == kernel]["r2_interpolation"].to_numpy()), 4):.5f} \\\\'
    )
  print('')
  exit()


## plots

datasetSubsets = [subsetGrid1296, subsetGrid2401, subsetSobol1, subsetSobol2]
#print(f'{datasetSubsets[0]}')
colors = ['#377eb8', '#ff7f00', '#4daf4a', '#f781bf', '#a65628', '#984ea3', '#999999', '#e41a1c', '#dede00']
markers = ['1', '2', '3', '4', 'x', '+']
DatasetNames = ['Grid1296', 'Grid2401', 'Sobol1', 'Sobol2']
for nSubset in range(0, len(datasetSubsets)):
  #print(f'nSubset: {nSubset}')
  thisDataSubset = datasetSubsets[nSubset]
  gs_kw = dict(width_ratios=[1, 1, 1], height_ratios=[1, 1])
  fig, axd = plt.subplot_mosaic([['METRIC1', 'METRIC2', 'AvgByKernel'],
                                 ['METRIC1ALL', 'METRIC2ALL', 'AvgByKernelALL']],  
                                 gridspec_kw=gs_kw, figsize=(15.0, 10.0))

  KernelsForPlotting = []
  
  AvgRMSE = []
  AvgRMSEerr = []
  AvgR2 = []
  AvgR2err = []
  
  AvgRMSEAll = []
  AvgRMSEerrAll = []
  AvgR2All = []
  AvgR2errAll = []
  for t in range(0, len(Kernels)):
    kernel = Kernels[t]
    thisSubsetDegree = thisDataSubset[thisDataSubset["kernel"] == kernel]
    #print(f'{thisSubsetDegree}')
    KernelsForPlotting.append(kernel)
    
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
    axd['METRIC1'].errorbar(thisX, thisRMSE, yerr=thisRMSEerr, label=f'kernel = {kernel}', marker=markers[t], color=colors[t], ls='-.')
    axd['METRIC2'].errorbar(thisX, thisR2, yerr=thisR2err, label=f'kernel = {kernel}', marker=markers[t], color=colors[t], ls='-.')
    axd["METRIC1ALL"].errorbar(thisX, thisRMSEAll, yerr=thisRMSEerrAll, label=f'kernel = {kernel}, interpol.', marker=markers[t], color=colors[t], ls='-.')
    axd["METRIC2ALL"].errorbar(thisX, thisR2All, yerr=thisR2errAll, label=f'kernel = {kernel}, interpol.', marker=markers[t], color=colors[t], ls='-.')


  axd["METRIC1"].legend()
  axd["METRIC1"].set_ylabel(f'{xLabel}', fontweight='bold')
  #axd["METRIC1"].set_xlabel("% of Dataset used for Training", fontweight='bold')
  axd["METRIC1"].set_title(f'Testdata: from {DatasetNames[nSubset]}')#, fontweight='bold')
  #axd["METRIC1"].set_ylim([minMETRIC1, maxMETRIC1])
  axd["METRIC2"].legend()
  #axd["METRIC2"].set_xlabel("% of Dataset used for Training", fontweight='bold')
  axd["METRIC2"].set_ylabel(f'{yLabel}', fontweight='bold')
  axd["METRIC2"].set_title(f'Testdata: from {DatasetNames[nSubset]}')#, fontweight='bold')
  #axd["METRIC2"].set_ylim([minMETRIC2, maxMETRIC2])
  
  axd["METRIC1ALL"].legend()
  axd["METRIC1ALL"].set_ylabel(f'{xLabel}', fontweight='bold')
  axd["METRIC1ALL"].set_xlabel("% of Dataset used for Training", fontweight='bold')
  axd["METRIC1ALL"].set_title(f'Interpolation Test')#, fontweight='bold')
  #axd["METRIC1ALL"].set_ylim([minMETRIC1, maxMETRIC1])
  axd["METRIC2ALL"].legend()
  axd["METRIC2ALL"].set_xlabel("% of Dataset used for Training", fontweight='bold')
  axd["METRIC2ALL"].set_ylabel(f'{yLabel}', fontweight='bold')
  axd["METRIC2ALL"].set_title(f'Interpolation Test')#, fontweight='bold')
  #axd["METRIC2ALL"].set_ylim([minMETRIC2, maxMETRIC2])
  
  axd['AvgByKernel'].errorbar(KernelsForPlotting, AvgRMSE, yerr=AvgRMSEerr, label=f'avg. MAPE', marker='o', color='#069AF3', ls='-.')
  axd['AvgByKernel'].legend(bbox_to_anchor=(0.22,0.5), loc='center')
  axd["AvgByKernel"].set_ylabel(f'{xLabel}', c="#069AF3", fontweight='bold')
  #axd["AvgByKernel"].set_xlabel("kernel", fontweight='bold')
  axd["AvgByKernel"].set_title(f'Testdata: from same dataset')#, fontweight='bold')
  axd["AvgByKernel"].set_xticks(KernelsForPlotting)
  axd["AvgByKernel"].tick_params(axis='y', color="#069AF3", which='both')
  axd["AvgByKernel"].spines['left'].set_color("#069AF3")
  #axd["AvgByKernel"].set_ylim([minMETRIC1, maxMETRIC1])
  axd2 = axd["AvgByKernel"].twinx()
  axd2.errorbar(KernelsForPlotting, AvgR2, yerr=AvgR2err, label=f'avg. R²', marker='o', color='#F97306', ls='-.')
  axd2.legend(bbox_to_anchor=(0.8,0.5), loc='center')
  axd2.set_ylabel(f'{yLabel}', c="#F97306", fontweight='bold')
  #axd2.set_ylim([minMETRIC2, maxMETRIC2])
  axd2.spines['left'].set_color("#069AF3")
  axd2.spines['right'].set_color("#F97306")
  axd2.tick_params(axis='y', color="#F97306", which='both')
  #axd2.set_ylim([minMETRIC2, maxMETRIC2])
  
  axd["AvgByKernelALL"].errorbar(KernelsForPlotting, AvgRMSEAll, yerr=AvgRMSEerrAll, label=f'avg. MAPE, interpol', marker='o', color='#069AF3', ls='-.')
  axd["AvgByKernelALL"].legend(bbox_to_anchor=(0.25,0.55), loc='center')
  axd["AvgByKernelALL"].set_ylabel(f'{xLabel}', c="#069AF3", fontweight='bold')
  axd["AvgByKernelALL"].set_xlabel("kernel", fontweight='bold')
  axd["AvgByKernelALL"].set_title(f'Testdata: from all datasets')#, fontweight='bold')
  axd["AvgByKernelALL"].set_xticks(KernelsForPlotting)
  axd["AvgByKernelALL"].tick_params(axis='y', color="#069AF3", which='both')
  axd["AvgByKernelALL"].spines['left'].set_color("#069AF3")
  #axd["AvgByKernelALL"].set_ylim([minMETRIC1, maxMETRIC1])
  axd2 = axd["AvgByKernelALL"].twinx()
  axd2.errorbar(KernelsForPlotting, AvgR2All, yerr=AvgR2errAll, label=f'avg. R², interpol', marker='o', color='#F97306', ls='-.')
  axd2.legend(bbox_to_anchor=(0.75,0.55), loc='center')
  axd2.set_ylabel(f'{yLabel}', c="#F97306", fontweight='bold')
  #axd2.set_ylim([minMETRIC2, maxMETRIC2])
  axd2.spines['left'].set_color("#069AF3")
  axd2.spines['right'].set_color("#F97306")
  axd2.tick_params(axis='y', color="#F97306", which='both')
  
  #fig.suptitle(f'Dataset used for Training: {DatasetNames[nSubset]}', fontweight='bold')
  plt.tight_layout()
  if saveOrShow == "save":
    plt.savefig(f'Ratios_Kernels-vs-MAPE_R2_{DatasetNames[nSubset]}.png', dpi=100, format='png')

  #break
if saveOrShow == "show":
  plt.show()





















