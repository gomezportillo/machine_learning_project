#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Andrés Montoro Montarroso
@author: Pedro Manuel Gómez-Portillo
"""

from sklearn.cluster import DBSCAN

# Calculating labels my means of the DBSCAN algorithm
X = []
with open ('data/inc2006.csv','r') as file_filter:
    for line in file_filter:
        cadena = line.split(";")
        data=[cadena[2],cadena[12]]
        X.append(data)
labels = DBSCAN(eps=0.0075, min_samples=5).fit_predict(X)

# Appending the id of the zone to each incident
nl = ""
with open('data/inc2006.csv') as fin:
    with open('data/inc2006zone.csv', 'w') as fout:
        lines = fin.readlines()
        for i in xrange(len(lines)):
            if labels[i] != -1: #In that way we get ride of the noise
                nl = str(lines[i].replace("\n", "")) + ";" + str(labels[i]) + "\n"
                fout.write(nl)
