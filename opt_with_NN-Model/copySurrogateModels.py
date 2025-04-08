import os
import glob
import shutil

maxR2Models = "/home/rstric2s/current_sim/Paper_Octane-3_NN-predictor/ML_density-model/02.5_neuralNetworkPerceptron/bestTrainedModels/maxR2"
minMAPEModels = "/home/rstric2s/current_sim/Paper_Octane-3_NN-predictor/ML_density-model/02.5_neuralNetworkPerceptron/bestTrainedModels/minMAPE"
logFile = "log_copySurrogateModels.log"

if os.path.exists(logFile):
  os.remove(logFile)
with open(logFile, 'w') as f:
  f.write(f'which modelfile was copied where\n\n')
  
maxR2DstPath = os.path.join(os.getcwd(), 'maxR2')
minMAPEDstPath = os.path.join(os.getcwd(), 'minMAPE')

maxR2Models = glob.glob(os.path.join(maxR2Models, '*'))
#print(f'{maxR2Models}')
i = 0
for maxR2Model in maxR2Models:
  srcModelPath = maxR2Model
  #print(f'{srcModelPath}')
  dstModelPath = os.path.join(maxR2DstPath, f'maxR2-{i}', "density", "trainedModel.pth")
  #print(f'{dstModelPath}\n')
  shutil.copy(srcModelPath, dstModelPath)
  with open(logFile, 'a') as f:
    f.write(f'{os.path.basename(srcModelPath)} copied to maxR2-{i}\n')
  i = i + 1
  
with open(logFile, 'a') as f:
    f.write(f'\n')

minMAPEModels = glob.glob(os.path.join(minMAPEModels, '*'))
#print(f'{minMAPEModels}')
i = 0
for minMAPEModel in minMAPEModels:
  srcModelPath = minMAPEModel
  #print(f'{srcModelPath}')
  dstModelPath = os.path.join(minMAPEDstPath, f'minMAPE-{i}', "density", "trainedModel.pth")
  #print(f'{dstModelPath}\n')
  shutil.copy(srcModelPath, dstModelPath)
  with open(logFile, 'a') as f:
    f.write(f'{os.path.basename(srcModelPath)} copied to minMAPE-{i}\n')
  i = i + 1
