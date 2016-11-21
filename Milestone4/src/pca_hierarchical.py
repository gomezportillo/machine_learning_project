#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Andrés Montoro Montarroso
@author: Pedro Manuel Gómez-Portillo
"""

import codecs
import matplotlib.pyplot as plt
import numpy
from sklearn.decomposition import PCA
from sklearn import preprocessing
import sklearn.cluster
from scipy import cluster

#Load data
data=[]
count = 0
with open ('out/inc2006features.csv', 'r') as file_filter:
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

#PCA Estimation
estimator = PCA (n_components = 2)
X_pca = estimator.fit_transform(data)

#Plot PCA
plt.scatter([x[0] for x in X_pca], [x[1] for x in X_pca])
plt.show()


#Plot the zone where the number of clusters is higher
fig, ax = plt.subplots()
plt.xlim(-0.5, 1)
plt.ylim(-0.5, 0.75)
ax.grid(True)

for i in range(len(X_pca)):
	plt.scatter(X_pca[i][0], X_pca[i][1])
plt.show()



#Compute the similarity matrix
dist = sklearn.neighbors.DistanceMetric.get_metric('euclidean')
matsim = dist.pairwise(X_pca)
avSim = numpy.average(matsim)
print ("%s\t%6.2f" % ('Distancia Media', avSim))

# Building the Dendrogram
clusters = cluster.hierarchy.linkage(matsim, method = 'ward')
cluster.hierarchy.dendrogram(clusters, color_threshold=19.5)
plt.show()

#Cutting the dendrogram
cut = 19.5
clusters = cluster.hierarchy.fcluster(clusters, cut, criterion='distance')
labels = list(set(clusters))
print ('Clusters number %d' % (len(labels) + 1))

#Characterize the obtained groups

#zones = ['Low risk','Medium risk','High risk']
#features = ['Alcance','Atropello','Vuelco','Tijera_camion','Salida','Rojo','Amarillo',
			#'Negro','Blanco','Invierno','Verano','8am_15pm','15pm_20pm','20pm_3am']


	








