# plottask.py
# This program  displays a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function h(x)=x3 in the range [0, 10], on the one set of axes.
# Author: Damien Farrell

# Import Modules.
import numpy as np
import matplotlib.pyplot as plt

# Setting the colour list
CB91_Green = '#47DBCD'
CB91_Blue = '#2CBDFE'
CB91_Pink = '#F3A0F2'
CB91_Purple = '#9D2EC5'
CB91_Violet = '#661D98'
CB91_Amber = '#F5B14C'

# Set font size as:
title_fontsize = 15
axis_fontsize = 12

color_list = [CB91_Green, CB91_Pink, CB91_Blue, CB91_Amber,
              CB91_Purple, CB91_Violet]
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=color_list)

# Set up random numpy normalised hist data with a mean of 5 and sd of 2.
hist_data = np.random.normal(size=1000, loc=5, scale=2)

# Histogram formatting
plt.legend()
plt.grid(True)
plt.title('Histogram', fontsize=title_fontsize)
plt.xlabel('Value', fontsize=axis_fontsize)
plt.ylabel('Frequency', fontsize=axis_fontsize)

# Plot a histogram data with matplotlib.
plt.hist(hist_data)
plt.show()

# Setting the data for a line plot.
xpoints = np.arange(0, 11)
ypoints = xpoints * 3

# Line plot formatting
plt.legend()
plt.grid(True)
plt.title('Line Plot', fontsize=title_fontsize)
plt.xlabel('X Points', fontsize=axis_fontsize)
plt.ylabel('Y Points', fontsize=axis_fontsize)

# Plotting the line plot. 
plt.plot(xpoints, ypoints, linestyle='--', alpha=0.5)
plt.show()