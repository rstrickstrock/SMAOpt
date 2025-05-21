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

facecolorG1296 = "#332288"
facecolorG2401 = "#88CCEE"
facecolorS1 = "#DDCC77"
facecolorS2 = "#117733"

edgecolor_IST = "#005AB5"
edgecolor_OST = "#DC3220"

edgecolor_IST = "#0ba1e2"
edgecolor_OST = "#e24c0b"
facecolor_IST = "#3ed4ff"
facecolor_OST = "#ff693e"

statisticsFiles = ['02.1_Stats.csv', '02.2_Stats.csv', '02.3_Stats.csv', '02.4_Stats.csv', '02.5_Stats.csv']
MethodName = ['Lin. Regr.', 'Polyn. Regr.', 'RF Regr.', 'GP Regr.', 'NN Regr.']
MethodACR = ['LR', 'PR', 'RFR', 'GPR', 'NNR']

figDPI = 300

minMAPE = -0.005
maxMAPE = 0.13
MAPETicks = [0.00, 0.04, 0.08, 0.10, 0.12]
MAPETickLabels = ["0", "4", "8", "10", "12"]
minR2 = -0.05
maxR2 = 1.05
R2Ticks = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
R2TickLabels = ["0.0", "0.2", "0.4", "0.6", "0.8", "1.0"]

xLabel = 'MAPE'
yLabel = 'R²'
                               

dfStatistics = pd.DataFrame({"ratio": [],
                             "rndint": [],
                             "dataset": [],
                             "mape_ist": [],
                             "r2_ist": [],
                             "mape_ost": [],
                             "r2_ost": []})
                             
dropCols = ['degree', '#trees', 'kernel']

for nMethod in range(0, len(statisticsFiles)):  
  statisticsFile = statisticsFiles[nMethod]
  
  if not os.path.isfile(statisticsFile):
    print(f'Can not find and open \'{statisticsFile}\'. Exit.')
    exit()
  else:
    dfThisStatistics = pd.read_csv(statisticsFile)
    #print(f'{dfThisStatistics}')
    try:
      dfThisStatistics = dfThisStatistics.drop(columns=["Unnamed: 0"])
    except:
      print(f'Something went wrong with\'dfThisStatistics = dfThisStatistics.drop(columns=["Unnamed: 0"])\'.')
    else:
      #print(f'{dfThisStatistics}')
      #exit()
      pass
      
  for colname in dropCols:
    try:
      dfThisStatistics = dfThisStatistics.drop(columns=[f'{colname}'])
    except:
      pass
  #print(f'{dfThisStatistics}')
  #print(f'\n\n\n\n\n\n\n') 
  
  #print(f'{len(dfThisStatistics)}')
  thisMethod = []
  for i in range(0, len(dfThisStatistics)):
    thisMethod.append(MethodACR[nMethod])
    
  dfThisMethod = pd.DataFrame({"method": thisMethod})
  dfThisStatistics = pd.concat([dfThisStatistics, dfThisMethod], axis=1)
  #print(f'{dfThisStatistics}')

  dfStatistics = pd.concat([dfStatistics, dfThisStatistics], ignore_index=True)

#print(f'{dfStatistics}')

subsetGrid1296 = dfStatistics[dfStatistics["dataset"] == "Grid1296"]
subsetGrid2401 = dfStatistics[dfStatistics["dataset"] == "Grid2401"]
subsetSobol1 = dfStatistics[dfStatistics["dataset"] == "Sobol1"]
subsetSobol2 = dfStatistics[dfStatistics["dataset"] == "Sobol2"]


gs_kw = dict(width_ratios=[1, 1], height_ratios=[1, 1])
fig, axd = plt.subplot_mosaic([['Grid1296', 'Sobol1'], 
                               ['Grid2401', 'Sobol2']], 
                               gridspec_kw=gs_kw, figsize=(12.0, 12.0))


axd["Grid1296"].scatter(subsetGrid1296["mape_ist"], subsetGrid1296["r2_ist"], label="in-sample test (IST)", c=facecolor_IST, marker='o', edgecolor=edgecolor_IST)
axd["Grid1296"].scatter(subsetGrid1296["mape_ost"], subsetGrid1296["r2_ost"], label="out-of-sample test (OST)", c=facecolor_OST, marker='P', edgecolor=edgecolor_OST)
axd["Grid1296"].legend()
axd["Grid1296"].set_ylabel(f'{yLabel}', fontweight='bold', fontsize=18)
axd["Grid1296"].set_title("Training data: Grid1296", fontweight='bold', color='gray', fontsize=15)
axd["Grid1296"].set_xlim([minMAPE, maxMAPE])
axd["Grid1296"].set_ylim([minR2, maxR2])
axd["Grid1296"].set_yticks(R2Ticks)
axd["Grid1296"].set_yticklabels(R2TickLabels, fontsize=15)
axd["Grid1296"].set_xticks(MAPETicks)
axd["Grid1296"].set_xticklabels(MAPETickLabels, fontsize=15)
axd["Grid1296"].grid(color='lightgray', linestyle='dotted')

