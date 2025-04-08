import glob
import os
import shutil

thisCWD = os.getcwd()

maxR2Dir = os.path.join(thisCWD, 'maxR2')
minMAPEDir = os.path.join(thisCWD, 'minMAPE')

maxR2Dirs = glob.glob(os.path.join(maxR2Dir, 'maxR2-*'))
#print(f'{maxR2Dirs}')
minMAPEDirs = glob.glob(os.path.join(minMAPEDir, 'minMAPE-*'))
#print(f'{minMAPEDirs}')

for maxR2Dir in maxR2Dirs:
  #print(f'{maxR2Dir}')
  thisPhysPropDirs = glob.glob(os.path.join(maxR2Dir, 'PhysProp', 'a.*'))
  
  iterations = []
  steps = []
  for thisPhysPropDir in thisPhysPropDirs:
    #print(f'{thisPhysPropDir}')
    ite = int(thisPhysPropDir.split('.')[1])
    ste = int(thisPhysPropDir.split('.')[2])
    try:
      iterations[ite-1] = ite
      steps[ite-1] = steps[ite-1] + 1
    except:
      iterations.append(ite)
      steps.append(1)
  #print(f'{iterations}')
  #print(f'{steps}')
  #break
      
  for thisPhysPropDir in thisPhysPropDirs:
    ite = int(thisPhysPropDir.split('.')[1])
    ste = int(thisPhysPropDir.split('.')[2])
    if ste < steps[ite-1]-1: ## for safety '- 1'
      #print(f'rm {thisPhysPropDir}')
      QMMMDir = os.path.join(maxR2Dir, "QMMM", f'a.{ite}.{ste}')
      #print(f'rm {QMMMDir}')
      try:
        shutil.rmtree(thisPhysPropDir)
      except:
        print(f'  couldn t delete {thisPhysPropDir}.')
      else:
        print(f'Deleted {thisPhysPropDir}')
        
      try:
        shutil.rmtree(QMMMDir)
      except:
        print(f'couldn t delete {QMMMDir}.')
      else:
        print(f'Deleted {QMMMDir}')
    else:
      #print(f'  keep: {thisPhysPropDir}')
      #QMMMDir = os.path.join(maxR2Dir, "QMMM", f'a.{ite}.{ste}')
      #print(f'  keep: {QMMMDir}')
      pass
      
for minMAPEDir in minMAPEDirs:
  #print(f'{minMAPEDir}')
  thisPhysPropDirs = glob.glob(os.path.join(minMAPEDir, 'PhysProp', 'a.*'))
  
  iterations = []
  steps = []
  for thisPhysPropDir in thisPhysPropDirs:
    #print(f'{thisPhysPropDir}')
    ite = int(thisPhysPropDir.split('.')[1])
    ste = int(thisPhysPropDir.split('.')[2])
    try:
      iterations[ite-1] = ite
      steps[ite-1] = steps[ite-1] + 1
    except:
      iterations.append(ite)
      steps.append(1)
  #print(f'{iterations}')
  #print(f'{steps}')
  #break
      
  for thisPhysPropDir in thisPhysPropDirs:
    ite = int(thisPhysPropDir.split('.')[1])
    ste = int(thisPhysPropDir.split('.')[2])
    if ste < steps[ite-1]-1: ## for safety '- 1'
      #print(f'rm {thisPhysPropDir}')
      QMMMDir = os.path.join(minMAPEDir, "QMMM", f'a.{ite}.{ste}')
      #print(f'rm {QMMMDir}')
      try:
        shutil.rmtree(thisPhysPropDir)
      except:
        print(f'  couldn t delete {thisPhysPropDir}.')
      else:
        print(f'Deleted {thisPhysPropDir}')
        
      try:
        shutil.rmtree(QMMMDir)
      except:
        print(f'couldn t delete {QMMMDir}.')
      else:
        print(f'Deleted {QMMMDir}')
    else:
      #print(f'  keep: {thisPhysPropDir}')
      #QMMMDir = os.path.join(minMAPEDir, "QMMM", f'a.{ite}.{ste}')
      #print(f'  keep: {QMMMDir}')
      pass
  
