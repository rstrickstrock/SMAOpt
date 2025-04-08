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


## plots
#cm = plt.get_cmap('RdYlBu')
#cm = plt.get_cmap('viridis')
cm = plt.get_cmap('jet')
#cm = plt.get_cmap('seismic')
#cm = plt.get_cmap('gist_rainbow')
colormin = 600
colormax = 800

Z = np.array(dfData.density)


X = dfData.SigC
Y = dfData.SigH
plt.figure()
sc = plt.scatter(X, Y, c=Z, cmap=cm, vmin=colormin, vmax=colormax)
plt.xlabel("Sigma C [nm]", fontweight='bold')
plt.ylabel("Sigma H [kJ/mol]", fontweight='bold')
cb = plt.colorbar(sc)
cb.set_label(label="Denisty [kg/m³]", weight='bold')
plt.tight_layout()
if saveOrShow == "save":
  plt.savefig(f'HEATMAP_Dataset_{name_dataset}_SigCvsSigH.png')
#if saveOrShow == "show":
#  plt.show()
#  exit()


X = dfData.SigC
Y = dfData.EpsC
plt.figure()
sc = plt.scatter(X, Y, c=Z, cmap=cm, vmin=colormin, vmax=colormax)
plt.xlabel("Sigma C [nm]", fontweight='bold')
plt.ylabel("Epsilon C [kJ/mol]", fontweight='bold')
cb = plt.colorbar(sc)
cb.set_label(label="Denisty [kg/m³]", weight='bold')
plt.tight_layout()
if saveOrShow == "save":
  plt.savefig(f'HEATMAP_Dataset_{name_dataset}_SigCvsEpsC.png')

X = dfData.SigC
Y = dfData.EpsH
plt.figure()
sc = plt.scatter(X, Y, c=Z, cmap=cm, vmin=colormin, vmax=colormax)
plt.xlabel("Sigma C [nm]", fontweight='bold')
plt.ylabel("Epsilon H [kJ/mol]", fontweight='bold')
cb = plt.colorbar(sc)
cb.set_label(label="Denisty [kg/m³]", weight='bold')
plt.tight_layout()
if saveOrShow == "save":
  plt.savefig(f'HEATMAP_Dataset_{name_dataset}_SigCvsEpsH.png')

X = dfData.SigH
Y = dfData.EpsC
plt.figure()
sc = plt.scatter(X, Y, c=Z, cmap=cm, vmin=colormin, vmax=colormax)
plt.xlabel("Sigma H [nm]", fontweight='bold')
plt.ylabel("Epsilon C [kJ/mol]", fontweight='bold')
cb = plt.colorbar(sc)
cb.set_label(label="Denisty [kg/m³]", weight='bold')
plt.tight_layout()
if saveOrShow == "save":
  plt.savefig(f'HEATMAP_Dataset_{name_dataset}_SigHvsEpsC.png')

X = dfData.SigH
Y = dfData.EpsH
plt.figure()
sc = plt.scatter(X, Y, c=Z, cmap=cm, vmin=colormin, vmax=colormax)
plt.xlabel("Sigma H [nm]", fontweight='bold')
plt.ylabel("Epsilon H [kJ/mol]", fontweight='bold')
cb = plt.colorbar(sc)
cb.set_label(label="Denisty [kg/m³]", weight='bold')
plt.tight_layout()
if saveOrShow == "save":
  plt.savefig(f'HEATMAP_Dataset_{name_dataset}_SigHvsEpsH.png')

X = dfData.EpsC
Y = dfData.EpsH
plt.figure()
sc = plt.scatter(X, Y, c=Z, cmap=cm, vmin=colormin, vmax=colormax)
plt.xlabel("Epsilon C [kJ/mol]", fontweight='bold')
plt.ylabel("Epsilon H [kJ/mol]", fontweight='bold')
cb = plt.colorbar(sc)
cb.set_label(label="Denisty [kg/m³]", weight='bold')
plt.tight_layout()
if saveOrShow == "save":
  plt.savefig(f'HEATMAP_Dataset_{name_dataset}_EpsCvsEpsH.png')

if saveOrShow == "show":
  plt.show()
