# We can determine the type of a variable using the type() function.

x = 5
y = 3.14
z = "Hi"

print(type(x)) # <class 'int'>
print(type(y)) # <class 'float'>   
print(type(z)) # <class 'str'>


# Type Casting a Variable

'''python provides some in-built function to convert one data type to another. this process of conversion is called type casting .'''

# Implicit Type Casting (Automatic Conversion)

x = 10       # Integer
y = 3.5      # Float

result = x + y  # Python implicitly converts x (int) to float
print(result)    # Output: 13.5 (float)


# Explicit Type Casting (Manual Conversion)

'''Here are some common type conversion functions:

int(): Converts a value to an integer.
float(): Converts a value to a float.
str(): Converts a value to a string.
bool(): Converts a value to a boolean.'''

# Converting to Integer

x = 10.5
y = int(x) 
print(y) # 10 int type


# Converting to Float
x =10 
y = float(x)

print(y)  # 10.0 float type


#converting to string

x = 10 
y = str(x)

print(y) # 10 string type   

# converting to boolean
'''when converting to boolean "0" ,"0.0" , empty string i.e "" , empty list [], empty tuple (), empty dictinoary {} , None are considered as false . 
and all other values are considered as true. '''

x = 1 
y =bool(x)

print(y) # True boolean type

# converting complex data types

'''we can convert complex data types like list , tuple , dictionary to other data types using the respective conversion functions .'''

# List to Tuple
list_data = [1, 2, 3]
tuple_data = tuple(list_data)
print(tuple_data)  # Output: (1, 2, 3)

# Set to List
set_data = {4, 5, 6}
list_from_set = list(set_data)
print(list_from_set)  # Output: [4, 5, 6] (order may vary)


'''Note : When converting between types, especially from float to int, the data might be truncated (decimal values are lost).

Invalid Conversion: If the conversion is not possible, Python will raise a ValueError.
For example,

x = "hello"
y = int(x)  # This will raise a ValueError

trying to convert a non-numeric string to an integer
'''