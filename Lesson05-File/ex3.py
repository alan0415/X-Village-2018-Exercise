import json

with open('SearchShowAction.json',encoding = 'utf8') as f:
    person = json.load(f)
    print(json.dumps(person, indent=2,separators=(',',':')))