import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

try:
  saveOrShow = sys.argv[1]
except:
  saveOrShow = "show"
if saveOrShow == "save":
  pass
else:
  saveOrShow = "show"

dfResults1296 = pd.read_csv("RESULTS_gridsearch_1296.csv")
dfResults1296 = dfResults1296.drop(columns='Unnamed: 0')
dfResults2401 = pd.read_csv("RESULTS_gridsearch_2401.csv")
dfResults2401 = dfResults2401.drop(columns='Unnamed: 0')
dfResultsSobol1 = pd.read_csv("RESULTS_sobolsampling-2048.csv")
dfResultsSobol1 = dfResultsSobol1.drop(columns='Unnamed: 0')
dfResultsSobol2 = pd.read_csv("RESULTS_sobolsampling-2048-2.csv")
dfResultsSobol2 = dfResultsSobol2.drop(columns='Unnamed: 0')

dfCleaned1296 = pd.read_csv("CLEANED_gridsearch_1296.csv")
dfCleaned1296 = dfCleaned1296.drop(columns='Unnamed: 0')
dfCleaned2401 = pd.read_csv("CLEANED_gridsearch_2401.csv")
dfCleaned2401 = dfCleaned2401.drop(columns='Unnamed: 0')
dfCleanedSobol1 = pd.read_csv("CLEANED_sobolsampling-2048.csv")
dfCleanedSobol1 = dfCleanedSobol1.drop(columns='Unnamed: 0')
dfCleanedSobol2 = pd.read_csv("CLEANED_sobolsampling-2048-2.csv")
dfCleanedSobol2 = dfCleanedSobol2.drop(columns='Unnamed: 0')

figDPI = 300
#print(f'{dfResults1296}')
#print(f'{dfCleaned1296}')
ymin = 0
ymax = 1000
yTicks = [100, 300, 500, 700, 900]
yLabels = ["100", "300", "500", "700", "900"]

colnames = dfResults1296.iloc[0:6,0]
#print(f'{colnames}')

cols = []
for i in range(0,5):
    #print(f'{colnames[i]}')
    cols.append(colnames[i])
#print(f'{cols}')

thisDF = pd.DataFrame({"SigC": [],
                       "SigH": [],
                       "EpsC": [],
                       "EpsH": [],
                       "density": []})
for i in range(1, dfResults1296.shape[1]):
    d = dfResults1296.iloc[0:5,i]
    #print(f'{d.iloc[0]}')
    tmpDF = pd.DataFrame({"SigC": [d.iloc[0]],
                          "SigH": [d.iloc[1]],
                          "EpsC": [d.iloc[2]],
                          "EpsH": [d.iloc[3]],
                          "density": [d.iloc[4]]})
    thisDF = pd.concat([thisDF, tmpDF], ignore_index=True)
#print(f'{thisDF}')
dfResults1296 = thisDF

thisDF = pd.DataFrame({"SigC": [],
                       "SigH": [],
                       "EpsC": [],
                       "EpsH": [],
                       "density": []})
for i in range(1, dfResults2401.shape[1]):
    d = dfResults2401.iloc[0:5,i]
    #print(f'{d.iloc[0]}')
    tmpDF = pd.DataFrame({"SigC": [d.iloc[0]],
                          "SigH": [d.iloc[1]],
                          "EpsC": [d.iloc[2]],
                          "EpsH": [d.iloc[3]],
                          "density": [d.iloc[4]]})
    thisDF = pd.concat([thisDF, tmpDF], ignore_index=True)
dfResults2401 = thisDF

thisDF = pd.DataFrame({"SigC": [],
                       "SigH": [],
                       "EpsC": [],
                       "EpsH": [],
                       "density": []})
for i in range(1, dfResultsSobol1.shape[1]):
    d = dfResultsSobol1.iloc[0:5,i]
    #print(f'{d.iloc[0]}')
    tmpDF = pd.DataFrame({"SigC": [d.iloc[0]],
                          "SigH": [d.iloc[1]],
                          "EpsC": [d.iloc[2]],
                          "EpsH": [d.iloc[3]],
                          "density": [d.iloc[4]]})
    thisDF = pd.concat([thisDF, tmpDF], ignore_index=True)
dfResultsSobol1 = thisDF

thisDF = pd.DataFrame({"SigC": [],
                       "SigH": [],
                       "EpsC": [],
                       "EpsH": [],
                       "density": []})
for i in range(1, dfResultsSobol2.shape[1]):
    d = dfResultsSobol2.iloc[0:5,i]
    #print(f'{d.iloc[0]}')
    tmpDF = pd.DataFrame({"SigC": [d.iloc[0]],
                          "SigH": [d.iloc[1]],
                          "EpsC": [d.iloc[2]],
                          "EpsH": [d.iloc[3]],
                          "density": [d.iloc[4]]})
    thisDF = pd.concat([thisDF, tmpDF], ignore_index=True)
dfResultsSobol2 = thisDF


