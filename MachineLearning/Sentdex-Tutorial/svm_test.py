import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot([1,1], [2,2], 'k')