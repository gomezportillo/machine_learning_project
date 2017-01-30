import csv
import matplotlib.pyplot as plt
import numpy as np
from sklearn import tree
from sklearn.externals.six import StringIO
import pydotplus


#Load data
features_file = open('out/datos2007_features.csv').readlines()
zones_file = open('out/datos2007acc_zone.csv').readlines()

data = [line.split(';') for line in features_file]
target = [line.split(';')[0] for line in zones_file if 'Cluster' not in line]

#Characterize the obtained groups
features_names = ['pk_ini', 'tipo', 'lat', 'causa', 'pk_fin', 'matricula', 'nivel', 'sentido',
                  'provincia', 'carretera', 'fecha_hora_ini', 'autonomia', 'long', 'poblacion']

zones = ['Low risk','Medium risk','High risk']

#Fit Decision Tree
clf = tree.DecisionTreeClassifier(random_state = 0)
clf = clf.fit(data, target)

#Write pfd with decision tree
dot_data = StringIO()
tree.export_graphviz(clf,
                     out_file = dot_data,
                     feature_names = features_names,
                     class_names = zones,
                     filled = True,
                     rounded = True,
                     special_characters = True)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf(path = 'out/decision_tree.pdf')
