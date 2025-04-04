'''
- Inheritance allows us to define a class that inherits all the methods and properties from another class.

- Parent class is the class being inherited from, also called base class.

- Child class is the class that inherits from another class, also called derived class.

- The child class can:
   -  Inherit all the attributes and methods from the parent class.
   -  Override the methods of the parent class to provide specific functionality.
   -  Add new attributes and methods specific to the child class.
   


'''

# creating a parent class 

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# creating a child class :

class Student(Person):
  pass # as you can see we don't have any methods or properties in the child class of it owns.


child_class = Student("Mike", "Olsen")
child_class.printname()


'''
- if we have __init__ method in parent class and not in child class, then the child class will use and inherit the __init__ method of the parent class .

- but if we do have The child's __init__() function ,then it will overrides the inheritance of the parent's __init__() function.
'''

# Use the super() Function
'''
- Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
'''

class Student(Person):
  def __init__(self, fname, lname, gradyear):
    super().__init__(fname, lname)
    # Add Properties
    self.gradyear = gradyear
    

std1 = Student("sam" , "willson" , 2021)
std1.printname()

print(std1.gradyear) # 2021