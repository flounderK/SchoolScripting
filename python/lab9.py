import requests
import re
import json

s = requests.session()
r = s.get("http://localhost:3000")
data = json.loads(r.content)

for i in data:
    name = i['name']
    color = i['color']
    print("{:s} is {:s}".format(name, color))
