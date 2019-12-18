import csv
from math import sqrt


g = 9.8

filenams =  ["dataset1.csv","dataset2.csv"]

dino_records = {}
for data_file in filenams:
    with open(data_file,'r') as read_line:
        datasets = csv.DictReader(read_line)

        for line in datasets:
            #print line
            name = line["NAME"]
            if name not in dino_records:
                del line["NAME"]
                dino_records[name] = line
            else:
                del line["NAME"]
                dino_records[name].update(line)

track  = {}

for name , val in dino_records.items():
    try:
        if val["STANCE"] == "bipedal":
            STRIDE_LENGTH = float(val["STRIDE_LENGTH"])
            LEG_LENGTH = float(val["LEG_LENGTH"])
            speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * sqrt(LEG_LENGTH * g)
            track[name] = speed
    except:
        pass


for res in sorted(track.items(), key=lambda x:x[1], reverse=True):
    print res[0]
