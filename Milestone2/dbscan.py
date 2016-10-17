#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 16:58:09 2016

@author: MontoroMontarroso
"""

import csv
import matplotlib.pyplot as plt
import sklearn.neighbors
import numpy as np
from sklearn.cluster import DBSCAN


#Filtra inc2006.csv por accidentes
def filtro():
    with open('inc2006.csv', 'r') as csvopen:
        with open('inc2006filt.csv', 'w') as csvout:
            lineas=csvopen.readlines()
            for i in range(len(lineas)):
                if "Accidente" in lineas[i]:
                    csvout.write(lineas[i])
filtro()


#Filtramos por latitud y longitud
X = []
with open ('inc2006filt.csv','r') as f:
    for linea in f:
        cadena = linea.split(";")
        data=[cadena[2],cadena[12]]
        X.append(data)

miX = []
miY=[]
for e in X:
    miX.append(e[0])
    miY.append(e[1])

plt.scatter(miX, miY)
plt.show()

dist = sklearn.neighbors.DistanceMetric.get_metric('euclidean')
matsim = dist.pairwise(data)
