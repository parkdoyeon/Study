from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

xs = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
ys = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64) #just being explicit with data type

#plt.scatter(xs, ys)
#plt.show()

def best_fit_slope(xs, ys):
    m = ( ((mean(xs)*mean(ys))-(mean(xs*ys))) /
            ((mean(xs))**2-mean(xs**2)) )
    return m

def best_fit_slope_and_intercept(xs, ys):
    m = ( ((mean(xs)*mean(ys))-(mean(xs*ys))) /
            ((mean(xs))**2-mean(xs**2)) )
    b = mean(ys)-m*mean(xs)
    return m, b

m = best_fit_slope(xs, ys)
m, b = best_fit_slope_and_intercept(xs, ys)
print(m) # 0.42857142857142866, positive relation이라서 양수로 나옴
print(m, b) # 0.42857142857142866, 4.0


regression_line = [(m*x+b) for x in xs]
predict_x = 8
predict_y = (m*predict_x)+b

print(regression_line)
plt.scatter(xs, ys)
plt.scatter(predict_x, predict_y, color='g')
plt.plot(xs, regression_line)
plt.show()