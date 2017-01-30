#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Andrés Montoro Montarroso
@author: Pedro Manuel Gómez-Portillo
"""

import matplotlib.pyplot as plt
import sklearn.neighbors
import numpy
import sklearn.cluster
from sklearn import metrics

#Filtering inc2006.csv by accidents
def filter():
    with open('data/inc2006.csv', 'r') as f_in:
        with open('data/inc2006filt.csv', 'w') as f_out:
            lines = f_in.readlines()
            for i in range(len(lines)):
                if "Accidente" in lines[i]:
                    f_out.write(lines[i])
filter()

#Plottering data by clusters
def plotdata(data, labels, name):
    fig, ax = plt.subplots()
    plt.scatter([row[0] for row in data], [row[1] for row in data], c=labels)
    ax.grid(True)
    fig.tight_layout()
    plt.title(name)
    plt.show()

#Creating file only with latitude and longitude
X = []
with open ('data/inc2006filt.csv','r') as file_filter:
    for line in file_filter:
        cadena = line.split(";")
        data=[cadena[2],cadena[12]]
        X.append(data)

#Creating two vector, one with lat. and with long.
miX = []
miY=[]
for e in X:
    miX.append(e[0])
    miY.append(e[1])

plt.scatter(miX, miY)
plt.show()

#Creating the graph with the distribution in order to see de inflexion point
dist = sklearn.neighbors.DistanceMetric.get_metric('euclidean')
matsim = dist.pairwise(X)

minPts=5
"""
A = sklearn.neighbors.kneighbors_graph(X, minPts, include_self=False)
Ar = A.toarray()

seq = []
for i,s in enumerate(X):
    for j in range(len(X)):
        if Ar[i][j] != 0:
            seq.append(matsim[i][j])

seq.sort()
plt.plot(seq)
plt.show()
"""
#plotting the clusters
labels = sklearn.cluster.DBSCAN(eps=0.0075, min_samples=minPts).fit_predict(X)
	
# 3. Plot the results
plotdata(X,labels, 'dbscan')

print("Number of clusters: {}".format(len(set(labels)) - (1 if -1 in labels else 0)))

# 4. Validation
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(numpy.asarray(X), labels))
