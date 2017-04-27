# -*- coding: utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs


n_samples = 150000
random_state = 59
X,y = make_blobs(n_samples = n_samples, centers =5,random_state = random_state)
plt.scatter(X[:,0],X[:,1],c=y)
plt.title('initial data')

from sklearn.cluster import KMeans
k = 3

clusters = KMeans(n_clusters = k).fit_predict(X)
plt.scatter(X[:,0],X[:,1],c = clusters)
plt.show()

#from sklearn.cluster import AgglomerativeClustering
#
#k = 3
#ag_cluster = AgglomerativeClustering(n_clusters = k).fit_predict(X)
#plt.scatter(X[:,0],X[:,1],c = ag_cluster)

def centroid(X):
    return np.mean(X, axis=0)
    
    
def voronoi(X, centroids):
    
    for x in X:
        idx = 0
        last_dist = 5000
        for centr in centroids:
            
            dist = np.linalg.norm(x-centr)
            if dist < last_dist:
                last_dist = dist
                
            idx += idx
            