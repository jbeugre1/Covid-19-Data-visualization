# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:23:37 2020

@author: Maryam Botrus 
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import csv

def func(x, a, b):
    return a*np.power(x, b)

def harm(x, a, b, c):
    return a * np.sin(b * x) + c*x

def loga(x, a, b, c):
    return a * np.log(b * x)

# prints out positive case totals in the state of california change
# names to change state
    
# only edit this for loading another csv file
# Ex: for Georgia 'georgia-history.csv' , 'Georgia'    
names = ['texas-history.csv','Texas']


# don't change anything below this line 

california_data = []
with open(names[0]) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        #print(row)
        california_data.append(row[20]) # use 12 for national 20 for others
        
# clip positive string from top of list 
california_data = california_data[1:-1]  
# reverse list
california_data = california_data[::-1]

# build list as floats
california_num = []
for my_entry in california_data:
    california_num.append(float(my_entry))

   
# do model projections for California 

x_data = np.linspace(1,len(california_num),len(california_num))
y_data = np.asarray(california_num)
plt.plot(x_data,y_data,color='b', marker='.')

# try third order poylnomial
coef = np.polyfit(x_data,y_data, 5)
equ = np.poly1d(coef)

# project out 30 days
project = 30 
x_proj = np.linspace(1,len(california_num)+project,len(california_num)+project) 
y_proj = equ(x_proj)
plt.plot(x_proj,y_proj,color = 'r')

# try power law
popt1, pconv = curve_fit(func, x_data,y_data)
plt.plot(x_proj, func(x_proj, *popt1))

# try harmonic curve
popt2, pconv = curve_fit(harm, x_data,y_data)
plt.plot(x_proj, harm(x_proj, *popt2))

# try logarthmic regression
popt3, pconv = curve_fit(loga, x_data,y_data)
plt.plot(x_proj, loga(x_proj, *popt3))

plt.title(names[1] + ' Coronavirus Cases')
plt.ylabel('Number of Positive Cases')
plt.xlabel('Days Since March 3rd 2020')
plt.legend(['Real Data','5th-Order Poly Project','Power Law','Harmonic','Log Regression'])
plt.ylim([0,np.max((loga(x_proj,*popt3),harm(x_proj,*popt2),func(x_proj,*popt1),y_proj))])
plt.show()

        #print(row[20])
#california_csv = np.genfromtxt('california-history.csv',delimiter=",")1