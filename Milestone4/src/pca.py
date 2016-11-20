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

#Load data
data=[]
count = 0 
with open ('out/my_data.csv','r') as file_filter:
	for line in file_filter:
		if count > 0: 
			row=line.split(";")
			row.pop(0)
			if row != []:
				data.append(map(float, row))
		count += 1

		
#Normalization of the data
min_max_scaler = preprocessing.MinMaxScaler()
data = min_max_scaler.fit_transform(data)
print (data)

