import csv
from math import sqrt

dataset1 = []
dataset2 = []
g = 9.8

with open("dataset1.csv", "r") as data1:
    readline = csv.reader(data1)
    for line in readline:
        dataset1.append(line)

with open("dataset2.csv", "r") as data2:
    readline = csv.reader(data2)
    for line in readline:
        dataset2.append(line)

track = {}

for name1 in dataset1:
    for name2 in dataset2:
        if name2[2]=="bipedal" and name1[0]==name2[0]:
            #print name1,name2
            STRIDE_LENGTH = float(name2[1])
            LEG_LENGTH = float(name1[1])
            speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * sqrt(LEG_LENGTH * g)
            track[name1[0]] = speed



for name in sorted(track.items(), key=lambda x:x[1], reverse=True):
    print name[0]
