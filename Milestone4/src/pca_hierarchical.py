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
with open ('out/inc2006features.csv', 'r') as file_filter:
	for line in file_filter:
		row=line.split(";")
		row.pop(0)
		if row != []:
			data.append(list(map(float, row)))

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
plt.xlim(-1.1, 0.5)
plt.ylim(-0.7, 0.4)
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
labels = set(clusters)
print ('Clusters number %d' % (len(labels) + 1))

#Characterize the obtained groups
zones = ['Low risk','Medium risk','High risk']

lines = open("out/inc2006features.csv").readlines()

acc_per_zone = []

for i in range(len(lines)):
	zone = clusters[i]
	number_accidents = sum(map(int, lines[i].split(";")))
	acc_per_zone.append((zone, number_accidents))

cluster_1 = []
cluster_2 = []
cluster_3 = []

for result in acc_per_zone:
	zone = result[0]
	n_accidents = result[1]

	if zone == 1:
		cluster_1.append(n_accidents)
	if zone == 2:
		cluster_2.append(n_accidents)
	if zone == 3:
		cluster_3.append(n_accidents)

mean_cluster_1 = sum(cluster_1)/len(cluster_1)
mean_cluster_2 = sum(cluster_2)/len(cluster_2)
mean_cluster_3 = sum(cluster_3)/len(cluster_3)

fout_name = "out/inc2006acc_zone.csv"
headers = "Cluster;Number of accidents;Mean\n"

with open(fout_name, 'w') as f_out:
	f_out.write(headers)

	for index, number in enumerate(cluster_1):
		if index == 0:
			f_out.write('1;{};{}\n'.format(number, mean_cluster_1))
		else:
			f_out.write('1;{}\n'.format(number))

	for index, number in enumerate(cluster_2):
		if index == 0:
			f_out.write('2;{};{}\n'.format(number, mean_cluster_2))
		else:
			f_out.write('2;{}\n'.format(number))

	for index, number in enumerate(cluster_3):
		if index == 0:
			f_out.write('3;{};{}\n'.format(number, mean_cluster_3))
		else:
			f_out.write('3;{}\n'.format(number))
