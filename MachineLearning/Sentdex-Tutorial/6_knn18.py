import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
import pandas as pd
import random

def k_nearest_neighbors(data, predict, k=3): #k는 랭킹 그룹
    if len(data) >= k:
        print('k is set to a value less than total voting groups!')
    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_distance, group])

    votes = [i[1] for i in sorted(distances)[:k]] #탑 k개의 group을 가져옴
    vote_result = Counter(votes).most_common(1)[0][0] # 1 -> the most common한 것(첫번째로)을 가져오고싶으면 1
    confidence = Counter(votes).most_common(1)[0][1] / k # 빈도의 확실성
    #print(vote_result, confidence)
    return vote_result, confidence

df = pd.read_csv('breast-cancer-wisconsin.data')
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)
print(df.head())
# float 변환하는 이유
# 1. everyting in the dataframe ought to be float to reuse mostlikely
# 2. replace된 값때문인지 스트링으로 취급받는 데이터가 조금씩 있기 때문에 astype으로 변환을 해줘야한다
full_data = df.astype(float).values.tolist() 
# print(full_data[:5]) # 5개 까지만샘플로 보기
random.shuffle(full_data)
# print(20*'#')
# print(full_data[:5])

# 위스콘신 데이터의 class값은 2와 4로 이루어져있다.
test_size = 0.2
train_set = {2:[], 4:[]}
test_set = {2:[], 4:[]}

train_data = full_data[:-int(test_size*len(full_data))] #상위 0.8까지
test_data = full_data[-int(test_size*len(full_data)):] #상위 0.8부터 1까지

for i in train_data:
    train_set[i[-1]].append(i[:-1]) #마지막 컬럼 값(class)을 가져옴

for i in test_data:
    test_set[i[-1]].append(i[:-1]) #마지막 컬럼 값(class)을 가져옴

correct = 0
total = 0

for group in test_set:
    for data in test_set[group]:
        #k값이 커질수록 정확도는 떨어지기도 한다. k값을 어떻게 하느냐가 결과에 영향을 줄 수 있음.
        vote, confidence = k_nearest_neighbors(train_set, data, k=5)
        if group == vote:
            correct += 1
        else:
            print(confidence) # confidence가 떨어지면 경험적인 정확도가 낮은 것이라고 할수있는듯?
        total += 1

print('Accuracy:', correct/total)