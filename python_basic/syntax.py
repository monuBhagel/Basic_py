# This file contains the basic syntax of python programming language , which includes:
# - Comments
# - Print statement
# - Variables and data types
# - Lists
# - Tuples
# - Dictionaries
# - Conditional statements
# - Loops
# - Functions
# - Classes and Objects

# This is a comment in Python . the comment in python is denoted by '#' symbole.
"""for multi-line comment we use ''' ''' or """ """ i.e triple quotes
this is multi-line comment in python.
Also comments are not executed by python interpreter and are used for understanding the code / documentation and debugging purpose.
"""

# Print statement
print("Hello, World!")

# Variables and data types
x = 5           # Integer
y = 3.14        # Float
name = "Alice"  # String
is_student = True  # Boolean

# Lists
fruits = ["apple", "banana", "cherry"]

# Tuples
coordinates = (10.0, 20.0)

# Dictionaries
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Conditional statements
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Loops
# For loop
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Classes and Objects
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

my_dog = Dog("Buddy", 3)
print(my_dog.name)
print(my_dog.bark())