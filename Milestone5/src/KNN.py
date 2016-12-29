import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors

#We will start training the knn algorithm and serching the best k
#f_zones_out_60 is our training group
#f_zones_out_40 is our test group

def training():
	train = 150
	validation_error= [0] * 151
	with open('out/zones_random_60.csv','r') as f_zones_out_60:
		with open('out/zones_random_40.csv','r') as f_zones_out_40:
			for n_neighbors in range (1,151):
				clf = neighbors.KNeighborsClassifier(n_neighbors, weights='distance')
				clf.fit(f_zones_out_60[['latitude','longitude']],f_zones_out_60['zone'])
				Z = clf.predict(f_zones_out_40[['latitude','longitude']])
				error = (f_zones_out_40['zone'] != Z).sum() / len(f_zones_out_40) 
				validation_error[n_neighbors]+=error

	validation_error=map(lambda x : x / train, validation_error) 
	
	plt.title('Selection of best K (distance)')
	plt.ylabel('Error')
	plt.xlabel('K')
	plt.xlim(1, 150)
	plt.plot(validation_error)
	plt.show()

training()