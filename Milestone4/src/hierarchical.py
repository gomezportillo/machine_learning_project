#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Andrés Montoro Montarroso
@author: Pedro Manuel Gómez-Portillo
"""

import matplotlib.pyplot as plt
import numpy
from scipy import cluster
from sklearn import preprocessing
import sklearn.neighbors

#MAKING HIERARCHICAL ALGORITHM WITH THE DBSCAN RESULTS

#Load data
data=[]
count = 0
with open ('out/inc2006features.csv','r') as file_filter:
	for line in file_filter:
		if count > 0:
			row=line.split(";")
			row.pop(0)
			if row != []:
				data.append(list(map(float, row)))
		count += 1


#Normalization of the data
min_max_scaler = preprocessing.MinMaxScaler()
data = min_max_scaler.fit_transform(numpy.asarray(data))
print (data)

#Compute the similarity matrix
dist = sklearn.neighbors.DistanceMetric.get_metric('euclidean')
matsim = dist.pairwise(data)
avSim = numpy.average(matsim)
print ("%s\t%6.2f" % ('Distancia Media', avSim))

# Building the Dendrogram
clusters = cluster.hierarchy.linkage(matsim, method = 'complete')
cluster.hierarchy.dendrogram(clusters, color_threshold=1)
plt.show()

#Cutting the dendrogram
cut = 1
clusters = cluster.hierarchy.fcluster(clusters, cut, criterion='distance')
labels = set(clusters)
print ('Clusters number %d' % (len(labels) + 1))

#Clasification zones
