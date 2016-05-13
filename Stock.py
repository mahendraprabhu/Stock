# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 17:12:05 2015

@author: mramacha
"""

import pandas
import pandas.io.data
import datetime
import matplotlib.pyplot as plt

# Window length for moving average
window_length = 200

# Dates
start = datetime.datetime(2014, 1, 1)
end = datetime.datetime(2015, 8, 4)

# Get data
#data = pandas.io.data.DataReader('CVX', 'yahoo', start, end)
data = pandas.io.data.DataReader('OIL', 'yahoo', start)
# Get just the close
close = data['Adj Close']

MA_200 = pandas.stats.moments.ewma(close, 200)
MA_15 = pandas.stats.moments.ewma(close, 50)

plt.clf
MA_200.plot()
MA_15.plot()
close.plot()

# Adding some additional data

# Get the difference in price from previous step
#delta = close.diff()
## Get rid of the first row, which is NaN since it did not have a previous 
## row to calculate the differences
#delta = delta[1:] 
#
## Make the positive gains (up) and negative gains (down) Series
#up, down = delta.copy(), delta.copy()
#up[up < 0] = 0
#down[down > 0] = 0
#
## Calculate the EWMA
#roll_up1 = pandas.stats.moments.ewma(up, window_length)
#roll_down1 = pandas.stats.moments.ewma(down.abs(), window_length)
#
## Calculate the RSI based on EWMA
#RS1 = roll_up1 / roll_down1
#RSI1 = 100.0 - (100.0 / (1.0 + RS1))
#
## Calculate the SMA
#roll_up2 = pandas.rolling_mean(up, window_length)
#roll_down2 = pandas.rolling_mean(down.abs(), window_length)
#
## Calculate the RSI based on SMA
#RS2 = roll_up2 / roll_down2
#RSI2 = 100.0 - (100.0 / (1.0 + RS2))
#
## Compare graphically
#plt.figure()
#RSI1.plot()
#RSI2.plot()
#plt.legend(['RSI via EWMA', 'RSI via SMA'])
#plt.show()