violin_plot = sns.violinplot(data=dfResults1296["density"])
violin_plot.set_xlabel('Frequency Of Occurrence', fontweight='bold', fontsize=15)
violin_plot.set_ylabel('Density [kg/m³]', fontweight='bold', fontsize=18)
violin_plot.set_ylim([ymin, ymax])
violin_plot.set_yticks(yTicks)
violin_plot.set_yticklabels(yLabels, fontweight='bold', fontsize=15)
fig = violin_plot.get_figure()
plt.tight_layout()
if saveOrShow == "save":
  plt.savefig(f'violinplotDensityGrid1296_all.png', dpi=figDPI, format='png')

plt.figure()  
violin_plot = sns.violinplot(data=dfResults2401["density"])
violin_plot.set_xlabel('Frequency Of Occurrence', fontweight='bold', fontsize=15)
violin_plot.set_ylabel('Density [kg/m³]', fontweight='bold', fontsize=18)
violin_plot.set_ylim([ymin, ymax])
violin_plot.set_yticks(yTicks)
violin_plot.set_yticklabels(yLabels, fontweight='bold', fontsize=15)
fig = violin_plot.get_figure()
plt.tight_layout()
if saveOrShow == "save":
  plt.savefig(f'violinplotDensityGrid2401_all.png', dpi=figDPI, format='png')
  
plt.figure()
violin_plot = sns.violinplot(data=dfResultsSobol1["density"])
violin_plot.set_xlabel('Frequency Of Occurrence', fontweight='bold', fontsize=15)
violin_plot.set_ylabel('Density [kg/m³]', fontweight='bold', fontsize=18)
violin_plot.set_ylim([ymin, ymax])
violin_plot.set_yticks(yTicks)
violin_plot.set_yticklabels(yLabels, fontweight='bold', fontsize=15)
fig = violin_plot.get_figure()
plt.tight_layout()
if saveOrShow == "save":
  plt.savefig(f'violinplotDensitySobol1_all.png', dpi=figDPI, format='png')

plt.figure()
violin_plot = sns.violinplot(data=dfResultsSobol2["density"])
violin_plot.set_xlabel('Frequency Of Occurrence', fontweight='bold', fontsize=15)
violin_plot.set_ylabel('Density [kg/m³]', fontweight='bold', fontsize=18)
violin_plot.set_ylim([ymin, ymax])
violin_plot.set_yticks(yTicks)
violin_plot.set_yticklabels(yLabels, fontweight='bold', fontsize=15)
fig = violin_plot.get_figure()
plt.tight_layout()
if saveOrShow == "save":
  plt.savefig(f'violinplotDensitySobol2_all.png', dpi=figDPI, format='png')



plt.figure()
violin_plot = sns.violinplot(data=dfCleaned1296["density"])
violin_plot.set_xlabel('Frequency Of Occurrence', fontweight='bold', fontsize=15)
violin_plot.set_ylabel('Density [kg/m³]', fontweight='bold', fontsize=18)
violin_plot.set_ylim([ymin, ymax])
violin_plot.set_yticks(yTicks)
violin_plot.set_yticklabels(yLabels, fontweight='bold', fontsize=15)
fig = violin_plot.get_figure()
plt.tight_layout()
if saveOrShow == "save":
  plt.savefig(f'violinplotDensityGrid1296_preprocessed.png', dpi=figDPI, format='png')

plt.figure()  
violin_plot = sns.violinplot(data=dfCleaned2401["density"])
violin_plot.set_xlabel('Frequency Of Occurrence', fontweight='bold', fontsize=15)
violin_plot.set_ylabel('Density [kg/m³]', fontweight='bold', fontsize=18)
violin_plot.set_ylim([ymin, ymax])
violin_plot.set_yticks(yTicks)
violin_plot.set_yticklabels(yLabels, fontweight='bold', fontsize=15)
fig = violin_plot.get_figure()
plt.tight_layout()
if saveOrShow == "save":
  plt.savefig(f'violinplotDensityGrid2401_preprocessed.png', dpi=figDPI, format='png')
  
plt.figure()
violin_plot = sns.violinplot(data=dfCleanedSobol1["density"])
violin_plot.set_xlabel('Frequency Of Occurrence', fontweight='bold', fontsize=15)
violin_plot.set_ylabel('Density [kg/m³]', fontweight='bold', fontsize=18)
violin_plot.set_ylim([ymin, ymax])
violin_plot.set_yticks(yTicks)
violin_plot.set_yticklabels(yLabels, fontweight='bold', fontsize=15)
fig = violin_plot.get_figure()
plt.tight_layout()
if saveOrShow == "save":
  plt.savefig(f'violinplotDensitySobol1_preprocessed.png', dpi=figDPI, format='png')

plt.figure()
violin_plot = sns.violinplot(data=dfCleanedSobol2["density"])
violin_plot.set_xlabel('Frequency Of Occurrence', fontweight='bold', fontsize=15)
violin_plot.set_ylabel('Density [kg/m³]', fontweight='bold', fontsize=18)
violin_plot.set_ylim([ymin, ymax])
violin_plot.set_yticks(yTicks)
violin_plot.set_yticklabels(yLabels, fontweight='bold', fontsize=15)
fig = violin_plot.get_figure()
plt.tight_layout()
if saveOrShow == "save":
  plt.savefig(f'violinplotDensitySobol2_preprocessed.png', dpi=figDPI, format='png')

if saveOrShow == "show":
  plt.show()





























