import math
print("importing the math module")

root = math.sqrt(9)
print(root)

from math import sqrt

root = sqrt(9)
print(root)

#alias

import math as m
cosine = m.cos(0)
print(cosine)

from math import factorial as f
factorial_5=f(5)# 5*4*3*2*1
print(factorial_5)

from math import *
