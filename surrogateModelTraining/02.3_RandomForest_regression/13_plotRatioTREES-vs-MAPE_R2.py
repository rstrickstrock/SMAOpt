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


treeTicks = [1, 2, 3, 4, 5, 6]
treeLabels = ["10", "100", "250", "500", "750", "1000"]
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

numberOfTrees = [10, 100, 250, 500, 750, 1000]
if printTable:
  print(f'Grid1296')
  for trees in numberOfTrees:  # Loop through #trees
    print(
        f'& {trees} & '
        f'{np.round(np.mean(subsetGrid1296[subsetGrid1296["#trees"] == trees]["mape_ist"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid1296[subsetGrid1296["#trees"] == trees]["mape_ist"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetGrid1296[subsetGrid1296["#trees"] == trees]["r2_ist"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid1296[subsetGrid1296["#trees"] == trees]["r2_ist"].to_numpy()), 4):.5f} \\\\'
    )
  print('')
  print(f'Grid2401')
  for trees in numberOfTrees:  # Loop through #trees
    print(
        f'& {trees} & '
        f'{np.round(np.mean(subsetGrid2401[subsetGrid2401["#trees"] == trees]["mape_ist"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid2401[subsetGrid2401["#trees"] == trees]["mape_ist"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetGrid2401[subsetGrid2401["#trees"] == trees]["r2_ist"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid2401[subsetGrid2401["#trees"] == trees]["r2_ist"].to_numpy()), 4):.5f} \\\\'
    )
  print('')
  print(f'Sobol1')
  for trees in numberOfTrees:  # Loop through #trees
    print(
        f'& {trees} & '
        f'{np.round(np.mean(subsetSobol1[subsetSobol1["#trees"] == trees]["mape_ist"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol1[subsetSobol1["#trees"] == trees]["mape_ist"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetSobol1[subsetSobol1["#trees"] == trees]["r2_ist"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol1[subsetSobol1["#trees"] == trees]["r2_ist"].to_numpy()), 4):.5f} \\\\'
    )
  print('')
  print(f'Sobol2')
  for trees in numberOfTrees:  # Loop through #trees
    print(
        f'& {trees} & '
        f'{np.round(np.mean(subsetSobol2[subsetSobol2["#trees"] == trees]["mape_ist"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol2[subsetSobol2["#trees"] == trees]["mape_ist"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetSobol2[subsetSobol2["#trees"] == trees]["r2_ist"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol2[subsetSobol2["#trees"] == trees]["r2_ist"].to_numpy()), 4):.5f} \\\\'
    )
  print('')

