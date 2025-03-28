'''
- we can loop through dict using  for loop
'''
car = {
    "brand" : "Ford",
    "model"  : "Mustang" , 
    "year" : 1964
}

for x in car:  # this will return keys
    print(x)
    
for x in car.keys(): # this will return keys
    print(x)
    
for x in car.values(): # this will return values
    print(x)
    
for x in car.items(): # this will return key - value pairs
    print(x)