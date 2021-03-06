import copy
import scipy.io
import math

def rip(Graph, delay = 0, time = 0):
  #find better way
  def way(j, c):
    if(ripMatrix[j][c][2]!=c and ripMatrix[j][c][2]!=None):
      return ripMatrix[j][ripMatrix[j][c][2]][1]+way(ripMatrix[j][c][2],c)
    else:
      return ripMatrix[j][c][1]
       
  ripMatrix = {}
  for i in range(len(Graph)):
    link = []
    for j in range(len(Graph[i])):
      linkIns = []
      linkIns.append(j)
      linkIns.append(Graph[i][j])
      if (i!=j and Graph[i][j]==0):
        linkIns.append(None)
      else:
        linkIns.append(j)
      link.append(linkIns)
    ripMatrix[i]=link

  checkRipMatrix = []
  for i in range(len(ripMatrix)):
    link = []
    for j in range(len(ripMatrix[i])):
      if ripMatrix[i][j][2]!=None:
        link.append(ripMatrix[i][j][2])
    checkRipMatrix.append(link)
    link = []

  newRipMatrix = copy.deepcopy(ripMatrix)

  adict1 = {}
  for z in range(3):
    for i in range(len(ripMatrix)):
      for j in range(len(ripMatrix)):
        if (j in checkRipMatrix[i] and i!=j and ripMatrix[i][j][2]!=None):
          for c in range(len(ripMatrix[j])):
            if ripMatrix[j][c][2]!=None:  
              val = newRipMatrix[i][j][1] + way(j,c)
              if(newRipMatrix[i][c][1]>=val or newRipMatrix[i][c][2]==None):
                newRipMatrix[i][c][1] = val
                newRipMatrix[i][c][2] = j
      new = copy.deepcopy(newRipMatrix[i])
      for b in range(len(newRipMatrix)):
        if new[b][1]!=0:
          new[b][1]+=z+1;
        if newRipMatrix[i][b][2]==None:
          new[b][2] = 0 
      adict1['in'+str(z)+str(i)] = copy.deepcopy(new)

    ripMatrix = copy.deepcopy(newRipMatrix)
  scipy.io.savemat('./testmat1.mat', adict1)  

  adict = {}
  for i in range(10):
    print("Timeout for " +str(i))
    for j in range(10):
      adict['Node'+str(i)]=newRipMatrix[i]
      print(newRipMatrix[i][j])
  scipy.io.savemat('./testmat.mat', adict)
  return newRipMatrix;
      