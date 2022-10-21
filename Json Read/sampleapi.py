import json
f = open("Json Read/data.json")

data = json.load(f)

for i in data:
    print(i["displayTitle"])

f.close()

