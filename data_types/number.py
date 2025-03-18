# Python Numbers

'''there are three numeric types in python :

1. int 
2. float
3. complex

note: variable of numberic types are created when you assign a value to them.

'''

# Example : 

x = 5 # int
y = 5.0 # float
z = 5J # complex

print(f"type of x : {type(x)}")
print(f"type of y : {type(y)}")
print(f"type of z : {type(z)}")

# Int : 
'''
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
'''

# Float :
'''
Float, or "floating point number" is a number, positive or negative, containing one or more decimal.
Float can also be scientific numbers with an "e" to indicate the power of 10.
'''

f = 35e3
g = 35 * 10**3

print(f==g)

# Complex :
'''
Complex numbers are written with a "j" as the imaginary part:
'''

a = 3+5j
b =5j
c = -5j

print(f"type of a : {type(a)}")
print(f"type of b : {type(b)}")
print(f"type of c : {type(c)}")



# Extra :

'''      Random Number
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
'''

import random 

ran = random.randrange(1,50)

print(ran)

print(f"data type of ran : {type(ran)}")