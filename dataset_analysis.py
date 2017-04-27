#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import numpy as np


file = 'datasets/rocks_vs_mines.csv'


xList = []
labels =[]

data = open(file,'r')

for line in data:
    row = line.strip().split(',')
    xList.append(row)
    
nrow = len(xList)
ncol = len(xList[1])

print 'Analysis of dataset' 
print '-'*30
print 'Number of samples:\t %d' % nrow
print 'Number of attributes:\t %d' % ncol
print '-'*30
print 'Type of attributes'
print 'Col#\tNumber\tString\tOther'

type = [0]*3
colCounts = []


for col in range(ncol):
    for row in xList:
        try:
            a= float(row[col])
            if isinstance(a,float):
                type[0] += 1
        except ValueError:
            if len(row[col]) > 0:
                type[1] += 1
            else:
                type[2] += 1
    colCounts.append(type)
    type = [0]*3
    
iCol = 1

for types in colCounts:
    print '%d\t%d\t%d\t%d' % (iCol, types[0],types[1],types[2])
    iCol += 1
    
print '-'*30
#stats on specific column - col
col = 3
colData = []

for row in xList:
    colData.append(float(row[col]))
    
colArray = np.array(colData)
colMean = np.mean(colArray)
colMedian = np.median(colArray)
colsd = np.std(colArray)

print 'Mean : %s | Median: %s | Std.Deviation: %s' % (str(colMean),
                                                        str(colMedian),str(colsd))

print '-'*15
ntiles = 4
percentBdry = []
for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray, i*(100)/ntiles))
print 'Boundaries for 4 Equal Percentiles'
print percentBdry
print '-'*15

#run again with 10 equal intervals


ntiles = 10
percentBdry = []
for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray, i*(100)/ntiles))
#The last column contains categorical col = 60
print 'Boundaries for 10 Equal Percentiles'
print percentBdry
print '-'*15
col = 60

colData = []
for row in xList:
    colData.append(row[col])
unique = set(colData)

print 'Unique Label Value', unique
#count up the number of elements having each value
catDict = dict(zip(list(unique),range(len(unique))))
catCount = [0]*2
for elt in colData:
    catCount[catDict[elt]] += 1

print list(unique)
print catCount

























    
