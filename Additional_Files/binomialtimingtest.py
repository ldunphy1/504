# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 23:13:38 2016

@author: montgomt
"""

import random
from binomialheapTimed import BinomialHeap



    
print('time test started')

timelog = []

values = list(range(1,50))
random.shuffle(values)

H = BinomialHeap()

'''inserting all values'''
print('\ninserting')
for v in values:
    t = H.insertNode(v,str(v))
    timelog = timelog + t
    
'''extracting a few minimums'''
print('\nextracting')
for i in range(10):
    v,k,t = H.extractMin()
    timelog = timelog + t
    
print('\nprinting results')
for row in timelog:
    print(row)