import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import sys
import os
import glob

#metricY1 = "rmse"
metricY1 = "mape"
metricY2 = "r2"
#metricY2 = "mape"
statisticsFile = 'Stats.csv'

try:
  saveOrShow = sys.argv[1]
except:
  saveOrShow = "show"
if saveOrShow == "save":
  pass
else:
  saveOrShow = "show"

if not metricY1 in ["rmse", "mape", "r2"]:
  print(f'Chosen metric 1 ({metricY1}) is not in [rmse, mape, r2]. Please chose one of them. Exit.')
  exit()
if not metricY2 in ["rmse", "mape", "r2"]:
  print(f'Chosen metric 2 ({metricY2}) is not in [rmse, mape, r2]. Please chose one of them. Exit.')
  exit()
  
if metricY1 is "rmse":
  xLabel = "RMSE"
  xLabelAll = "RMSE_ALL"
  metricY1All = "rmse_all"
elif metricY1 is "mape":
  xLabel = "MAPE"
  xLabelAll = "MAPE, interp."
  metricY1All = "mape_all"
else:
  xLabel = "R²"
  xLabelAll = "R², interp."
  metricY1All = "r2_all"

if metricY2 is "rmse":
  yLabel = "RMSE"
  yLabelAll = "RMSE_ALL"
  metricY2All = "rmse_all"
elif metricY2 is "mape":
  yLabel = "MAPE"
  yLabelAll = "MAPE, interp."
  metricY2All = "mape_all"
else:
  yLabel = "R²"
  yLabelAll = "R², interp."
  metricY2All = "r2_all"

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


minMetric1 = dfStatistics[f'{metricY1}'].min()
minMetric1 = minMetric1 - 0.01*minMetric1
maxMetric1 = dfStatistics[f'{metricY1}'].max()
maxMetric1 = maxMetric1 + 0.01*maxMetric1
minMetric2 = dfStatistics[f'{metricY2}'].min()
minMetric2 = minMetric2 - 0.001*minMetric2
maxMetric2 = dfStatistics[f'{metricY2}'].max()
maxMetric2 = maxMetric2 + 0.01*maxMetric2

minMetric1All = dfStatistics[f'{metricY1All}'].min()
minMetric1All = minMetric1All - 0.01*minMetric1All
maxMetric1All = dfStatistics[f'{metricY1All}'].max()
maxMetric1All = maxMetric1All + 0.01*maxMetric1All
minMetric2All = dfStatistics[f'{metricY2All}'].min()
minMetric2All = minMetric2All - 0.001*minMetric2All
maxMetric2All = dfStatistics[f'{metricY2All}'].max()
maxMetric2All = maxMetric2All + 0.01*maxMetric2All

minMetric1 = min(minMetric1, minMetric1All)
maxMetric1 = max(maxMetric1, maxMetric1All)
minMetric2 = min(minMetric2, minMetric2All)
maxMetric2 = max(maxMetric2, maxMetric2All)

