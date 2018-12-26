import math
from functions.wayDij import way

def dijkststa(Graph, source, printer = 1):
  # nodes from Zd1
  start = source[0]-1

  #
  dist = [] 
  visited = [] 
  previous = [] 
  for i in range(len(Graph)):
    dist.insert(i, math.inf)
    visited.insert(i, 0)
    previous.insert(i, False)
  

  dist[start] = 0;
  while sum(visited) < 9:
    tmin = math.inf
    for i in range(len(dist)):
      if (visited[i] == 0 and dist[i] < tmin):
        tmin = dist[i]
        u = i
    visited[u] = 1;
    neighbor = createNeib(Graph, u)

    for i in range(len(neighbor)):
      neib = neighbor[i]
      alt = dist[u] + Graph[u, neib]
      if alt < dist[neib] and visited[neib]!=1:
        dist[neib] = alt
        previous[neib] = u
  if printer == 1:
    for i in range(len(source)-1):
      print('Answer for '+str(source[i+1]-1)+' = '+str(dist[source[i+1]-1]))
      print('Path ', end='')
      way(previous,source[i+1]-1)

  else:
    return [dist, previous]
    
def createNeib(Graph, source):
  neighbor = []
  arr = Graph[source]
  for i in range(len(arr)):
    if (arr[i]!=0):
      neighbor.append(i)
  
  return neighbor
