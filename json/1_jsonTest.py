import json

jsonString = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'

# convert json to python dict
dict = json.loads(jsonString)
print(dict)
print(type(dict))

# convert dict to json
print('------------------')
jsonNew = json.dumps(dict)
print(jsonNew)
print(type(jsonNew))

# use requests module to get response from a json endpoint and then work with that dictionary as shown above
