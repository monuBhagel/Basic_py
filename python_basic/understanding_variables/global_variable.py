# python offer scope of variable to work within
# this mean in python variable are block level scoped that is variable outside (GLOBAL VARIABLE) the block of a function is different the variable inside (LOCAL VARIABLE)

#LOCAL VARIABEL

'''these type of variable have the scope or limit of functioning within certain area called block or scope of that variable

Example :-
            Variable within the function or condition statement [if , if-else , switch , try-expect block etc are called the LOCAL variable ]'''
            
'''def myfunc():
  x
  x = "fantastic"

myfunc()

print("Python is " + x)'''

#the above code result in an error specifically UnboundLocalError
# UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
# this is because the variable x is decleared inside the myfunc() which make the var "x" a local variable 

# the above code can corrected as this 
def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc() # result as python is fantastic

# GLOBAL VARIABLE

# Variables that are created outside of a function  are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.'

x = "awesome" #golbal variable

def myfunc():
  print("Python is " + x)

myfunc() #result as python is awesome


# If we create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
# The global variable with the same name will remain as it was, global and with the original value.

y = "awesome" #golbal variable 

def myfunc():
  y = "fantastic" #local variable 
  print("Python is " + y) #prints local var

myfunc()

print("Python is " + y) # prints global var


# The global Keyword

# we can use and even declared global variable inside the block using global keyword

#examle :-

def myfunc():
  global a # gloabl variable declared
  a = "fantastic"

myfunc()

print("Python is " + a)