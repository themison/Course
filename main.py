import scipy.io

import copy
from functions.exs1 import dijkststa 
from functions.exs2 import powerOf

# from functions.exs4 import rip
from functions.exs3 import networkDegree
mat = scipy.io.loadmat('V_02.mat')

#create variables Zd1, Zd3, Zd5, Zd5ip, Zd6, Zd6NN, a
locals().update(mat)
dijkststa(a, Zd1[0])
powerOf(a)
networkDegree(a,Zd1[0])

# def rip(Graph, delay = 0, time = 0):
  # ripMatrix = {}
  # for i in range(len(Graph)):
  #   link = []
  #   for j in range(len(Graph[i])):
  #     linkIns = []
  #     linkIns.append(j)
  #     linkIns.append(Graph[i][j])
  #     if (i!=j and Graph[i][j]==0):
  #       linkIns.append(None)
  #     else:
  #       linkIns.append(j)
  #     link.append(linkIns)
  #   ripMatrix[i]=link

  
  # newRipMatrix = copy.deepcopy(ripMatrix)
  # print(ripMatrix[0][0][0])
  # for z in range(1):
  #   for i in range(len(ripMatrix)):
  #     for j in range(len(ripMaчtrix)):
  #       if (i!=j and ripMatrix[i][j][2]!=None):
  #         for c in range(len(ripMatrix[j])):
  #           if ripMatrix[j][c][2]!=None:
  #             print(i,j,c)
  #             val = newRipMatrix[i][j][1]
  #             if(newRipMatrix[i][c][1]>val+ripMatrix[j][c][1] or newRipMatrix[i][c][2]==None):
  #               newRipMatrix[i][c][0] = c
  #               newRipMatrix[i][c][1] = (val+ripMatrix[j][c][1])
  #               newRipMatrix[i][c][2] = j;
  # print(ripMatrix)

# def findWay():
#   continue



# rip(a)

# def exs5(ip, source=0):
  # newIp = []
  # mask = [11111111,00000000,00000000,00000000]
  # numberOfNetwork = []
  # numberOf
  # for i in range(4):
  #   new = bin(ip[i])
  #   newIp.insert(i,new[2:])
    
  # print(smth)  
