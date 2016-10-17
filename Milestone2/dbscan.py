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


#Filtra inc2006.csv por accidentes
def filtro():
    with open('inc2006.csv', 'r') as csvopen:
        with open('inc2006filt.csv', 'w') as csvout:
            lineas=csvopen.readlines()
            for i in range(len(lineas)):
                if "Accidente" in lineas[i]:
                    csvout.write(lineas[i])
filtro()



X = []
inc = [[0,], [0,]]
fields = ["latitud","longitud"]

with open ('inc2006filt.csv','r') as f:
    
    


        
    




            
    