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
def load_data():
	with open ('out/my_data.csv','r') as file_filter:
		for line in file_filter:
		
#Normalization of the data

min_max_scaler = preprocessing.MinMaxScaler()
features = min_max_scaler.fit_transform(features)
print (states)
