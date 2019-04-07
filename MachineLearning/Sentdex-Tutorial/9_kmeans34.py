import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans

#flat clustering

X = np.array([[1,2],
[1.5, 1.8],
[5, 8],
[8, 8],
[1, 0.6],
[9, 11]])

# plt.scatter(X[:,0], X[:,1], s=150, linewidth=5) #X의 첫번째 값과 X의 모든 두번째 값끼리 매치, 넘파이에서만 가능
# plt.show()

clf = KMeans(n_clusters=3) #default is 8
clf.fit(X)

centroids = clf.cluster_centers_
labels = clf.labels_ # array of lebels(lower case y)

colors = 10*['g.', 'r.', 'c.', 'b.', 'k.']

for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=25) # since we have only 2 clusters, labels only be 0 or 1
plt.scatter(centroids[:,0], centroids[:,1], marker='x', s=150, linewidths=5)
plt.show()