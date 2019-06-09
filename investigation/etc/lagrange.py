#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 21:37:05 2019

@author: evinracher
"""

def L(X, xk, x):
    result = 1.0
    for xi in X:
        if xi != xk:
            result *= (x - xi)/(xk - xi)
    return result

def interpolate(X,Y, x):
    y_evaluation = 0.0
    n = len(X)
    for xk in range(n):
        y_evaluation += Y[xk]*L(X, X[xk], x)
    return y_evaluation

x = [1,2,4]
y = [2,3,-1]
result = interpolate(x,y, 5)
print(result)
