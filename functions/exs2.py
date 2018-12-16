import math

def powerOf(Graph):
  powerOfNode = []
  powerOfNetwork = math.inf
  for i in range(len(Graph)):
    power = 0
    for j in range(len(Graph[i])):
      if (Graph[i,j]!=0):
        power+=1
    if power<powerOfNetwork:
      powerOfNetwork = power
    print('Степень узла '+str(i)+' = ' + str(power))
  print('Степень сети = ' +str(powerOfNetwork))