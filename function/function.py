'''
- a function is a block of code that only runs when it is called.
- we can pass data as arguments into a function.
- Also a function can return data as a result .
- To create a function :-
    - A function is defined using the "def" keyword.
        ->   def function_name(parameters 'optional') :
                -> function body/block

- To call a function :-
    - A function is called by using the function name followed by parentheses.

- Information can be passed into functions as arguments.
    - Arguments are specified after the function name, inside the parentheses. - You can add as many arguments as you want, just separate them with a comma. 

- By default , a function takes positional arguments. 

- for arguments we can use :
    - default args
    - keyword args  aka kwargs
    - positional args 
    - arbitrary args  aka *args
    - keyword arbitrary args aka **kwargs
'''

# creating a function :

def greet():
    print("Hello world !")
    
# calling a function :

# greet()


# fucntion with args :

def greet(name):
    print(f"hello {name} ")
    
#  calling the function with args:

greet("sam")

greet("ram") # we call a function as many times we want .


#  function with multiple args :

def info(name, age):
    print(f"name is {name} and age is {age}")
    
# calling function with multiple args :

info("sam", 23)  # this is a function with positional args 

info(23, "sam") 
'''
-  the main concept of positional args is that the order of the arguments matters. 
- the first args is assigned to the first parameter and the second args is assigned to the second parameter and so on.
-  if we change the order of the args then the output will also change.

  -  in the info(23, "sam") code output don't make sense . but it dosn't give any error . which is wrong .
  
- to overcome such problem we can use keyword args.
'''

# keyword args :
'''
- the keyword args are written in the form of "Key = value" pair.
-  the keyword args are the args that are passed to the function by using the name of the parameter.

- here the order doesn't matter. we can pass the args in any order.
'''

def info(name , age):
    print(f"name is {name} and age is {age}")
    
# calling the function with keyword args :
info(name = "sam" , age = 23 )

info(age = 23 , name = "sam")



# default args :
'''
-  we can pass default args to the function. 
- this is usefull when we want to pass a default value to the function if the user doesn't pass any value.
'''

def greet(name = "user_name"):
    print(f"hello {name}")
    
# calling the function with default args :

greet()  # hello user_name . this is what we get when we dont pass any value

greet("mohan") # hello mohan .  this is what we get when we  pass  value



#  Arbitrary arguments :
'''
- when we don't known how many args we will pass to the function then we can use arbitrary args . 
- to use this : in the function definition we use a * asterisk before the parameter name.

- This way the function will receive a tuple of arguments, and can access the items accordingly:
'''

def childer(*names):
    print(f"the name of child 1 is {names[0]}") # {names[0]} this allow us to acces the first child name
    
childer("ram", "shyam" , "mohan")


# Arbitrary Keyword Arguments, **kwargs :
'''
- when we don't known how many kwargs we will pass to the function then we can use arbitrary args .

-  to use this in the function definition we use a ** double asterisk before the parameter name .
'''

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


# Positional-Only Arguments
'''
- we can specify that a function can have ONLY positional arguments,
- To specify that a function can have only positional arguments, add ", /" after the arguments:
'''

def my_function(x, /):
  print(x)

my_function(3)


# Keyword-Only Arguments
'''
- To specify that a function can have only keyword arguments, add *, before the arguments:
'''

def my_function(*, x):
  print(x)

my_function(x = 3)