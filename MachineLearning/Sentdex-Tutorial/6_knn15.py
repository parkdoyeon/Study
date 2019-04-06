import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter

style.use('fivethirtyeight')

# k nearest neighbor를 보여주기위한 샘플데이터 그리기
dataset = {'k': [[1,2], [2,3], [3,1]], 'r': [[6,5], [7,7], [8,6]]}
new_features = [5,7]

# 그래프 생성
# [[plt.scatter(ii[0], ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]
# plt.scatter(new_features[0], new_features[1])
# plt.show()


# knn의 핵심 문제: 예측을 하기위해 모든 데이터 포인트와 유클리디안거리를 비교해야함
# radius를 구해서 그 근방의 값이랑만 비교하면 조금 해소할 수 있음
def k_nearest_neighbors(data, predict, k=3): #k는 랭킹 그룹
    if len(data) >= k:
        print('k is set to a value less than total voting groups!')
    distances = []
    for group in data:
        for features in data[group]:
            #본래 사용해야하는 수식은 이거지만
            #euclidean_distance = sqrt((plot1[0]-plot2[0])**2+(plot1[1]-plot2[1])**2)
            #더 빠른 연산을 하기 위해서 다른 버전을 사용하자
            #euclidean_distance = np.sqrt(np.sum((np.array(features)-np.array(predict))**2))
            #하지만 넘파이는 더 단순한 버전이 있다
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_distance, group])

    votes = [i[1] for i in sorted(distances)[:k]] #탑 k개의 group을 가져옴
    print(Counter(votes).most_common(1)) # ex) [(2, 4)] 형태로 출력됨, 2:가장 공통된 요소값, 4:출현 빈도
    vote_result = Counter(votes).most_common(1)[0][0] # 1 -> the most common한 것(첫번째로)을 가져오고싶으면 1

    return vote_result

result = k_nearest_neighbors(dataset, new_features, k=3)
print(result)

[[plt.scatter(ii[0], ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]
plt.scatter(new_features[0], new_features[1], color=result)
plt.show()