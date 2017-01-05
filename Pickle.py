# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
n"""

#import pandas as pd
#import quandl
import pickle
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

#df = quandl.get('WIKI/GOOGL');

#with open('googl.pickle', 'wb') as f:
#    pickle.dump(df, f)

pickle_in = open('googl.pickle','rb')
df = pickle.load(pickle_in)

print( df.head );

xs = np.array([1,2,3,4,5,6], dtype=np.float64)
ys = np.array([5,4,6,5,6,7], dtype=np.float64)

def best_fit_slope_intercept(xs, ys):
        m = (mean(xs)*mean(ys) - mean(xs*ys)) / (mean(xs)**2 - mean(xs**2))
        b = mean(ys) - m*mean(xs)
        return m, b
        
m, b = best_fit_slope_intercept(xs, ys)        
print(m, b)

#PEMDAS - Order of execution of a python expression (paren, equals, multiply, divide, add, subtract)

regression_line = [(m*x) + b for x in xs]
      
predict_x = 8
def predict_y(x):
        return (m*x)+b

plt.scatter(xs,ys)
plt.scatter(predict_x,predict_y(predict_x), color='g')
plt.plot(xs, regression_line)
plt.show()

#square_error_y = sum((predict_y(xs[i])-ys[i])**2 for i in range(0, len(xs)-1))
#square_error_y_mean = sum((mean(ys)-ys[i])**2 for i in range(0, len(xs)-1))

square_error_y = sum(([predict_y(x) for x in xs]-ys)**2)
square_error_y_mean = sum(([mean(ys) for y in ys]-ys)**2)

r_2 = 1 - square_error_y / square_error_y_mean