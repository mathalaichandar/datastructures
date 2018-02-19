from circularbuffer import CircularBuffer
from movingavg import MovingAvg
from linkedlist import *
from heap import *
from hauffman import *
import math
m = MovingAvg(4)
m.add(6)
m.getStd()
print(m)
m.add(2)
m.getStd()
print(m)
m.add(3)
m.getStd()
print(m)
m.add(1)
m.getStd()
print(m)
'''
m.add(59)
m.getStd()
print(m)
m.remove()
m.getStd()
print(m)
m.add(1)
m.getStd()
print(m)
'''

h = Heap([5,7,2,8,1,9,5])
print(h)

l = LinkedList()
l.prepend(4)
l.prepend(5)
l.prepend(6)
l.remove(5)
print(l)

hf = Huffman('aabbad')
print(hf)