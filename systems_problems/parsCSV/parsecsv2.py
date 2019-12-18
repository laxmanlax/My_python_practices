import csv
from math import sqrt


filename = ['dataset1.csv','dataset2.csv']
track = {}
g = 9.8

for csv_file in filename:
    with open(csv_file, 'r') as re:
        csv_data = csv.DictReader(re)

        for data in csv_data:
            name = data["NAME"]
            if name not in track:
                del data["NAME"]
                track[name] = data
            else:
                del data["NAME"]
                track[name].update(data)

result = {}
for name , details in track.items():
    
    #print name, details
    try:
        if details["STANCE"]=="bipedal":
            STRIDE_LENGTH = float(details["STRIDE_LENGTH"])
            LEG_LENGTH = float(details["LEG_LENGTH"])
            speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * sqrt(LEG_LENGTH * g)
            result[name] = speed
    except:
        pass


for dino in sorted(result.items(), key=lambda x:x[1], reverse=True):
    print dino



