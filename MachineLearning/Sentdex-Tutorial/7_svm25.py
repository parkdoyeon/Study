https://pythonprogramming.net/predictions-svm-machine-learning-tutorial/ 에 있는 강의와 코드를 설명한 글입니다.

아래와 같은 2차원 데이터가 있다고 가정하자.
딕셔너리 타입으로 -1와 1로 클래스를 구분해서 작성한다.
<pre><code>data_dict = {
    -1: np.array([[1,7],
    [2,8],
    [3,8],]),
    1: np.array([[5,1],
    [6,-1],
    [7,3],]) }</code></pre>


import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

class Support_Vector_Machine:
    def __init__(self, visualization=True):
        self.visualization = visualization
        self.colors = {-1:'b', 1:'r'}
        if self.visualization:
            self.fig = plt.figure() # actual figure of the wholemost window
            self.ax = self.fig.add_subplot(1,1,1) # specific subplot

    # train
    def fit(self, data):
        self.data = data
        # { ||w||: [w,b]}
        opt_dict = {}
        transforms = [[1,1],[-1,1],[-1,-1],[1,-1]]

        all_data = []
        for yi in self.data:
            for featureset in self.data[yi]:
                for feature in featureset:
                    all_data.append(feature)
        self.max_feature_value = max(all_data)
        self.min_feature_value = min(all_data)
        all_data = None

        # sklearn.svm.svc: max_iter
        step_sizes = [self.max_feature_value * 0.1, # quicker reseponse
                    self.max_feature_value * 0.01,
                    #point of expense (slower, but more precise):
                    self.max_feature_value * 0.001]
        
        # b doesn't have to have smaller steps unlike w
        # extremely expensive
        # w처럼 step단위로 끊어서 테스트할수도 있지만 b는 그만큼의 중요도를 갖고있는 상수도 아니거니와
        # 최적화 문제에 있어서 속도/성능 문제가 발생하므로 이번에는 최대한 심플하게 임의의 수를 지정한다.
        b_range_multiple = 2
        b_multiple = 5

        # first value of vector w, major corner we are gonna cut.
        latest_optimum = self.max_feature_value*10

        for step in step_sizes:
            w = np.array([latest_optimum, latest_optimum])
            optimized = False
            while not optimized:
                for b in np.arange(-1*(self.max_feature_value*b_range_multiple),
                                        self.max_feature_value*b_range_multiple,
                                        step*b_multiple):
                    for transformation in transforms:
                        w_t = w*transformation
                        found_option = True

                        # weakest link in the SVM fundamentally
                        # SMO attemps to fix this bit
                        # yi(xi*w+b) >= 1
                        # #### add a break later..
                        for i in self.data:
                            for xi in self.data[i]:
                                yi = i
                                # sklearn.svm.svc: tol
                                if not yi*(np.dot(w_t,xi)+b) >= 1:
                                    found_option = False
                                    #이 샘플에서는 더 찾을 필요가 없음.

                        if found_option:
                            opt_dict[np.linalg.norm(w_t)] = [w_t, b] # { ||w||: [w,b]}
                        
                if w[0] < 0:
                    optimized = True
                    print('Optimized a step.')
                else:
                    # ex) w = [5,5]
                    # step = 1
                    # w - step = [4,4]
                    w = w-step
            norms = sorted([n for n in opt_dict])
            # ||w||: [w,b]
            opt_choice = opt_dict[norms[0]] # sorted 된 제일 낮은 ||w||의 [w, b]를 가져온다
            self.w = opt_choice[0]
            self.b = opt_choice[1]
            latest_optimum = opt_choice[0][0]+step*2 ##w의 x값+단위*2

    def predict(self, features):
        # sign(x.w+b)
        classification = np.sign(np.dot(np.array(features), self.w)+self.b)
        if classification != 0 and self.visualization:
            self.ax.scatter(features[0], features[1], s=200, marker='*', c=self.colors[classification])
        return classification

    def visualize(self):
        [[self.ax.scatter(x[0], x[1], s=100, color=self.colors[i]) for x in data_dict[i]] for i in data_dict]

        # hyperplane = x*w + b
        # v = x*w+b
        # positive sv = 1, negative sv = -1, decision point = 0
        def hyperplane(x, w, b, v):
            print(w)
            return (-w[0]*x-b+v)/w[1]

        datarange = (self.min_feature_value*0.9, self.max_feature_value*1.1)
        hyp_x_min = datarange[0]
        hyp_x_max = datarange[1]

        # w*x+b = 1
        # positive support vector hyperplane
        psv1 = hyperplane(hyp_x_min, self.w, self.b, 1)
        psv2 = hyperplane(hyp_x_max, self.w, self.b, 1)
        self.ax.plot([hyp_x_min, hyp_x_max], [psv1, psv2], 'k')
        print(psv1)
        print(psv2)
        print('---')

        # w*x+b = -1
        # negative support vector hyperplane
        nsv1 = hyperplane(hyp_x_min, self.w, self.b, -1)
        nsv2 = hyperplane(hyp_x_max, self.w, self.b, -1)
        self.ax.plot([hyp_x_min, hyp_x_max], [nsv1, nsv2], 'k')

        # w*x+b = 0
        # dicision boundary
        db1 = hyperplane(hyp_x_min, self.w, self.b, 0)
        db2 = hyperplane(hyp_x_max, self.w, self.b, 0)
        self.ax.plot([hyp_x_min, hyp_x_max], [db1, db2], 'y--')

        plt.show()


data_dict = {
    -1: np.array([[1,7],
    [2,8],
    [3,8],]),
    1: np.array([[5,1],
    [6,-1],
    [7,3],]) }
svm = Support_Vector_Machine()
svm.fit(data=data_dict)

predict_us = [[0,10], [1,3], [3,4], [3,5], [5,5], [5,6], [6,-5], [5,8]]
for p in predict_us:
    svm.predict(p)

svm.visualize()