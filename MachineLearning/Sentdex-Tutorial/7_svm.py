# support vector machine: SVM
# support vector + machine
# 60's에 만들어졌으나 90's까지 잘 알려지지 않다가 나중에 알려짐
# 기본적으로 2가지(binary) 데이터로 나눔
# 2차원, 많아봤자 3차원 데이터까지만 다룸

import numpy as np
from sklearn import preprocessing, model_selection, neighbors, svm
import pandas as pd

df = pd.read_csv('breast-cancer-wisconsin.data')
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True) # id 칼럼 안바꾸면 정확도가 약 30퍼센트 정도나 떨어지는걸 알 수있음.
 
X = np.array(df.drop(['class'],1))
y = np.array(df['class'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
clf = svm.SVC()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy) # 정확도는 0.9642857142857143, 즉 약 96%임

#example_measure = np.array([4,2,1,1,1,2,3,2,1])
example_measure = np.array([10,7,7,6,4,10,4,1,2])
example_measure = example_measure.reshape(1, -1)

prediction = clf.predict(example_measure)
print(prediction) #에측된 클래스 값