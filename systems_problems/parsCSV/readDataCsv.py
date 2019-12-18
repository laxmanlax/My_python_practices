import csv
from math import sqrt

filenames = "dataset1.csv", "dataset2.csv"

result = {}
g = 9.8

for filename in filenames:
    with open(filename, "rb") as fp: # python 2
        reader = csv.DictReader(fp)
        for d in reader:
            name = d["NAME"]
            if name not in result:
                del d["NAME"]
                result[name] = d
            else:
                del d["NAME"]
                result[name].update(d)

track = {}

for name, val in result.items():
    try:
        if val["STANCE"] == "bipedal":
            STRIDE_LENGTH = float(val["STRIDE_LENGTH"])
            LEG_LENGTH = float(val["LEG_LENGTH"])
            speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * sqrt(LEG_LENGTH * g)
            track[name]= speed
    except:
        pass


for dino in sorted(track.items(), key=lambda x:x[1], reverse=True):
    print dino[0]
