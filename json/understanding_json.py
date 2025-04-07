'''
- JSON is a syntax for storing and exchanging data.
- JSON is text, written with JavaScript object notation.
- Python has a built-in package called json, which can be used to work with JSON data.

'''

# Parse JSON - Convert from JSON to Python
import json

with open('json/data.json', 'r') as file:
    data = json.load(file)
    
# accessing the data

print(data)
# {'name': 'John Doe', 'age': 30, 'city': 'Bengaluru', 'address': {'street': '123 Main St', 'zip': '560001'}, 'hobbies': ['reading', 'hiking', 'coding'], 'isEmployed': True, 'skills': [{'name': 'Python', 'proficiency': 'Expert'}, {'name': 'JavaScript', 'proficiency': 'Intermediate'}]}

print(data['name'])
# John Doe

