# -*- coding: utf-8 -*-
file = 'datasets/rocks_vs_mines.csv'

import pandas as pd

data = pd.read_csv(file,header=None,prefix='V')

#print data.head()
#print data.tail()

print 'Data Summary' 
print '-'*15
#print data.describe()
dataRow2= data.iloc[1,0:60]

print dataRow2.mean()
mean = 0.0
nEl = len(dataRow2)

for i in range(nEl):
    mean += dataRow2[i]/nEl

print mean