import scipy.io
import numpy
from functions.exs1 import dijkststa 
from functions.exs2 import powerOf
from functions.exs3 import networkDegree
from functions.exs4 import rip
from functions.exs5 import ex5
from functions.exs6a import ex6a
from functions.exs6b import ex6b

mat = scipy.io.loadmat('V_02.mat')

#create variables Zd1, Zd3, Zd5, Zd5ip, Zd6, Zd6NN, a
locals().update(mat)
# 1
dijkststa(a, Zd1[0])
print('\n')
#2
powerOf(a)
print('\n')
#3  
networkDegree(a,Zd1[0])
print('\n')
# 4
rip(a, 30, 90)
print('\n')
#5
ex5(Zd5ip, Zd5)
print('\n')
#6
ex6a(Zd5ip, Zd5, Zd6, Zd6NN)
print('\n')
ex6b(Zd5ip, Zd5, Zd6, Zd6NN)
