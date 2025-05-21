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

dfData = pd.read_csv("CLEANED_sobolsampling-2048.csv")
name_dataset = "Sobol1"
#print(f'{dfData}')
dfData = dfData.drop(columns='Unnamed: 0')
#print(f'{dfData}')
figDPI = 300

## plots
#cm = plt.get_cmap('RdYlBu')
#cm = plt.get_cmap('viridis')
cm = plt.get_cmap('jet')
#cm = plt.get_cmap('seismic')
#cm = plt.get_cmap('gist_rainbow')
colormin = 600
colormax = 800

sigCTicks = [0.05, 0.15, 0.25, 0.35]
sigHTicks = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30]
epsCTicks = [0.20, 0.50, 0.80, 1.10]
epsHTicks = [0.02, 0.06, 0.10, 0.14]
cbTicks = [600, 650, 700, 750, 800]
cbTickLabels = ["600", "650", "700", "750", "800"]
Z = np.array(dfData.density)


X = dfData.SigC
Y = dfData.SigH
plt.figure()
sc = plt.scatter(X, Y, c=Z, cmap=cm, vmin=colormin, vmax=colormax)
plt.xlabel("Sigma C [nm]", fontweight='bold', fontsize=18)
plt.ylabel("Sigma H [kJ/mol]", fontweight='bold', fontsize=18)
plt.xticks(sigCTicks, fontsize=15)
plt.yticks(sigHTicks, fontsize=15)
cb = plt.colorbar(sc)
cb.set_label(label="Denisty [kg/m³]", weight='bold', fontsize=18)
cb.set_ticks(cbTicks)
cb.set_ticklabels(cbTickLabels, fontsize=12)
plt.tight_layout()
if saveOrShow == "save":
  plt.savefig(f'HEATMAP_Dataset_{name_dataset}_SigCvsSigH.png', dpi=figDPI, format='png')
#if saveOrShow == "show":
#  plt.show()
#  exit()


X = dfData.SigC
Y = dfData.EpsC
plt.figure()
sc = plt.scatter(X, Y, c=Z, cmap=cm, vmin=colormin, vmax=colormax)
plt.xlabel("Sigma C [nm]", fontweight='bold', fontsize=18)
plt.ylabel("Epsilon C [kJ/mol]", fontweight='bold', fontsize=18)
plt.xticks(sigCTicks, fontsize=15)
plt.yticks(epsCTicks, fontsize=15)
cb = plt.colorbar(sc)
cb.set_label(label="Denisty [kg/m³]", weight='bold', fontsize=18)
cb.set_ticks(cbTicks)
cb.set_ticklabels(cbTickLabels, fontsize=12)
plt.tight_layout()
if saveOrShow == "save":
  plt.savefig(f'HEATMAP_Dataset_{name_dataset}_SigCvsEpsC.png', dpi=figDPI, format='png')

X = dfData.SigC
Y = dfData.EpsH
plt.figure()
sc = plt.scatter(X, Y, c=Z, cmap=cm, vmin=colormin, vmax=colormax)
plt.xlabel("Sigma C [nm]", fontweight='bold', fontsize=18)
plt.ylabel("Epsilon H [kJ/mol]", fontweight='bold', fontsize=18)
plt.xticks(sigCTicks, fontsize=15)
plt.yticks(epsHTicks, fontsize=15)
cb = plt.colorbar(sc)
cb.set_label(label="Denisty [kg/m³]", weight='bold', fontsize=18)
cb.set_ticks(cbTicks)
cb.set_ticklabels(cbTickLabels, fontsize=12)
plt.tight_layout()
if saveOrShow == "save":
  plt.savefig(f'HEATMAP_Dataset_{name_dataset}_SigCvsEpsH.png', dpi=figDPI, format='png')

X = dfData.SigH
Y = dfData.EpsC
plt.figure()
sc = plt.scatter(X, Y, c=Z, cmap=cm, vmin=colormin, vmax=colormax)
plt.xlabel("Sigma H [nm]", fontweight='bold', fontsize=18)
plt.ylabel("Epsilon C [kJ/mol]", fontweight='bold', fontsize=18)
plt.xticks(sigHTicks, fontsize=15)
plt.yticks(epsCTicks, fontsize=15)
cb = plt.colorbar(sc)
cb.set_label(label="Denisty [kg/m³]", weight='bold', fontsize=18)
cb.set_ticks(cbTicks)
cb.set_ticklabels(cbTickLabels, fontsize=12)
plt.tight_layout()
if saveOrShow == "save":
  plt.savefig(f'HEATMAP_Dataset_{name_dataset}_SigHvsEpsC.png', dpi=figDPI, format='png')

X = dfData.SigH
Y = dfData.EpsH
plt.figure()
sc = plt.scatter(X, Y, c=Z, cmap=cm, vmin=colormin, vmax=colormax)
plt.xlabel("Sigma H [nm]", fontweight='bold', fontsize=18)
plt.ylabel("Epsilon H [kJ/mol]", fontweight='bold', fontsize=18)
plt.xticks(sigHTicks, fontsize=15)
plt.yticks(epsHTicks, fontsize=15)
cb = plt.colorbar(sc)
cb.set_label(label="Denisty [kg/m³]", weight='bold', fontsize=18)
cb.set_ticks(cbTicks)
cb.set_ticklabels(cbTickLabels, fontsize=12)
plt.tight_layout()
if saveOrShow == "save":
  plt.savefig(f'HEATMAP_Dataset_{name_dataset}_SigHvsEpsH.png', dpi=figDPI, format='png')

X = dfData.EpsC
Y = dfData.EpsH
plt.figure()
sc = plt.scatter(X, Y, c=Z, cmap=cm, vmin=colormin, vmax=colormax)
plt.xlabel("Epsilon C [kJ/mol]", fontweight='bold', fontsize=18)
plt.ylabel("Epsilon H [kJ/mol]", fontweight='bold', fontsize=18)
plt.xticks(epsCTicks, fontsize=15)
plt.yticks(epsHTicks, fontsize=15)
cb = plt.colorbar(sc)
cb.set_label(label="Denisty [kg/m³]", weight='bold', fontsize=18)
cb.set_ticks(cbTicks)
cb.set_ticklabels(cbTickLabels, fontsize=12)
plt.tight_layout()
if saveOrShow == "save":
  plt.savefig(f'HEATMAP_Dataset_{name_dataset}_EpsCvsEpsH.png', dpi=figDPI, format='png')

if saveOrShow == "show":
  plt.show()
