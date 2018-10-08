import requests 
import json 
r = requests.get("https://api.github.com/events")


#print r.content
print json.loads(r.text.encode())
print r.status_code   