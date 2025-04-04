'''
- python is an object-oritented programming language.
- everything in python is an object. with its properties and methods.

- A class is like an object constructor or say a blueprint for creating an object.
- An object is an unique instance of a class.

- to create a class , we use the keyword "class". 

'''

# creating a class :

class Number:
    x = 10 
    
    def greet(self):
        print("hello world")
    
    
#  creating an object of class

num  = Number() # num is the object of class number

# accessing properties and method of class using object.

print(num.x)

num.greet()


# The __init__() Function
'''
- All classes have a function called __init__(), which is always executed when the class is being initiated.
- Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
- The __init__() function is called automatically every time the class is being used to create a new object.
- the sefl parameter is a refernce to the current instance of the class and is used to access variables that belong to the class.

'''

class person:
    # constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
p1 = person("ram" , 21)

print(p1.name)
print(p1.age)

print(p1)  # <__main__.person object at 0x1007d2120>


#  The __str__() Function
'''
- The __str__() function controls what should be returned when the class object is represented as a string.
- If the __str__() function is not set, the string representation of the object is returned:
'''

class person : 
     def __init__(self, name, age):
      self.name = name
      self.age = age
      
     def __str__(self):
         return f"{self.name}({self.age})"


p2 = person("John", 36)
print(p2) 


# methods inside class

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self): # user-defined method
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# Modify Object Properties
# to do such just asscess the property and assign new value to it.
print(p1.age)
p1.age =30
print(p1.age)


# Delete Object Properties
# You can delete properties on objects by using the del keyword:

del p1.age

# print(p1.age) # AttributeError: 'Person' object has no attribute 'age'
