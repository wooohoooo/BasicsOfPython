# -*- coding: utf-8 -*-
"""
Created on Sun Jan  4 01:04:11 2015

@author: Trost
"""

import pandas as pd

####IMPORTANTE: STUPID BOOKRATINGSFILE contained "-",which is unusable. Changed it to "_"

ugly = pd.read_csv("..\\Material\\BX-Book-Ratings.csv",header=0,sep=";",encoding = "ISO-8859-1")

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

print('Uglytest \n')
print(ugly[ugly.User_ID==170155][['ISBN','Book_Rating']].head())

#Books = ugly[ugly.User_ID=170155]['ISBN'].head()


Books = ugly[ugly.User_ID==170155][['ISBN']]
print(Books.head())
#a = Books.index
#a= Books[['ISBN']]
a = Books.ISBN
a = list(a)
#a = list(a)
for book in a[-5:-1]:
    print("dayum")
    print(book)
    print(ugly[ugly.ISBN == book])
#



#Ratings = ugly[ugly.User_ID==170155][['Book_Rating']]



#print users[['age', 'zip_code']].head()
#print '\n'
#
## can also store in a variable to use later
#columns_you_want = ['occupation', 'sex'] 
#print users[columns_you_want].head()







