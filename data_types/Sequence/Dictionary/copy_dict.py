'''
we can make copies of dict using :
    - copy() method
    - passing a dict into dictinory constructor
'''

car = {
    "brand" : "Ford",
    "model"  : "Mustang" , 
    "year" : 1964
}

car_copy = car.copy()

print(car_copy)
print(car_copy == car)


# or

car_copy_2 = dict(car)

print(car_copy_2)
print(car_copy_2 == car)