subsetGrid1296 = dfStatistics[dfStatistics["dataset"] == "Grid1296"]
print(f'Grid1296')
print(f'mean {xLabel}: {np.mean(subsetGrid1296[metricY1].to_numpy()):.5f} +/- {np.std(subsetGrid1296[metricY1].to_numpy()):.5f}')
print(f'mean {yLabel}:   {np.mean(subsetGrid1296[metricY2].to_numpy()):.5f} +/- {np.std(subsetGrid1296[metricY2].to_numpy()):.5f}')
print(f'mean {xLabelAll}: {np.mean(subsetGrid1296[metricY1All].to_numpy()):.5f} +/- {np.std(subsetGrid1296[metricY1All].to_numpy()):.5f}')
print(f'mean {yLabelAll}:   {np.mean(subsetGrid1296[metricY2All].to_numpy()):.5f} +/- {np.std(subsetGrid1296[metricY2All].to_numpy()):.5f}')
subsetGrid2401 = dfStatistics[dfStatistics["dataset"] == "Grid2401"]
print(f'Grid2401')
print(f'mean {xLabel}: {np.mean(subsetGrid2401[metricY1].to_numpy()):.5f} +/- {np.std(subsetGrid2401[metricY1].to_numpy()):.5f}')
print(f'mean {yLabel}:   {np.mean(subsetGrid2401[metricY2].to_numpy()):.5f} +/- {np.std(subsetGrid2401[metricY2].to_numpy()):.5f}')
print(f'mean {xLabelAll}: {np.mean(subsetGrid2401[metricY1All].to_numpy()):.5f} +/- {np.std(subsetGrid2401[metricY1All].to_numpy()):.5f}')
print(f'mean {yLabelAll}:   {np.mean(subsetGrid2401[metricY2All].to_numpy()):.5f} +/- {np.std(subsetGrid2401[metricY2All].to_numpy()):.5f}')
subsetSobol1 = dfStatistics[dfStatistics["dataset"] == "Sobol1"]
print(f'Sobol1')
print(f'mean {xLabel}: {np.mean(subsetSobol1[metricY1].to_numpy()):.5f} +/- {np.std(subsetSobol1[metricY1].to_numpy()):.5f}')
print(f'mean {yLabel}:   {np.mean(subsetSobol1[metricY2].to_numpy()):.5f} +/- {np.std(subsetSobol1[metricY2].to_numpy()):.5f}')
print(f'mean {xLabelAll}: {np.mean(subsetSobol1[metricY1All].to_numpy()):.5f} +/- {np.std(subsetSobol1[metricY1All].to_numpy()):.5f}')
print(f'mean {yLabelAll}:   {np.mean(subsetSobol1[metricY2All].to_numpy()):.5f} +/- {np.std(subsetSobol1[metricY2All].to_numpy()):.5f}')
subsetSobol2 = dfStatistics[dfStatistics["dataset"] == "Sobol2"]
print(f'Sobol2')
print(f'mean {xLabel}: {np.mean(subsetSobol2[metricY1].to_numpy()):.5f} +/- {np.std(subsetSobol2[metricY1].to_numpy()):.5f}')
print(f'mean {yLabel}:   {np.mean(subsetSobol2[metricY2].to_numpy()):.5f} +/- {np.std(subsetSobol2[metricY2].to_numpy()):.5f}')
print(f'mean {xLabelAll}: {np.mean(subsetSobol2[metricY1All].to_numpy()):.5f} +/- {np.std(subsetSobol2[metricY1All].to_numpy()):.5f}')
print(f'mean {yLabelAll}:   {np.mean(subsetSobol2[metricY2All].to_numpy()):.5f} +/- {np.std(subsetSobol2[metricY2All].to_numpy()):.5f}')

## plots
gs_kw = dict(width_ratios=[1, 1], height_ratios=[1, 1])
fig, axd = plt.subplot_mosaic([['Grid1296', 'Sobol1'], 
                               ['Grid2401', 'Sobol2']], 
                               gridspec_kw=gs_kw, figsize=(10.0, 10.0))

axd2Grid1296 = axd["Grid1296"].twinx()
axd2Grid2401 = axd["Grid2401"].twinx()
axd2Sobol1 = axd["Sobol1"].twinx()
axd2Sobol2 = axd["Sobol2"].twinx()