if printTable:
  print(f'Grid1296')
  for trees in numberOfTrees:  # Loop through #trees
    print(
        f'& {trees} & '
        f'{np.round(np.mean(subsetGrid1296[subsetGrid1296["#trees"] == trees]["mape_ost"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid1296[subsetGrid1296["#trees"] == trees]["mape_ost"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetGrid1296[subsetGrid1296["#trees"] == trees]["r2_ost"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid1296[subsetGrid1296["#trees"] == trees]["r2_ost"].to_numpy()), 4):.5f} \\\\'
    )
  print('')
  print(f'Grid2401')
  for trees in numberOfTrees:  # Loop through #trees
    print(
        f'& {trees} & '
        f'{np.round(np.mean(subsetGrid2401[subsetGrid2401["#trees"] == trees]["mape_ost"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid2401[subsetGrid2401["#trees"] == trees]["mape_ost"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetGrid2401[subsetGrid2401["#trees"] == trees]["r2_ost"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetGrid2401[subsetGrid2401["#trees"] == trees]["r2_ost"].to_numpy()), 4):.5f} \\\\'
    )
  print('')
  print(f'Sobol1')
  for trees in numberOfTrees:  # Loop through #trees
    print(
        f'& {trees} & '
        f'{np.round(np.mean(subsetSobol1[subsetSobol1["#trees"] == trees]["mape_ost"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol1[subsetSobol1["#trees"] == trees]["mape_ost"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetSobol1[subsetSobol1["#trees"] == trees]["r2_ost"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol1[subsetSobol1["#trees"] == trees]["r2_ost"].to_numpy()), 4):.5f} \\\\'
    )
  print('')
  print(f'Sobol2')
  for trees in numberOfTrees:  # Loop through #trees
    print(
        f'& {trees} & '
        f'{np.round(np.mean(subsetSobol2[subsetSobol2["#trees"] == trees]["mape_ost"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol2[subsetSobol2["#trees"] == trees]["mape_ost"].to_numpy()), 4):.5f} & '
        f'{np.round(np.mean(subsetSobol2[subsetSobol2["#trees"] == trees]["r2_ost"].to_numpy()), 4):.5f} $\pm$ '
        f'{np.round(np.std(subsetSobol2[subsetSobol2["#trees"] == trees]["r2_ost"].to_numpy()), 4):.5f} \\\\'
    )
  print('')
  
  
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
  fig, axd = plt.subplot_mosaic([['METRIC1', 'METRIC2', 'AvgByTrees'],
                                 ['METRIC1ALL', 'METRIC2ALL', 'AvgByTreesALL']],  
                                 gridspec_kw=gs_kw, figsize=(15.0, 10.0))

  TreesForPlotting = []
  
  AvgRMSE = []
  AvgRMSEerr = []
  AvgR2 = []
  AvgR2err = []
  
  AvgRMSEAll = []
  AvgRMSEerrAll = []
  AvgR2All = []
  AvgR2errAll = []
  for t in range(0, len(numberOfTrees)):
    trees = numberOfTrees[t]
    thisSubsetDegree = thisDataSubset[thisDataSubset["#trees"] == trees]
    #print(f'{thisSubsetDegree}')
    TreesForPlotting.append(trees)
    
    tmpAvgRMSE = np.mean(thisSubsetDegree[f'{metric1_ist}'].to_numpy())
    AvgRMSE.append(tmpAvgRMSE)
    thisUpperAvgRMSEerr = np.std(thisSubsetDegree[f'{metric1_ist}'].to_numpy())
    if tmpAvgRMSE - thisUpperAvgRMSEerr <= 0.0:
      thisLowerAvgRMSEerr = tmpAvgRMSE
    else:
      thisLowerAvgRMSEerr = thisUpperAvgRMSEerr
    AvgRMSEerr.append([thisLowerAvgRMSEerr, thisLowerAvgRMSEerr])
    
    tmpAvgR2 = np.mean(thisSubsetDegree[f'{metric2_ist}'].to_numpy())
    AvgR2.append(tmpAvgR2)
    thisLowerAvgR2err = np.std(thisSubsetDegree[f'{metric2_ist}'].to_numpy())
    if tmpAvgR2 + thisLowerAvgR2err <= 1.0:
      thisUpperAvgR2err = thisLowerAvgR2err
    else:
      thisUpperAvgR2err = 1.0 - tmpAvgR2
    AvgR2err.append([thisLowerAvgR2err, thisUpperAvgR2err])
    
    tmpAvgRMSEAll = np.mean(thisSubsetDegree[f'{metric1_ost}'].to_numpy())
    AvgRMSEAll.append(tmpAvgRMSEAll)
    thisUpperAvgRMSEerrAll = np.std(thisSubsetDegree[f'{metric1_ost}'].to_numpy())
    if tmpAvgRMSEAll - thisUpperAvgRMSEerrAll <= 0.0:
      thisLowerAvgRMSEerrAll = tmpAvgRMSEAll
    else:
      thisLowerAvgRMSEerrAll = thisUpperAvgRMSEerrAll
    AvgRMSEerrAll.append([thisLowerAvgRMSEerrAll, thisLowerAvgRMSEerrAll])
    
    tmpAvgR2All = np.mean(thisSubsetDegree[f'{metric2_ost}'].to_numpy())
    AvgR2All.append(tmpAvgR2All)
    thisLowerAvgR2errAll = np.std(thisSubsetDegree[f'{metric2_ost}'].to_numpy())
    if tmpAvgR2All + thisLowerAvgR2errAll <= 1.0:
      thisUpperAvgR2errAll = thisLowerAvgR2errAll
    else:
      thisUpperAvgR2errAll = 1.0 - tmpAvgR2All
    AvgR2errAll.append([thisLowerAvgR2errAll, thisUpperAvgR2errAll])
    
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
      
      tmpRMSE = np.mean(thisSubsetDegreeRatio[f'{metric1_ist}'].to_numpy())
      thisRMSE.append(tmpRMSE)  
      #thisRMSEerr.append(np.std(thisSubsetDegreeRatio[f'{metric1_ist}'].to_numpy()))
      thisUpperRMSEerr = np.std(thisSubsetDegreeRatio[f'{metric1_ist}'].to_numpy())
      if tmpRMSE - thisUpperRMSEerr <= 0.0:
        thisLowerRMSEerr = tmpRMSE
      else:
        thisLowerRMSEerr = thisUpperRMSEerr
      thisRMSEerr.append([thisLowerRMSEerr, thisUpperRMSEerr])
      
      tmpR2 = np.mean(thisSubsetDegreeRatio[f'{metric2_ist}'].to_numpy())
      thisR2.append(tmpR2)
      #thisR2err.append(np.std(thisSubsetDegreeRatio[f'{metric2_ist}'].to_numpy()))
      thisLowerR2err = np.std(thisSubsetDegreeRatio[f'{metric2_ist}'].to_numpy())
      if tmpR2 + thisLowerR2err <= 1.0:
        thisUpperR2err = thisLowerR2err
      else:
        thisUpperR2err = 1.0 - tmpR2
      thisR2err.append([thisLowerR2err, thisUpperR2err])
      
      tmpRMSEAll = np.mean(thisSubsetDegreeRatio[f'{metric1_ost}'].to_numpy())
      thisRMSEAll.append(tmpRMSEAll)
      #thisRMSEerrAll.append(np.std(thisSubsetDegreeRatio[f'{metric1_ost}'].to_numpy()))
      thisUpperRMSEerrAll = np.std(thisSubsetDegreeRatio[f'{metric1_ost}'].to_numpy())
      if tmpRMSEAll - thisUpperRMSEerrAll <= 0.0:
        thisLowerRMSEerrAll = tmpRMSEAll
      else:
        thisLowerRMSEerrAll = thisUpperRMSEerrAll
      thisRMSEerrAll.append([thisLowerRMSEerrAll, thisUpperRMSEerrAll])
      
      tmpR2All = np.mean(thisSubsetDegreeRatio[f'{metric2_ost}'].to_numpy())
      thisR2All.append(tmpR2All)
      #thisR2errAll.append(np.std(thisSubsetDegreeRatio[f'{metric2_ost}'].to_numpy()))
      thisLowerR2errAll = np.std(thisSubsetDegreeRatio[f'{metric2_ost}'].to_numpy())
      if tmpR2All + thisLowerR2errAll <= 1.0:
        thisUpperR2errAll = thisLowerR2errAll
      else:
        thisUpperR2errAll = 1.0 - tmpR2All
      thisR2errAll.append([thisLowerR2errAll, thisUpperR2errAll])
    
    thisRMSEerr = np.array(thisRMSEerr).transpose() 
    thisR2err = np.array(thisR2err).transpose()
    thisRMSEerrAll = np.array(thisRMSEerrAll).transpose()
    thisR2errAll = np.array(thisR2errAll).transpose()
      
    axd["METRIC1"].errorbar(thisX, thisRMSE, yerr=thisRMSEerr, label=f'#trees = {trees}', marker=markers[t], color=colors[t], ls='dotted', capsize=4.0)
    axd["METRIC2"].errorbar(thisX, thisR2, yerr=thisR2err, label=f'#trees = {trees}', marker=markers[t], color=colors[t], ls='dotted', capsize=4.0)
    axd["METRIC1ALL"].errorbar(thisX, thisRMSEAll, yerr=thisRMSEerrAll, label=f'#trees = {trees}', marker=markers[t], color=colors[t], ls='dotted', capsize=4.0)
    axd["METRIC2ALL"].errorbar(thisX, thisR2All, yerr=thisR2errAll, label=f'#trees = {trees}', marker=markers[t], color=colors[t], ls='dotted', capsize=4.0)


  AvgRMSEerr = np.array(AvgRMSEerr).transpose() 
  AvgR2err = np.array(AvgR2err).transpose()
  AvgRMSEerrAll = np.array(AvgRMSEerrAll).transpose()
  AvgR2errAll = np.array(AvgR2errAll).transpose()
  
  axd["METRIC1"].legend()
  axd["METRIC1"].set_ylabel(f'{xLabel} [%]', fontweight='bold', fontsize=18)
  axd["METRIC1"].set_title(f'In-sample Test (IST), {DatasetNames[nSubset]}', fontweight='bold', color='gray', fontsize=15)
  axd["METRIC1"].set_ylim([minMAPE, maxMAPE])
  axd["METRIC1"].set_yticks(MAPETicks)
  axd["METRIC1"].set_yticklabels(MAPETickLabels, fontsize=15)
  axd["METRIC1"].set_xticks(ratioTicks)
  axd["METRIC1"].set_xticklabels(ratioLabels, fontsize=15)
  axd["METRIC1"].grid(color='lightgray', linestyle='dotted')
  #
  axd["METRIC2"].legend()
  axd["METRIC2"].set_ylabel(f'{yLabel}', fontweight='bold', fontsize=18)
  axd["METRIC2"].set_title(f'In-sample Test (IST), {DatasetNames[nSubset]}', fontweight='bold', color='gray', fontsize=15)
  axd["METRIC2"].set_ylim([minR2, maxR2])
  axd["METRIC2"].set_yticks(R2Ticks)
  axd["METRIC2"].set_yticklabels(R2TickLabels, fontsize=15)
  axd["METRIC2"].set_xticks(ratioTicks)
  axd["METRIC2"].set_xticklabels(ratioLabels, fontsize=15)
  axd["METRIC2"].grid(color='lightgray', linestyle='dotted')
  
  axd["METRIC1ALL"].legend()
  axd["METRIC1ALL"].set_ylabel(f'{xLabel} [%]', fontweight='bold', fontsize=18)
  axd["METRIC1ALL"].set_xlabel("Dataset ratio used for Training [%]", fontweight='bold', fontsize=15)
  axd["METRIC1ALL"].set_title(f'Out-of-sample Test (OST), {DatasetNames[nSubset]}', fontweight='bold', color='gray', fontsize=15)
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
  axd["METRIC2ALL"].set_title(f'Out-of-sample Test (OST), {DatasetNames[nSubset]}', fontweight='bold', color='gray', fontsize=15)
  axd["METRIC2ALL"].set_ylim([minR2, maxR2])
  axd["METRIC2ALL"].set_yticks(R2Ticks)
  axd["METRIC2ALL"].set_yticklabels(R2TickLabels, fontsize=15)
  axd["METRIC2ALL"].set_xticks(ratioTicks)
  axd["METRIC2ALL"].set_xticklabels(ratioLabels, fontsize=15)
  axd["METRIC2ALL"].grid(color='lightgray', linestyle='dotted')
  
  axd["AvgByTrees"].errorbar(treeTicks, AvgRMSE, yerr=AvgRMSEerr, label=f'avg. MAPE', marker='o', color='#069AF3', ls='dotted', capsize=4.0)
  axd["AvgByTrees"].legend(bbox_to_anchor=(0.25,0.55), loc='center')
  axd["AvgByTrees"].set_ylabel(f'{xLabel} [%]', c="#069AF3", fontweight='bold', fontsize=18)
  axd["AvgByTrees"].set_title(f'In-sample Test (IST), {DatasetNames[nSubset]}', fontweight='bold', color='gray', fontsize=15)
  axd["AvgByTrees"].tick_params(axis='y', color="#069AF3", which='both')
  axd["AvgByTrees"].spines['left'].set_color("#069AF3")
  axd["AvgByTrees"].set_ylim([minMAPE, maxMAPE])
  axd["AvgByTrees"].set_yticks(MAPETicks)
  axd["AvgByTrees"].set_yticklabels(MAPETickLabels, fontsize=15)
  axd["AvgByTrees"].set_xticks(treeTicks)
  axd["AvgByTrees"].set_xticklabels(treeLabels, fontsize=15)
  axd["AvgByTrees"].grid(color='lightgray', linestyle='dotted')
  axd2 = axd["AvgByTrees"].twinx()
  axd2.errorbar(treeTicks, AvgR2, yerr=AvgR2err, label=f'avg. R²', marker='o', color='#F97306', ls='dotted', capsize=4.0)
  axd2.legend(bbox_to_anchor=(0.75,0.55), loc='center')
  axd2.set_ylabel(f'{yLabel}', c="#F97306", fontweight='bold', fontsize=18)
  axd2.set_ylim([minR2, maxR2])
  axd2.set_yticks(R2Ticks)
  axd2.set_yticklabels(R2TickLabels, fontsize=15)
  axd2.spines['left'].set_color("#069AF3")
  axd2.spines['right'].set_color("#F97306")
  axd2.tick_params(axis='y', color="#F97306", which='both')
  #
  axd["AvgByTreesALL"].errorbar(treeTicks, AvgRMSEAll, yerr=AvgRMSEerrAll, label=f'avg. MAPE', marker='o', color='#069AF3', ls='dotted', capsize=4.0)
  if DatasetNames[nSubset] == "Grid2401":
    axd["AvgByTreesALL"].legend(bbox_to_anchor=(0.25,0.25), loc='center')
  else:
    axd["AvgByTreesALL"].legend(bbox_to_anchor=(0.25,0.55), loc='center')
  axd["AvgByTreesALL"].set_ylabel(f'{xLabel} [%]', c="#069AF3", fontweight='bold', fontsize=18)
  axd["AvgByTreesALL"].set_xlabel("Number of Trees", fontweight='bold', fontsize=18)
  axd["AvgByTreesALL"].set_title(f'Out-of-sample Test (OST), {DatasetNames[nSubset]}', fontweight='bold', color='gray', fontsize=15)
  axd["AvgByTreesALL"].tick_params(axis='y', color="#069AF3", which='both')
  axd["AvgByTreesALL"].spines['left'].set_color("#069AF3")
  axd["AvgByTreesALL"].set_ylim([minMAPE, maxMAPE])
  axd["AvgByTreesALL"].set_yticks(MAPETicks)
  axd["AvgByTreesALL"].set_yticklabels(MAPETickLabels, fontsize=15)
  axd["AvgByTreesALL"].set_xticks(treeTicks)
  axd["AvgByTreesALL"].set_xticklabels(treeLabels, fontsize=15)
  axd["AvgByTreesALL"].grid(color='lightgray', linestyle='dotted')
  axd2 = axd["AvgByTreesALL"].twinx()
  axd2.errorbar(treeTicks, AvgR2All, yerr=AvgR2errAll, label=f'avg. R²', marker='o', color='#F97306', ls='dotted', capsize=4.0)
  if DatasetNames[nSubset] == "Grid2401":
    axd2.legend(bbox_to_anchor=(0.75,0.25), loc='center')
  else:
    axd2.legend(bbox_to_anchor=(0.75,0.55), loc='center')
  axd2.set_ylabel(f'{yLabel}', c="#F97306", fontweight='bold', fontsize=18)
  axd2.set_ylim([minR2, maxR2])
  axd2.set_yticks(R2Ticks)
  axd2.set_yticklabels(R2TickLabels, fontsize=15)
  axd2.spines['left'].set_color("#069AF3")
  axd2.spines['right'].set_color("#F97306")
  axd2.tick_params(axis='y', color="#F97306", which='both')
  
  plt.tight_layout()
  if saveOrShow == "save":
    plt.savefig(f'Ratios_Trees-vs-MAPE_R2_{DatasetNames[nSubset]}.png', dpi=figDPI, format='png')
  #break
  
if saveOrShow == "show":
  plt.show()
























