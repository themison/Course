import numpy
import copy

def ex5(ip, routers):
  first = ip[0][0]
  classes = str
  mask = []
  if first<128:
    classes = 'A'
    mask = [255,0,0,0]
  elif first<192:
    classes = 'B'
    mask = [255,255,0,0] 
  elif first<224:
    classes = 'C'
    mask = [255,255,255,0]
  elif first<240:
    classes = 'D'
    mask = [255,255,255,255] 
  
  count = len(routers)
  for i in range(len(routers)):
    count +=routers[i][1]

  network = numpy.bitwise_and(ip,mask)
  node =  numpy.bitwise_and(ip,numpy.invert(numpy.uint8(mask)))
  broadcast = numpy.bitwise_or(ip,numpy.invert(numpy.uint8(mask)))
  hostMin = copy.deepcopy(network)
  hostMin[0][3]+=1
  hostMax = copy.deepcopy(broadcast)
  hostMax[0][3]-=1
  print('Ip = ',str(ip))
  print('mask = ',str(mask))
  print('Class = ',str(classes))
  print('Network = ',str(network))
  print('Node = ',str(node))
  print('Broadcast = ',str(broadcast))
  print('Host min - ',str(hostMin), 'Host max - ', str(hostMax))

  
  

  