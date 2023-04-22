# plottask.py
# This program  displays a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function h(x)=x3 in the range [0, 10], on the one set of axes.
# Author: Damien Farrell


# Import Modules.
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot') # Uses style template

# Set font size as:
title_fontsize = 15
axis_fontsize = 12

# Set up random numpy normalised hist data with a mean of 5 and sd of 2.
hist_data = np.random.normal(size=1000, loc=5, scale=2)

# Setting the data for a line plot.
xpoints = np.arange(0, 11)
ypoints = xpoints * 3

# Create a figure and axis
fig, ax1 = plt.subplots()

# Histogram formatting
ax1.hist(hist_data, alpha=0.7, label='Histogram')
ax1.set_xlabel('Value', fontsize=axis_fontsize)
ax1.set_ylabel('Frequency', fontsize=axis_fontsize, color='C0')
ax1.tick_params(axis='y', labelcolor='C0')

# Line plot formatting
ax2 = ax1.twinx()
ax2.plot(xpoints, ypoints, linestyle='--', alpha=0.5, color='C1', label='Line Plot')
ax2.set_ylabel('Y Points', fontsize=axis_fontsize, color='C1')
ax2.tick_params(axis='y', labelcolor='C1')

# Set the title for both plots
plt.title('Histogram and Line Plot', fontsize=title_fontsize)

# Adding a legend to the plot
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='best')

plt.show()