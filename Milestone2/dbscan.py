#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 16:58:09 2016

@author: MontoroMontarroso
@author: Pedro Manuel Gómez-Portillo
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

def plotdata(data,labels,name): #def function plotdata
#colors = ['black']
    fig, ax = plt.subplots()
    plt.scatter([row[0] for row in data], [row[1] for row in data], c=labels)
    ax.grid(True)
    fig.tight_layout()
    plt.title(name)
    plt.show()

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
matsim = dist.pairwise(X)    

minPts=3
from sklearn.neighbors import kneighbors_graph
A = kneighbors_graph(X, minPts, include_self=False)
Ar = A.toarray()

seq = []
for i,s in enumerate(X):
    for j in range(len(X)):
        if Ar[i][j] != 0:
            seq.append(matsim[i][j])
            
seq.sort()
plt.plot(seq)
plt.show()

import sklearn.cluster
labels = sklearn.cluster.DBSCAN(eps=0.0075, min_samples=minPts).fit_predict(X)

# 3. Plot the results
plotdata(X,labels, 'dbscan')

# 4. Validation
from sklearn import metrics
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(np.asarray(X), labels))

 

 




            
    