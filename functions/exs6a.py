import numpy
import copy
import math

def ex6a(ip, Graph, count, routers):
  first = ip[0][0]
  classes = str
  mask = []
  if first<128:
    classes = 'A'
  elif first<192:
    classes = 'B'
  elif first<224:
    classes = 'C'
  elif first<240:
    classes = 'D'

  subnet = 0
  for i in range(count[0][0]+1):
    if i!=0:
      subnet += Graph[count[0][i]-1][1]
  subnet += routers[0][0]
  
  subnet = math.ceil(math.log(subnet,2))
  abc = []
  for i in range(32-subnet):
    abc.append(1)
  for i in range(subnet):
    abc.append(0)
  abc = numpy.packbits(abc)
  mask = [255,255,255,255]
  mask = numpy.bitwise_and(mask,abc)
  network = numpy.bitwise_and(ip,mask)
  node =  numpy.bitwise_and(ip,numpy.invert(numpy.uint8(mask)))
  broadcast = numpy.bitwise_or(ip,numpy.invert(numpy.uint8(mask)))
  hostMin = copy.deepcopy(network)
  hostMin[0][3]+=1
  hostMax = copy.deepcopy(broadcast)
  hostMax[0][3]-=1
  print('Ip = ',str(ip))
  print('Mask = ',str(mask))
  print('Class = ',str(classes))
  print('Network = ',str(network))
  print('Node = ',str(node))
  print('Broadcast = ',str(broadcast))
  print('Host min - ',str(hostMin), 'Host max - ', str(hostMax))

  
  

  