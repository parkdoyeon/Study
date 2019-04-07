import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.datasets.samples_generator import make_blobs
import random

#centers = random.randrange(2, 8)
#X, y = make_blobs(n_samples=50, centers=centers, n_features=2)

X = np.array([[1,2], [1.5,1.8], [5,8], [8,8], [1, 0.6], [9,11], [8,2], [10,2], [9,3]])

# plt.scatter(X[:,0], X[:,1], s=150)
# plt.show()

colors = 10*['g', 'r', 'c', 'b', 'k']

class Mean_Shift:
    def __init__(self, radius=None, radius_norm_step=100):
        self.radius = radius
        self.radius_norm_step = radius_norm_step
    
    def fit(self, data):

        if self.radius == None:
            all_data_centroid = np.average(data, axis=0) #axis값, 평균 기준(x,y값의평균? 혹은 x값만의 평균?)을 어디다 낼것인가를 정하는 파라미터. 0이면 x, y 점 사이의 평균이다.
            all_data_norm = np.linalg.norm(all_data_centroid) #원점과 중심점간의 거리값, radius 최대치 구하기
            self.radius = all_data_norm / self.radius_norm_step

        centroids = {}

        for i in range(len(data)):
            centroids[i] = data[i]

        weights = [i for i in range(self.radius_norm_step)][::-1] #reversed step

        while True:
            new_centroids = []
            for i in centroids:
                in_bandwidth = []
                #weight_list=[ ]  # To have weights for np.average
                centroid = centroids[i]

                for featureset in data:
                    distance = np.linalg.norm(featureset-centroid)
                    if distance == 0:
                        distance = 0.00000001
                    weight_index = int(distance/self.radius)

                    if weight_index > self.radius_norm_step-1: #weight가 radius_norm에서 정한 최대 radius보다 크면 마지막 인덱스 값으로 고정한다.
                        weight_index = self.radius_norm_step-1
                    
                    # 앞으로 center of mass를 찾을때 가까운 점에는 가중치를 줘야하는데, 이를 주기위해 인위적으로 list의 크기를 직접 weight값을 찾아서 제곱해버리는 식으로 확장한다 (방법1)
                    # sentdex도 이 방법이 최적의 방법이라고 보긴 어렵다고 코멘트 했다.
                    # 유투브에 댓글 보면 아예 np.average에서 제공하는 weight패러미터에 직접 리스트의 크기를 넣으라는 얘기가 있다. (방법2)
                    #방법1
                    to_add = (weights[weight_index]**2)*[featureset] #
                    in_bandwidth += to_add

                    #방법2
                    #weight_list.append(weights[weight_index])
                    #in_bandwidth.append(featureset)

                #방법1
                new_centroid = np.average(in_bandwidth, axis=0)
                #방법2
                #new_centroid = np.average(in_bandwidth,axis=0,weights=np.array(weight_list))

                new_centroids.append(tuple(new_centroid))
            
            uniques = sorted(list(set(new_centroids)))
            to_pop = []
            for i in uniques:
                for ii in [i for i in uniques]:
                    if i == ii:
                        pass
                    elif np.linalg.norm(np.array(i)-np.array(ii)) <= self.radius:
                        to_pop.append(ii) #one step radius
                        break
            for i in to_pop:
                try:
                    uniques.remove(i)
                except:
                    pass

            prev_centroids = dict(centroids) #deep copy를 위해 dict

            centroids = {}
            for i in range(len(uniques)):
                centroids[i] = np.array(uniques[i])
            
            optimized = True

            for i in centroids:
                if not np.array_equal(centroids[i], prev_centroids[i]): #이전 센트로이값과 같으면 최적화가 끝남!
                    optimized = False
                if not optimized:
                    break
            
            if optimized:
                break
        
        self.centroids = centroids
        self.classifications = {}

        for i in range(len(self.centroids)):
            self.classifications[i] = []
        
        for featureset in data:
            distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
            classification = distances.index(min(distances))
            self.classifications[classification].append(featureset)

    def predict(self, data):
        distances = [np.linalg.norm(featureset-self.centroids) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification

clf = Mean_Shift()
clf.fit(X)

centroids = clf.centroids

for classification in clf.classifications:
    color = colors[classification]
    for featureset in clf.classifications[classification]:
        plt.scatter(featureset[0], featureset[1], marker='x', color=color, s=150,)

for c in centroids:
    plt.scatter(centroids[c][0], centroids[c][1], color='k', marker='*', s=150)

plt.show()
