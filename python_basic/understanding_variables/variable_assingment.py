# We know variables are used to store data , but how do we assign data to a variable ?

# In python,  we use the assignment operator (=) to assign values to a variable . or say make reference of the object to the variable .


'''Basic Assignment'''

x = 5
y = 3.14
z = "Hi"



'''Dynamic Typing'''
# python is dynamically typed , which means we can reassign variables to different data types . 

age = 25 # integer

age = "twenty five" # string



'''Multiple Assignments'''
# we can assign  values to multiple variables in a single line .

a = b = c = 100 

# here a =100 
# b = 100
# c = 100   although this type of assignment is not recommeded as it makes the code less readable .



'''Assigning Different Values to Multiple Variables'''
# we can assign different values to multiple variables in a single line .

k , l , m = 10 , 20.54 , "hello world"

#here k = 10
# l = 20.54
# m = "hello world"


'''Unpack a Collection of Values'''
# we can assign values stored in an iterable (tuple, list,etc) to multiple vaiables in a single line .

fruits  = ["apple" , "banana" , "cherry"]

e , f , g = fruits

print(e) # apple
print(f) # banana
print(g) # cherry