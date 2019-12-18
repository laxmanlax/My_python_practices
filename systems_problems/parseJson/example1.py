import json
p = '{"name": "Bob", "languages": ["Python", "Java"]}'
person_dict = json.loads(p)
print (person_dict)
print(person_dict['languages'])

##Python read JSON file

with open('test.json') as f:
  data = json.load(f)
  for i in data["states"]:
    print i


#Convert dict to JSON
person_dict = {'name': 'Bob',
'age': 12,
'children': None
}
person_json = json.dumps(person_dict)
print(person_json)


person_dict = {"name": "Bob",
"languages": ["English", "Fench"],
"married": True,
"age": 32
}
with open('person.txt', 'w') as json_file:
  json.dump(person_dict, json_file)
