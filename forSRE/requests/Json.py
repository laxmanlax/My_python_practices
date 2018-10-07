import json 

test_string = '''
{
    "people":[
        {
        "name":"John Smith",
        "phone": "123345",
        "email": ["laxman@gmail.com","john@gmail.com"]
        },
        {
        "name":"Laxman Goswami",
        "phone": "123345",
        "email": ["laxman@gmail.com","john@gmail.com"]
        }
    ]
}
'''
data = json.loads(test_string)
print data , type(data)

new_str = json.dumps(data, indent=2)
print new_str, type(new_str)