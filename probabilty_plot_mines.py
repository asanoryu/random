# -*- coding: utf-8 -*-
file = 'datasets/rocks_vs_mines.csv'

import numpy as np
import pylab
import scipy.stats as stats

xList = []
labels =[]

data = open(file,'r')

for line in data:
    row = line.strip().split(',')
    xList.append(row)
    
nrow = len(xList)
ncol = len(xList[1])

type =[0]*3

colCounts = []

col = [1,2,3]
colData = []

for row in xList:
    colData.append(float(row[col[2]]))
    
stats.probplot(colData, dist='norm',plot=pylab)
pylab.show()