labeled = False
for ratio in subsetGrid1296["ratio"].unique():
  thisSubset = subsetGrid1296[subsetGrid1296["ratio"] == ratio]
  thisAvgRMSE = np.mean(thisSubset[f'{metricY1}'].to_numpy())
  thisStdRMSE = np.std(thisSubset[f'{metricY1}'].to_numpy())
  thisAvgR2 = np.mean(thisSubset[f'{metricY2}'].to_numpy())
  thisStdR2 = np.std(thisSubset[f'{metricY2}'].to_numpy())
  thisAvgRMSEAll = np.mean(thisSubset[f'{metricY1All}'].to_numpy())
  thisStdRMSEAll = np.std(thisSubset[f'{metricY1All}'].to_numpy())
  thisAvgR2All = np.mean(thisSubset[f'{metricY2All}'].to_numpy())
  thisStdR2All = np.std(thisSubset[f'{metricY2All}'].to_numpy())
  if not labeled:
    axd["Grid1296"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, label=f'{xLabel}', c="#069AF3", marker='o')
    axd2Grid1296.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, label=f'{yLabel}', c="#F97306", marker='o')
    axd["Grid1296"].errorbar(1-ratio, thisAvgRMSEAll, yerr=thisStdRMSEAll, label=f'{xLabelAll}', c="#069AF3", marker='P')
    axd2Grid1296.errorbar(1-ratio, thisAvgR2All, yerr=thisStdR2All, label=f'{yLabelAll}', c="#F97306", marker='P')
  else:
    axd["Grid1296"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, c="#069AF3", marker='o')
    axd2Grid1296.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, c="#F97306", marker='o')
    axd["Grid1296"].errorbar(1-ratio, thisAvgRMSEAll, yerr=thisStdRMSEAll, c="#069AF3", marker='P')
    axd2Grid1296.errorbar(1-ratio, thisAvgR2All, yerr=thisStdR2All, c="#F97306", marker='P')
    
  thisSubset = subsetGrid2401[subsetGrid2401["ratio"] == ratio]
  thisAvgRMSE = np.mean(thisSubset[f'{metricY1}'].to_numpy())
  thisStdRMSE = np.std(thisSubset[f'{metricY1}'].to_numpy())
  thisAvgR2 = np.mean(thisSubset[f'{metricY2}'].to_numpy())
  thisStdR2 = np.std(thisSubset[f'{metricY2}'].to_numpy())
  thisAvgRMSEAll = np.mean(thisSubset[f'{metricY1All}'].to_numpy())
  thisStdRMSEAll = np.std(thisSubset[f'{metricY1All}'].to_numpy())
  thisAvgR2All = np.mean(thisSubset[f'{metricY2All}'].to_numpy())
  thisStdR2All = np.std(thisSubset[f'{metricY2All}'].to_numpy())
  if not labeled:
    axd["Grid2401"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, label=f'{xLabel}', c="#069AF3", marker='o')
    axd2Grid2401.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, label=f'{yLabel}', c="#F97306", marker='o')
    axd["Grid2401"].errorbar(1-ratio, thisAvgRMSEAll, yerr=thisStdRMSEAll, label=f'{xLabelAll}', c="#069AF3", marker='P')
    axd2Grid2401.errorbar(1-ratio, thisAvgR2All, yerr=thisStdR2All, label=f'{yLabelAll}', c="#F97306", marker='P')
  else:
    axd["Grid2401"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, c="#069AF3", marker='o')
    axd2Grid2401.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, c="#F97306", marker='o')
    axd["Grid2401"].errorbar(1-ratio, thisAvgRMSEAll, yerr=thisStdRMSEAll, c="#069AF3", marker='P')
    axd2Grid2401.errorbar(1-ratio, thisAvgR2All, yerr=thisStdR2All, c="#F97306", marker='P')
    
  thisSubset = subsetSobol1[subsetSobol1["ratio"] == ratio]
  thisAvgRMSE = np.mean(thisSubset[f'{metricY1}'].to_numpy())
  thisStdRMSE = np.std(thisSubset[f'{metricY1}'].to_numpy())
  thisAvgR2 = np.mean(thisSubset[f'{metricY2}'].to_numpy())
  thisStdR2 = np.std(thisSubset[f'{metricY2}'].to_numpy())
  thisAvgRMSEAll = np.mean(thisSubset[f'{metricY1All}'].to_numpy())
  thisStdRMSEAll = np.std(thisSubset[f'{metricY1All}'].to_numpy())
  thisAvgR2All = np.mean(thisSubset[f'{metricY2All}'].to_numpy())
  thisStdR2All = np.std(thisSubset[f'{metricY2All}'].to_numpy())
  if not labeled:
    axd["Sobol1"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, label=f'{xLabel}', c="#069AF3", marker='o')
    axd2Sobol1.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, label=f'{yLabel}', c="#F97306", marker='o')
    axd["Sobol1"].errorbar(1-ratio, thisAvgRMSEAll, yerr=thisStdRMSEAll, label=f'{xLabelAll}', c="#069AF3", marker='P')
    axd2Sobol1.errorbar(1-ratio, thisAvgR2All, yerr=thisStdR2All, label=f'{yLabelAll}', c="#F97306", marker='P')
  else:
    axd["Sobol1"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, c="#069AF3", marker='o')
    axd2Sobol1.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, c="#F97306", marker='o')
    axd["Sobol1"].errorbar(1-ratio, thisAvgRMSEAll, yerr=thisStdRMSEAll, c="#069AF3", marker='P')
    axd2Sobol1.errorbar(1-ratio, thisAvgR2All, yerr=thisStdR2All, c="#F97306", marker='P')
    
  thisSubset = subsetSobol2[subsetSobol2["ratio"] == ratio]
  thisAvgRMSE = np.mean(thisSubset[f'{metricY1}'].to_numpy())
  thisStdRMSE = np.std(thisSubset[f'{metricY1}'].to_numpy())
  thisAvgR2 = np.mean(thisSubset[f'{metricY2}'].to_numpy())
  thisStdR2 = np.std(thisSubset[f'{metricY2}'].to_numpy())
  thisAvgRMSEAll = np.mean(thisSubset[f'{metricY1All}'].to_numpy())
  thisStdRMSEAll = np.std(thisSubset[f'{metricY1All}'].to_numpy())
  thisAvgR2All = np.mean(thisSubset[f'{metricY2All}'].to_numpy())
  thisStdR2All = np.std(thisSubset[f'{metricY2All}'].to_numpy())
  if not labeled:
    axd["Sobol2"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, label=f'{xLabel}', c="#069AF3", marker='o')
    axd2Sobol2.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, label=f'{yLabel}', c="#F97306", marker='o')
    axd["Sobol2"].errorbar(1-ratio, thisAvgRMSEAll, yerr=thisStdRMSEAll, label=f'{xLabelAll}', c="#069AF3", marker='P')
    axd2Sobol2.errorbar(1-ratio, thisAvgR2All, yerr=thisStdR2All, label=f'{yLabelAll}', c="#F97306", marker='P')
  else:
    axd["Sobol2"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, c="#069AF3", marker='o')
    axd2Sobol2.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, c="#F97306", marker='o')
    axd["Sobol2"].errorbar(1-ratio, thisAvgRMSEAll, yerr=thisStdRMSEAll, c="#069AF3", marker='P')
    axd2Sobol2.errorbar(1-ratio, thisAvgR2All, yerr=thisStdR2All, c="#F97306", marker='P')
    
  labeled = True
  
