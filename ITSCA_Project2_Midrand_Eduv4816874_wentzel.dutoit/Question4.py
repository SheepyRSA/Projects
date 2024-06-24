# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 07:51:10 2024

@author: Wentz
"""
from sklearn.datasets import load_wine
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = load_wine(return_X_y=True, as_frame=True)
"test = data[:1]"
wineTable = pd.DataFrame(data[(0)])
wineTable = wineTable.drop(['malic_acid', 'proline', 'ash', 'alcalinity_of_ash', 'magnesium'], axis=1)
wineTable = wineTable.drop(['od280/od315_of_diluted_wines', 'total_phenols', 'hue', 'flavanoids'], axis=1)
wineTable = wineTable.drop(['nonflavanoid_phenols', 'proanthocyanins',], axis=1)
print(wineTable)

x1 = wineTable['alcohol']
x2 = wineTable['color_intensity']
X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)

plt.plot()
plt.xlim([10, 15])
plt.ylim([0, 15])
plt.title('Alcohol and color intensity distribution')
plt.scatter(x1, x2)
plt.show()

distortions = []
inertias = []
mapping1 = {}
mapping2 = {}

K = range(1, 11)
 
for k in K:
    
    kmeanModel = KMeans(n_clusters=k, n_init=10).fit(X)
    kmeanModel.fit(X)
 
    distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_,
                                        'euclidean'), axis=1)) / X.shape[0])
    inertias.append(kmeanModel.inertia_)
 
    mapping1[k] = sum(np.min(cdist(X, kmeanModel.cluster_centers_,
                                   'euclidean'), axis=1)) / X.shape[0]
    mapping2[k] = kmeanModel.inertia_

for key, val in mapping1.items():
    print(f'{key} : {val}')

plt.plot(K, distortions, 'bx-')
plt.xlabel('Values of K')
plt.ylabel('Distortions')
plt.title('The Elbow Method using Distortion')
plt.show()

k_range = range(1, 11)
 
inertia_values = []
 
for k in k_range:
    kmeans = KMeans(n_clusters=k, n_init=10, \
                    init='k-means++', random_state=42)
    y_kmeans = kmeans.fit_predict(X)
    inertia_values.append(kmeans.inertia_)
    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans)
    plt.scatter(kmeans.cluster_centers_[:, 0],\
                kmeans.cluster_centers_[:, 1], \
                s=100, c='red')
    plt.title('K-means clustering (k={})'.format(k))
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
 
plt.plot(k_range, inertia_values, 'bo-')
plt.title('Elbow Method')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.show()

"Elbow method accessed online 18/06/2024: https://www.geeksforgeeks.org/elbow-method-for-optimal-value-of-k-in-kmeans/"
"Kmeans method tutorial accessed online 18/06/2024: https://realpython.com/k-means-clustering-python/#:~:text=Understanding%20the%20K-Means%20Algorithm,-Conventional%20k-means&text=The%20quality%20of%20the%20cluster,point%20to%20its%20closest%20centroid."