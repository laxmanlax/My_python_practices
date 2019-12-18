import csvs
from math import sqrt
g = 9.8

filenames = ['dataset1.csv','dataset2.csv']


track = {}
for dataset in filenames:

    with open(dataset, 'r') as file:
        csvdata = csv.DictReader(file)

        for line in csvdata:
            name = line["NAME"]
            if name not in track:
                del line["NAME"]
                track[name]= line
            else:
                del line["NAME"]
                track[name].update(line)
result = {}

for k,v in track.items():

    try:
        if v["STANCE"] == "bipedal":
            #print k,v
            STRIDE_LENGTH = float(v["STRIDE_LENGTH"])
            LEG_LENGTH = float(v["LEG_LENGTH"])
            speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * sqrt(LEG_LENGTH * g)
            result[k] = speed
    except:
        pass

print result
for name in sorted(result.items(), key=lambda x:x[1], reverse=True):
    print name
