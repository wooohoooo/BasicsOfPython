# -*- coding: utf-8 -*-
"""
Created on Sun Jan  4 01:04:11 2015

@author: Trost
"""

import pandas as pd

####IMPORTANTE: STUPID BOOKRATINGSFILE contained "-",which is unusable. Changed it to "_"

ugly = pd.read_csv("BX-Book-Ratings.csv",header=0,sep=";",encoding = "ISO-8859-1")

print(ugly.describe())

print(ugly.head())
print(ugly.tail())

print(ugly[1:5])

print(ugly.dtypes)


print("\n")


print(ugly['User_ID'].head())
print(ugly[['User_ID','ISBN']].head())

print("\n")

print(ugly[ugly.User_ID==170155])








