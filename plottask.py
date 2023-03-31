# squareroot.py
# This program  displays a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function h(x)=x3 in the range [0, 10], on the one set of axes.
# Author: Damien Farrell

import numpy as np
import matplotlib.pyplot as plt

hist_data = np.random.normal(size=1000, loc=5, scale=2)

plt.hist(hist_data)
plt.show()

xpoints = np.arange(0, 11)
ypoints = xpoints * 3

plt.plot(xpoints, ypoints)
plt.show()

# https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
# https://numpy.org/doc/stable/reference/generated/numpy.arange.html
# https://towardsdatascience.com/making-matplotlib-beautiful-by-default-d0d41e3534fd