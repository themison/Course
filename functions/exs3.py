from .exs1 import dijkststa
from .wayDij import way
def networkDegree(Graph, source):
  arr = Graph
  for i in range(len(Graph)):
    for j in range(len(Graph[i])):
      if (Graph[i,j]!=0):
        arr[i,j]=1

  maxium = 0
  for i in range(len(arr)):
    dij = dijkststa(arr, [i], 0)
    ans = max(dij[0])
    if ans>maxium:
      forAlg = dij[1]
      j = dij[0].index(ans)
      maxium = ans
  print('Network degree = '+ str(maxium))
  way(forAlg, j)

  