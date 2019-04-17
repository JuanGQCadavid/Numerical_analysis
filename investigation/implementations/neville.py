#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 21:10:47 2019

@author: evinracher
"""

X = [1,1.2,1.4,1.6,1.8,2]
Px = [0.674732,0.849196,1.121407,1.492135,1.960735,2.525897]

def neville(X,Px,x):
    n = len(X)
    matriz = [None] * n
    for i in range(n):
        matriz[i] = [None] * n
    for i in range(n):
        matriz[0][i] = Px[i]

    for grado in range(1,n):
        j = grado
        for i in range(0, n-grado):
            Pi = matriz[grado-1][j-1]
            Pj = matriz[grado-1][j]
            matriz[grado][j] = ((x-X[i])*Pj-(x-X[j])*Pi)/(X[j]-X[i])
            j += 1
    return matriz[n-1][n-1]

print(neville(X,Px,1.45))