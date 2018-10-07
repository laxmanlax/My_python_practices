import json 

with open("test1.json") as f:
    data = json.load(f)

for state in data["states"]:
    print state 