axd["Grid1296"].legend(bbox_to_anchor=(0.45,0.99))
#axd["Grid1296"].set_xlabel("% of Dataset used for Training")
axd["Grid1296"].set_ylabel(f'{xLabel}', c="#069AF3", fontweight='bold')
axd["Grid1296"].set_title("Training dataset: Grid1296")
axd["Grid1296"].set_ylim([minMetric1, maxMetric1])
axd["Grid1296"].tick_params(axis='y', color="#069AF3", which='both')
axd["Grid1296"].spines['left'].set_color("#069AF3")
axd2Grid1296.legend(bbox_to_anchor=(0.95,0.99))
#axd2Grid1296.set_ylabel(f'{yLabel}', c="#F97306")
axd2Grid1296.set_ylim([minMetric2, maxMetric2])
axd2Grid1296.spines['left'].set_color("#069AF3")
axd2Grid1296.spines['right'].set_color("#F97306")
axd2Grid1296.tick_params(axis='y', color="#F97306", which='both')


axd["Grid2401"].legend(bbox_to_anchor=(0.45,0.99))
axd["Grid2401"].set_xlabel("% of Dataset used for Training", fontweight='bold')
axd["Grid2401"].set_ylabel(f'{xLabel}', c="#069AF3", fontweight='bold')
axd["Grid2401"].set_title("Training dataset: Grid2401")
axd["Grid2401"].set_ylim([minMetric1, maxMetric1])
axd["Grid2401"].tick_params(axis='y', color="#069AF3", which='both')
axd["Grid2401"].spines['left'].set_color("#069AF3")
axd2Grid2401.legend(bbox_to_anchor=(0.95,0.99))
#axd2Grid2401.set_ylabel(f'{yLabel}', c="#F97306")
axd2Grid2401.set_ylim([minMetric2, maxMetric2])
axd2Grid2401.spines['left'].set_color("#069AF3")
axd2Grid2401.spines['right'].set_color("#F97306")
axd2Grid2401.tick_params(axis='y', color="#F97306", which='both')

axd["Sobol1"].legend(bbox_to_anchor=(0.45,0.99))
#axd["Sobol1"].set_xlabel("% of Dataset used for Training")
#axd["Sobol1"].set_ylabel(f'{xLabel}', c="#069AF3")
axd["Sobol1"].set_title("Training dataset: Sobol1")
axd["Sobol1"].set_ylim([minMetric1, maxMetric1])
axd["Sobol1"].tick_params(axis='y', color="#069AF3", which='both')
axd["Sobol1"].spines['left'].set_color("#069AF3")
axd2Sobol1.legend(bbox_to_anchor=(0.95,0.99))
axd2Sobol1.set_ylabel(f'{yLabel}', c="#F97306", fontweight='bold')
axd2Sobol1.set_ylim([minMetric2, maxMetric2])
axd2Sobol1.spines['left'].set_color("#069AF3")
axd2Sobol1.spines['right'].set_color("#F97306")
axd2Sobol1.tick_params(axis='y', color="#F97306", which='both')

axd["Sobol2"].legend(bbox_to_anchor=(0.45,0.99))
axd["Sobol2"].set_xlabel("% of Dataset used for Training", fontweight='bold')
#axd["Sobol2"].set_ylabel(f'{xLabel}', c="#069AF3")
axd["Sobol2"].set_title("Training dataset: Sobol2")
axd["Sobol2"].set_ylim([minMetric1, maxMetric1])
axd["Sobol2"].tick_params(axis='y', color="#069AF3", which='both')
axd["Sobol2"].spines['left'].set_color("#069AF3")
axd2Sobol2.legend(bbox_to_anchor=(0.95,0.99))
axd2Sobol2.set_ylabel(f'{yLabel}', c="#F97306", fontweight='bold')
axd2Sobol2.set_ylim([minMetric2, maxMetric2])
axd2Sobol2.spines['left'].set_color("#069AF3")
axd2Sobol2.spines['right'].set_color("#F97306")
axd2Sobol2.tick_params(axis='y', color="#F97306", which='both')

plt.tight_layout()

if saveOrShow == "show":
  plt.show()
elif saveOrShow == "save":
  plt.savefig(f'Ratio-vs-MAPE_R2.png', dpi=100, format='png')

























