import csv
import matplotlib.pyplot as plt 
import numpy as np 
from sklearn import tree
from sklearn.externals.six import StringIO
import pydotplus


#Load data
file_name_in = open('data/inc2006features.csv')
zonas_csv = csv.reader(file_name_in)
features = next(zonas_csv)

data = []
target = []
for z in zonas_csv:
    data.append(z)
    target.append(z)
    

#Characterize the obtained groups
zones = ['Low risk','Medium risk','High risk']


#Fit Decision Tree
clf = tree.DecisionTreeClassifier(random_state = 0)
clf = clf.fit(data, target)

#Write pfd with decision tree
dot_data = StringIO()
tree.export_graphviz(clf, 
                     out_file = dot_data,
                     feature_names = features,
                     class_names = zones,
                     filled = True,
                     rounded = True,
                     special_characters = True)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf(path = 'decision_tree.pdf')


