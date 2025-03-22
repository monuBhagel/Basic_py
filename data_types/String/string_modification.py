# python has as many as 40 built-in string methods

name = "---bruce--banner---"
# name = "bruece banner"


# capatilize method
'''the first letter of string will converted to upper case.'''
print(name.capitalize()) # when name is   name = "bruece banner  capatilize method will turn it into this -> Bruece banner

# upper case
'''this convertes the string into upper case'''
print(name.upper()) 

# lower case
'''this convertes the string into lower case''' 
print(name.lower())

# Remove Whitespace or strip method
''' this will remove the whitespace from the string. '''

post = "  avengers  "
print(post)
print(post.strip()) # the default arg of strip is whitespace ,  but you can pass characters to remove from the string.

print(name)
print(name.strip("-"))  # this will remove "-" from the start and the end but not in between the string.


# Replace String
'''this will replace the string with the given string.'''
print(f"post is {post}")

print(post.replace("avengers", "hulk")) 


# Split String
''' this will split the string into a list of strings.
    this will return a list of strings.
'''
fruits = "apple, banana , cherry, watermelon"

fruits_list = fruits.split(',') 

print(fruits_list)

# string concatenation

first_name = "tony"
last_name = "stark"

full_name = first_name + last_name

print(f"first name is : {first_name}")
print(f"last name is : {last_name}")
print(f"full name is : {full_name}")

print(first_name + " " + last_name)

