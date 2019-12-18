import csv
from math import sqrt

track = {}

dataset1 = []
dataset2 = []

result = {}
g = 9.8

with open('dataset1.csv','r') as set1:
    read_set1 = csv.reader(set1)
    next(read_set1)
    for i in read_set1:
        dataset1.append(i)

with open('dataset2.csv', 'r') as set2:
    read_set2 = csv.reader(set2)
    next(read_set2)
    for j in read_set2:
        dataset2.append(j)

for i in range(len(dataset1)):
    for j in range(len(dataset2)):
        if dataset1[i][0]==dataset2[j][0]

            NAME = dataset1[i][0]
            STRIDE_LENGTH = float(dataset1[i][1])
            LEG_LENGTH = float(dataset2[i][1])

            #print NAME, STRIDE_LENGTH, LEG_LENGTH
            speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * sqrt(LEG_LENGTH * g)
            track[NAME] = speed

#print track
res  = sorted(track.items(), key=lambda x:x[1], reverse=True)
for name in  res:
    print name[0]


"""
for l in dataset1:
    print l

print "\n"

for m in dataset2:
    print m
"""
