#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example of using interpolation lagrange with library
"""
import numpy
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
x=[1,2,4]
y=[2,3,-1]
plt.plot(x,y,"o")
plt.ylabel("Y")
plt.xlabel("X")
plt.show()
p=lagrange(x,y)
print(p)
print("Evaluate in x = 1")
print(p(5))
x1 = numpy.arange(1,4.2,0.1)
plt.plot(x1,p(x1))
plt.plot(x,y,"o")
plt.show()