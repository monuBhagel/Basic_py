# string fomatting in python is usefull function of python language

'''for example:
    name = "john"
    age = 14
    so if we print it like this:
    print("my name is " + name + " and age is " + age)
    
   this will retun a error:
 print("my name is " + name + " and age is " + age)
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
TypeError: can only concatenate str (not "int") to str
'''

# to overcome such things we can use f-string and Placeholders and Modifiers.

# f-string
name = "sam"
age = 20 
print("this is f-string example.")
print(f"my name is {name} and age is {age}")

# palceholders

print("this is placeholders example.")
print("my name is {n} and age is {a}".format(n=name , a= age))

# modifiers
print("this is modifiers example.")
print("my name is {n} and age is {a:.2f}".format(n=name , a= age))
    