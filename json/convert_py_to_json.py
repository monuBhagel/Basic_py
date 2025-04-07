'''
- to convert a python object to a json string we use the json.dumps() method
- to convert a python object to a json file we use the json.dump() method
- to convert a json string to a python object we use the json.loads() method
- to convert a json file to a python object we use the json.load() method
'''

# Convert from Python to JSON

x = {
    "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

import json

json_string = json.dumps(x)
print(json_string)
'''
{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}
'''

# fromt the result

json.dumps(x, indent=4,separators=(". ", " = "), sort_keys=True)

'''
{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}
'''