import json 

f = open('jsonapp\data.json')

data = json.load(f)

for i in data['firstName']:
    print(i)