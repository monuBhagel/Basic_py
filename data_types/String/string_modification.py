# python has as many as 40 built-in string methods

name = "---bruce--banner---"
# name = "bruece banner"


# capatilize method
'''the first letter of string will converted to upper case.'''
print(name.capitalize()) # when name is   name = "bruece banner  capatilize method will turn it into this -> Bruece banner

# upper case
'''this convertes the string into upper case'''
print(name.upper()) # ---BRUCE--BANNER---

# lower case
'''this convertes the string into lower case''' 
print(name.lower()) # ---bruce--banner---

# Remove Whitespace/blankspace or strip method
''' this will remove the whitespace/blankspace from the string. '''

post = "  avengers  "
print(post)
print(post.strip()) # result would be "avengers" .  The default arg of strip is whitespace ,  but you can pass characters to remove from the string.

print(name) # ---bruce--banner---
print(name.strip("-"))  #  bruce--banner. This will remove "-" from the start and the end but not in between the string.


# Replace String
'''this will replace the string with the given string.'''
print(f"post is {post}") # post is   avengers

print(f"post is {post.replace('avengers', 'hulk')}") # post is   hulk 


# Split String
''' this will split the string into a list of strings.
    this will return a list of strings.
'''
fruits = "apple, banana , cherry, watermelon"

fruits_list = fruits.split(',') 

print(fruits_list) # ['apple', ' banana ', ' cherry', ' watermelon']

# string concatenation

first_name = "tony"
last_name = "stark"

full_name = first_name + last_name

print(f"first name is : {first_name}") # first name is : tony
print(f"last name is : {last_name}") # last name is : stark
print(f"full name is : {full_name}") # full name is : tonystark

print(first_name + " " + last_name) # tony stark

