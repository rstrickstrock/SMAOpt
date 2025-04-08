import matplotlib.pyplot as plt
import pandas as pd

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
  metric1All = "mape_all"
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
  maxMETRIC1 = 0.15 
  minMETRIC1 = 0.00 
elif metric1 is "r2":
  metric1All = "r2_all"
  xLabel = "R²"
  #xLabelAll = "R2_ALL"
  maxMETRIC1 = 1.05
  minMETRIC1 = -1.05
else:
  print(f'Please set \'metric1\' to "rmse", "r2" or "mape". (Is: {metric1}). Exit.')
  exit()
  
if metric2 is "rmse":
  metric2All = "rmse_all"
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
  metric2All = "mape_all"
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
  metric2All = "r2_all"
  yLabel = "R²"
  #yLabelAll = "R2_ALL"
  maxMETRIC2 = 1.05
  minMETRIC2 = -1.05
else:
  print(f'Please set \'metric2\' to "rmse", "r2" or "mape". (Is: {metric2}). Exit.')
  exit()


subsetGrid1296 = dfStatistics[dfStatistics["dataset"] == "Grid1296"]
subsetGrid2401 = dfStatistics[dfStatistics["dataset"] == "Grid2401"]
subsetSobol1 = dfStatistics[dfStatistics["dataset"] == "Sobol1"]
subsetSobol2 = dfStatistics[dfStatistics["dataset"] == "Sobol2"]

## plots
gs_kw = dict(width_ratios=[2, 1, 1], height_ratios=[1, 1])
fig, axd = plt.subplot_mosaic([['AllInOne', 'Grid1296', 'Sobol1'], 
                               ['AllInOne', 'Grid2401', 'Sobol2']], 
                               gridspec_kw=gs_kw, figsize=(18.0, 9.0))

axd["AllInOne"].scatter(subsetGrid1296[f'{metric1}'], subsetGrid1296[f'{metric2}'], label="Trainingdata: Grid1296", c="#332288", marker='o', edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetGrid2401[f'{metric1}'], subsetGrid2401[f'{metric2}'], label="Trainingdata: Grid2401", c="#88CCEE", marker='o', edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetSobol1[f'{metric1}'], subsetSobol1[f'{metric2}'], label="Trainingdata: Sobol1", c="#DDCC77", marker='o', edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetSobol2[f'{metric1}'], subsetSobol2[f'{metric2}'], label="Trainingdata: Sobol2", c="#117733", marker='o', edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetGrid1296[f'{metric1All}'], subsetGrid1296[f'{metric2All}'], label="Grid1296, interpolation test", c="#332288", marker='P')#, edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetGrid2401[f'{metric1All}'], subsetGrid2401[f'{metric2All}'], label="Grid2401, interpolation test", c="#88CCEE", marker='P')#, edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetSobol1[f'{metric1All}'], subsetSobol1[f'{metric2All}'], label="Sobol1, interpolation test", c="#DDCC77", marker='P')#, edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetSobol2[f'{metric1All}'], subsetSobol2[f'{metric2All}'], label="Sobol2, interpolation test", c="#117733", marker='P')#, edgecolor="#44AA99")
axd["AllInOne"].legend()
#axd["AllInOne"].set(xlabel=f'{xLabel}', ylabel=f'{yLabel}')
axd["AllInOne"].set_xlabel(f'{xLabel}', fontweight='bold')
axd["AllInOne"].set_ylabel(f'R²', fontweight='bold')
#axd["AllInOne"].set_title("All In One", fontweight='bold')
axd["AllInOne"].set_xlim([minMETRIC1, maxMETRIC1])
axd["AllInOne"].set_ylim([minMETRIC2, maxMETRIC2])

axd["Grid1296"].scatter(subsetGrid1296[f'{metric1}'], subsetGrid1296[f'{metric2}'], label="Testdata: from Grid1296", c="#332288", marker='o', edgecolor="#44AA99")
axd["Grid1296"].scatter(subsetGrid1296[f'{metric1All}'], subsetGrid1296[f'{metric2All}'], label="Testdata: all other datasets", c="#332288", marker='P')#, edgecolor="#44AA99")
axd["Grid1296"].legend()
axd["Grid1296"].set_ylabel(f'R²', fontweight='bold')
axd["Grid1296"].set_title("Trainingdata: Grid1296")
axd["Grid1296"].set_xlim([minMETRIC1, maxMETRIC1])
axd["Grid1296"].set_ylim([minMETRIC2, maxMETRIC2])

axd["Grid2401"].scatter(subsetGrid2401[f'{metric1}'], subsetGrid2401[f'{metric2}'], label="Testdata: from Grid2401", c="#88CCEE", marker='o', edgecolor="#44AA99")
axd["Grid2401"].scatter(subsetGrid2401[f'{metric1All}'], subsetGrid2401[f'{metric2All}'], label="Testdata: all other datasets", c="#88CCEE", marker='P')#, edgecolor="#44AA99")
axd["Grid2401"].legend()
axd["Grid2401"].set_xlabel(f'{xLabel}', fontweight='bold')
axd["Grid2401"].set_ylabel(f'R²', fontweight='bold')
axd["Grid2401"].set_title("Trainingdata: Grid2401")
axd["Grid2401"].set_xlim([minMETRIC1, maxMETRIC1])
axd["Grid2401"].set_ylim([minMETRIC2, maxMETRIC2])

axd["Sobol1"].scatter(subsetSobol1[f'{metric1}'], subsetSobol1[f'{metric2}'], label="Testdata: from Sobol1", c="#DDCC77", marker='o', edgecolor="#44AA99")
axd["Sobol1"].scatter(subsetSobol1[f'{metric1All}'], subsetSobol1[f'{metric2All}'], label="Testdata: all other datasets", c="#DDCC77", marker='P')#, edgecolor="#44AA99")
axd["Sobol1"].legend()
axd["Sobol1"].set_title("Trainingdata: Sobol1")
axd["Sobol1"].set_xlim([minMETRIC1, maxMETRIC1])
axd["Sobol1"].set_ylim([minMETRIC2, maxMETRIC2])

axd["Sobol2"].scatter(subsetSobol2[f'{metric1}'], subsetSobol2[f'{metric2}'], label="Testdata: from Sobol2", c="#117733", marker='o', edgecolor="#44AA99")
axd["Sobol2"].scatter(subsetSobol2[f'{metric1All}'], subsetSobol2[f'{metric2All}'], label="Testdata: all other datasets", c="#117733", marker='P')#, edgecolor="#44AA99")
axd["Sobol2"].legend()
axd["Sobol2"].set_xlabel(f'{xLabel}', fontweight='bold')
axd["Sobol2"].set_title("Trainingdata: Sobol2")
axd["Sobol2"].set_xlim([minMETRIC1, maxMETRIC1])
axd["Sobol2"].set_ylim([minMETRIC2, maxMETRIC2])

plt.tight_layout()

if saveOrShow == "show":
  plt.show()
elif saveOrShow == "save":
  plt.savefig(f'MAPE-vs-R2_polyRegr.png', dpi=100, format='png')



























