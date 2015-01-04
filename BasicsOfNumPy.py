# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 15:15:18 2014
Basics of numpy
@author: Trost
"""
import numpy as np


a = np.array([0,1,2,3,4,5])
print a.ndim
print a.shape

b = a.reshape((3,2))
print b.ndim
print b.shape

#watchout:
print '\nwatchout\n'
b[1][0] = 77
print b

print a #a has been affected, because reshape does not make a new array but just refers to the old one

#to prevent bugs: 
print '\nbugprevent\n'
c = a.reshape((3,2)).copy()
print c

c[0][0] = -99

print c
print a

#basic numeric operations

print '\n basic math\n'

print a*2

print a**2

#Use addays as indices

print '\n use arrays as indices'

print a[np.array([2,3,4])]

print a >4
print a[a>4] #can be used to trim outliers
print a.clip(0,4) # this clips everything outside ofthe interval

#Handling NaNs
print '\n handling NaN\n'

c = np.array([1,2,np.NaN,3,4]) #pretend this comes from a text file
print c
print np.isnan(c)
print c[~np.isnan(c)] #gibt c an jeder stelle aus, an der c keine NaN ist
print np.mean(c[~np.isnan(c)])

#runtime considerations. Comment in if interested

#print '\n Runtime considerations \n'
#import timeit
#normal_py_sec = timeit.timeit('sum(x*x for x in xrange(1000))',number=10000)
#
#naive_np_sec = timeit.timeit('sum(na*na)',setup="import numpy as np; na = np.arange(1000)",number=10000)
#
#good_np_sec = timeit.timeit('na.dot(na)',setup="import numpy as np; na = np.arange(1000)",number=10000)
#
#
#print("Normal python: %f sec"%normal_py_sec)
#print("Naive NumPy: %f sec"%naive_np_sec)
#print("Good NumPy: %f sec"%good_np_sec)

#arrays can only hold one typ of data

print '\n arrays cant hold too much\n'
a = np.array([1,2,3])
print a.dtype

print np.array([1,"stringy"]).dtype
print np.array( [1,"stringy",set([1,2,3])]).dtype
