#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 18:17:35 2016

@author: tom
"""
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
import operator
style.use('fivethirtyeight')

dataset = {'k':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}
new_features = [4,4.5]

#[[plt.scatter(ii[0],ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]
#plt.show()

def distance(i, j):
    return(sqrt((i[0]-j[0])**2 + (i[1]-j[1])**2))
    
def k_nearest_neighbors(data, predict, k=3):
    if len(data) >= k:
        warnings.warn('K is set to a value less than total voting groups')
    
    distances = [[{'cat':i, 'd':distance(ii,predict)} for ii in dataset[i]] for i in dataset]
    flat = np.array(distances).flatten()
    flat = sorted(flat, key=operator.itemgetter('d'))
    vote_result = Counter([x['cat'] for x in flat[:k]])
    
    return vote_result.most_common(1)
    
x = k_nearest_neighbors(dataset, new_features, 3);