axd["Grid2401"].scatter(subsetGrid2401["mape_ist"], subsetGrid2401["r2_ist"], label="in-sample test (IST)", c=facecolor_IST, marker='o', edgecolor=edgecolor_IST)
axd["Grid2401"].scatter(subsetGrid2401["mape_ost"], subsetGrid2401["r2_ost"], label="out-of-sample test (OST)", c=facecolor_OST, marker='P', edgecolor=edgecolor_OST)
axd["Grid2401"].legend()
axd["Grid2401"].set_xlabel(f'{xLabel} [%]', fontweight='bold', fontsize=18)
axd["Grid2401"].set_ylabel(f'{yLabel}', fontweight='bold', fontsize=18)
axd["Grid2401"].set_title("Training data: Grid2401", fontweight='bold', color='gray', fontsize=15)
axd["Grid2401"].set_xlim([minMAPE, maxMAPE])
axd["Grid2401"].set_ylim([minR2, maxR2])
axd["Grid2401"].set_yticks(R2Ticks)
axd["Grid2401"].set_yticklabels(R2TickLabels, fontsize=15)
axd["Grid2401"].set_xticks(MAPETicks)
axd["Grid2401"].set_xticklabels(MAPETickLabels, fontsize=15)
axd["Grid2401"].grid(color='lightgray', linestyle='dotted')

axd["Sobol1"].scatter(subsetSobol1["mape_ist"], subsetSobol1["r2_ist"], label="in-sample test (IST)", c=facecolor_IST, marker='o', edgecolor=edgecolor_IST)
axd["Sobol1"].scatter(subsetSobol1["mape_ost"], subsetSobol1["r2_ost"], label="out-of-sample test (OST)", c=facecolor_OST, marker='P', edgecolor=edgecolor_OST)
axd["Sobol1"].legend()
axd["Sobol1"].set_title("Training data: Sobol1", fontweight='bold', color='gray', fontsize=15)
axd["Sobol1"].set_xlim([minMAPE, maxMAPE])
axd["Sobol1"].set_ylim([minR2, maxR2])
axd["Sobol1"].set_yticks(R2Ticks)
axd["Sobol1"].set_yticklabels(R2TickLabels, fontsize=15)
axd["Sobol1"].set_xticks(MAPETicks)
axd["Sobol1"].set_xticklabels(MAPETickLabels, fontsize=15)
axd["Sobol1"].grid(color='lightgray', linestyle='dotted')

axd["Sobol2"].scatter(subsetSobol2["mape_ist"], subsetSobol2["r2_ist"], label="in-sample test (IST)", c=facecolor_IST, marker='o', edgecolor=edgecolor_IST)
axd["Sobol2"].scatter(subsetSobol2["mape_ost"], subsetSobol2["r2_ost"], label="out-of-sample test (OST)", c=facecolor_OST, marker='P', edgecolor=edgecolor_OST)
axd["Sobol2"].legend()
axd["Sobol2"].set_xlabel(f'{xLabel} [%]', fontweight='bold', fontsize=18)
axd["Sobol2"].set_title("Training data: Sobol2", fontweight='bold', color='gray', fontsize=15)
axd["Sobol2"].set_xlim([minMAPE, maxMAPE])
axd["Sobol2"].set_ylim([minR2, maxR2])
axd["Sobol2"].set_yticks(R2Ticks)
axd["Sobol2"].set_yticklabels(R2TickLabels, fontsize=15)
axd["Sobol2"].set_xticks(MAPETicks)
axd["Sobol2"].set_xticklabels(MAPETickLabels, fontsize=15)
axd["Sobol2"].grid(color='lightgray', linestyle='dotted')

plt.tight_layout()

if saveOrShow == "show":
  plt.show()
elif saveOrShow == "save":
  plt.savefig(f'MAPE-vs-R2_allMethods.png', dpi=figDPI, format='png')


    
    
    
    
    
    
    

