import matplotlib.pyplot as plt
import pandas as pd
import sys

import os
import glob


statisticsFile = 'Stats.csv'
#metrictype = "rmse"
metrictype = "mape"

try:
  saveOrShow = sys.argv[1]
except:
  saveOrShow = "show"
if saveOrShow == "save":
  pass
else:
  saveOrShow = "show"

if metrictype is "rmse":
  xLabel = "RMSE"
  metrictypeAll = "rmse_all"
elif metrictype is "mape":
  xLabel = "MAPE"
  metrictypeAll = "mape_all"
else:
  print(f'Please set \'metrictype\' to "rmse" or "mape". (Is: {metrictype}). Exit.')
  exit()
  
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

maxMETRIC1 = 0.15 
minMETRIC1 = 0.02 
maxMETRIC2 = 1.05
minMETRIC2 = -0.05

subsetGrid1296 = dfStatistics[dfStatistics["dataset"] == "Grid1296"]
subsetGrid2401 = dfStatistics[dfStatistics["dataset"] == "Grid2401"]
subsetSobol1 = dfStatistics[dfStatistics["dataset"] == "Sobol1"]
subsetSobol2 = dfStatistics[dfStatistics["dataset"] == "Sobol2"]

## plots
gs_kw = dict(width_ratios=[2, 1, 1], height_ratios=[1, 1])
fig, axd = plt.subplot_mosaic([['AllInOne', 'Grid1296', 'Sobol1'], 
                               ['AllInOne', 'Grid2401', 'Sobol2']], 
                               gridspec_kw=gs_kw, figsize=(18.0, 9.0))

axd["AllInOne"].scatter(subsetGrid1296[f'{metrictype}'], subsetGrid1296["r2"], label="Trainingdata: Grid1296", c="#332288", marker='o', edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetGrid2401[f'{metrictype}'], subsetGrid2401["r2"], label="Trainingdata: Grid2401", c="#88CCEE", marker='o', edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetSobol1[f'{metrictype}'], subsetSobol1["r2"], label="Trainingdata: Sobol1", c="#DDCC77", marker='o', edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetSobol2[f'{metrictype}'], subsetSobol2["r2"], label="Trainingdata: Sobol2", c="#117733", marker='o', edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetGrid1296[f'{metrictypeAll}'], subsetGrid1296["r2_all"], label="Grid1296, interpolation test", c="#332288", marker='P')#, edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetGrid2401[f'{metrictypeAll}'], subsetGrid2401["r2_all"], label="Grid2401, interpolation test", c="#88CCEE", marker='P')#, edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetSobol1[f'{metrictypeAll}'], subsetSobol1["r2_all"], label="Sobol1, interpolation test", c="#DDCC77", marker='P')#, edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetSobol2[f'{metrictypeAll}'], subsetSobol2["r2_all"], label="Sobol2, interpolation test", c="#117733", marker='P')#, edgecolor="#44AA99")
axd["AllInOne"].legend()
#axd["AllInOne"].set(xlabel=f'{xLabel}', ylabel=, fontweight='bold')
axd["AllInOne"].set_xlabel(f'{xLabel}', fontweight='bold')
axd["AllInOne"].set_ylabel(f'R²', fontweight='bold')
#axd["AllInOne"].set_title("All In One", fontweight='bold')
axd["AllInOne"].set_xlim([minMETRIC1, maxMETRIC1])
axd["AllInOne"].set_ylim([minMETRIC2, maxMETRIC2])

axd["Grid1296"].scatter(subsetGrid1296[f'{metrictype}'], subsetGrid1296["r2"], label="Testdata: from Grid1296", c="#332288", marker='o', edgecolor="#44AA99")
axd["Grid1296"].scatter(subsetGrid1296[f'{metrictypeAll}'], subsetGrid1296["r2_all"], label="Testdata: all other datasets", c="#332288", marker='P')#, edgecolor="#44AA99")
axd["Grid1296"].legend()
axd["Grid1296"].set_ylabel(f'R²', fontweight='bold')
axd["Grid1296"].set_title("Trainingdata: Grid1296")
axd["Grid1296"].set_xlim([minMETRIC1, maxMETRIC1])
axd["Grid1296"].set_ylim([minMETRIC2, maxMETRIC2])

axd["Grid2401"].scatter(subsetGrid2401[f'{metrictype}'], subsetGrid2401["r2"], label="Testdata: from Grid2401", c="#88CCEE", marker='o', edgecolor="#44AA99")
axd["Grid2401"].scatter(subsetGrid2401[f'{metrictypeAll}'], subsetGrid2401["r2_all"], label="Testdata: all other datasets", c="#88CCEE", marker='P')#, edgecolor="#44AA99")
axd["Grid2401"].legend()
axd["Grid2401"].set_xlabel(f'{xLabel}', fontweight='bold')
axd["Grid2401"].set_ylabel(f'R²', fontweight='bold')
axd["Grid2401"].set_title("Trainingdata: Grid2401")
axd["Grid2401"].set_xlim([minMETRIC1, maxMETRIC1])
axd["Grid2401"].set_ylim([minMETRIC2, maxMETRIC2])

axd["Sobol1"].scatter(subsetSobol1[f'{metrictype}'], subsetSobol1["r2"], label="Testdata: from Sobol1", c="#DDCC77", marker='o', edgecolor="#44AA99")
axd["Sobol1"].scatter(subsetSobol1[f'{metrictypeAll}'], subsetSobol1["r2_all"], label="Testdata: all other datasets", c="#DDCC77", marker='P')#, edgecolor="#44AA99")
axd["Sobol1"].legend()
axd["Sobol1"].set_title("Trainingdata: Sobol1")
axd["Sobol1"].set_xlim([minMETRIC1, maxMETRIC1])
axd["Sobol1"].set_ylim([minMETRIC2, maxMETRIC2])

axd["Sobol2"].scatter(subsetSobol2[f'{metrictype}'], subsetSobol2["r2"], label="Testdata: from Sobol2", c="#117733", marker='o', edgecolor="#44AA99")
axd["Sobol2"].scatter(subsetSobol2[f'{metrictypeAll}'], subsetSobol2["r2_all"], label="Testdata: all other datasets", c="#117733", marker='P')#, edgecolor="#44AA99")
axd["Sobol2"].legend()
axd["Sobol2"].set_xlabel(f'{xLabel}', fontweight='bold')
axd["Sobol2"].set_title("Trainingdata: Sobol2")
axd["Sobol2"].set_xlim([minMETRIC1, maxMETRIC1])
axd["Sobol2"].set_ylim([minMETRIC2, maxMETRIC2])

plt.tight_layout()

if saveOrShow == "show":
  plt.show()
elif saveOrShow == "save":
  plt.savefig(f'MAPE-vs-R2_linRegr.png', dpi=100, format='png')
  























