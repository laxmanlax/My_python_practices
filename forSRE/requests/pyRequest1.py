import requests 
import json

#requests.get(url).json()

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.status_code
r.text 
r.json()


"""
r = requests.get("https://api.github.com/events")
print json.loads(r.content)
print json.loads(r.text)
print r.status_code   
"""
