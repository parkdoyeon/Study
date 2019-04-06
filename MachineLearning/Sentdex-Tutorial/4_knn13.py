# 그래프상 근접한 어떤 데이터를 그룹하기위해 사용. 
# 눈으로 확인할 수 없는 proximity를 연산을 통해 한다.
# confidence vs accuracy
# knn보다 벡터머신이 훨씬 낫다. knn은 연산속도가 너무 떨어지기 때문에.

# 여러 데이터와의 거리를 비교해서 더 가까운 경우의 그룹 수가 많은 것으로 예측한다.
# (즉, 각 모델마다 degree of confidence가 발생한다.
# 리니어 모델에서는 confidence라고라고 했는데 여기서는 accuracy하는게 더 적합함.
# 측정가능한 수치이지만 모델마다 매우 다른 양상에서 발생하므로.)
# knn은 단순한 유클리드 연산을 하기 때문에 많은 연산이 일어나고,
# 데이터셋이 많아지면 부하와 속도 문제가 생긴다. 이점에서 추후에 배우는 벡터머신이 더 나은 모델이라고 할 수 있다.

 
import numpy as np
from sklearn import preprocessing, model_selection, neighbors
import pandas as pd

df = pd.read_csv('breast-cancer-wisconsin.data')
df.replace('?', -99999, inplace=True) #데이터 row를 다 버리지말고 차라리 null값만 huge outlined data를 만들자.
df.drop(['id'], 1, inplace=True) #id라벨의, 1이면 컬럼 0이면 라인, inplace True면 원본 변경 아니면 카피(디폴트 옵션)
#의미없는 데이터니까 삭제

X = np.array(df.drop(['class'],1))
y = np.array(df['class'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2) #전체 데이터에서 20프로만 테스트
clf = neighbors.KNeighborsClassifier()
# default parameter가 있음
# clf = neighbors.KNeighborsClassifier(n_jobs=1) 1이 디폴트값이다
# linear데이터에도 사용할 수 있고, non-linear에도 사용할 수 있다.
# radius도 사용할 수 있다
# n_jobs파라미터 값을 조정하면 테스트를 여러번 돌릴수있음 -1로 하면 cpu 성능에 맞춰서 여러개 돌린다
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy) # 정확도는 0.9642857142857143, 즉 약 96%임

#example_measure = np.array([4,2,1,1,1,2,3,2,1])
example_measure = np.array([10,7,7,6,4,10,4,1,2])
example_measure = example_measure.reshape(1, -1)

# 데이터가 알수없는 길이면 이렇게 하면 편하다
# example_measure = example_measure.reshape(len(example_measure), -1)

prediction = clf.predict(example_measure)
print(prediction) #에측된 클래스 값