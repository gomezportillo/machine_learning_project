#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Andrés Montoro Montarroso
@author: Pedro Manuel Gómez-Portillo
"""
from sklearn.cluster import KMeans
from sklearn import metrics
import numpy
import matplotlib.pyplot as plt

def calculate_X():
    X = []
    with open ('data/inc2006filt.csv','r') as file_filter:
        for line in file_filter:
            cadena = line.split(";")
            data=[cadena[2],cadena[12]]
            X.append(data)
    return X

def calculate_best_k(X):
    miX = []
    miY=[]
    for e in X:
        miX.append(e[0])
        miY.append(e[1])

    plt.scatter(miX, miY)
    plt.grid()
    plt.show()

    init = 'random' # initialization method
    iterations = 10 # to run 10 times with different random centroids to choose the final model as the one with the lowest SSE
    max_iter = 300 # maximum number of iterations for each single run
    tol = 1e-04 # controls the tolerance with regard to the changes in the within-cluster sum-squared-error to declare convergence
    random_state = 0 # random


    distortions = []
    silhouettes = []

    for i in range(70, 110, 10):
        km = KMeans(i, init, n_init = iterations ,max_iter= max_iter, tol = tol,random_state = random_state)
        labels = km.fit_predict(X)
        distortions.append(km.inertia_)
        silhouettes.append(metrics.silhouette_score(numpy.asarray(X), labels)) #aquí se nota la potencia computacional

    # Plot distoritions
    plt.plot(range(70, 110, 10), distortions, marker='o')
    plt.xlabel('Number of clusters')
    plt.ylabel('Distortion')
    plt.show()

    # Plot Silhouette
    plt.plot(range(70, 110, 10), silhouettes , marker='o')
    plt.xlabel('Number of clusters')
    plt.ylabel('Silohouette')
    plt.show()


X = calculate_X()
#calculate_best_k(X)

#By the graphs we have conclude that the best number of clusters is k = 90
number_clusters = 5
#Now we will be using the spectral algorithm to cluster the data

from sklearn import cluster, datasets
from sklearn.preprocessing import StandardScaler

X = StandardScaler().fit_transform(X)

# estimate bandwidth for mean shift
spectral = cluster.SpectralClustering(n_clusters=number_clusters, eigen_solver='arpack', affinity="nearest_neighbors")
# predict cluster memberships
spectral.fit(X)
if hasattr(spectral, 'labels_'):
    labels = spectral.labels_.astype(numpy.int)
else:
    labels = spectral.predict(X)

# plot
colors = numpy.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
colors = numpy.hstack([colors] * 20)

plt.scatter(X[:, 0], X[:, 1], color=colors[labels].tolist(), s=10)

plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.xticks(())
plt.yticks(())

plt.show()
