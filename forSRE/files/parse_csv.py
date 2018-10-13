'''
f = open("football.csv","r")

for row in f:
    print row.split(",")

'''

import csv


def read_data(data):
    with open(data, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    return data


# ---- run code ---- #

data = "football.csv"
print read_data(data)
