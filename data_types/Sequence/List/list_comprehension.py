# List comprehension offers a shorter syntax when you want to loop through tha list with some condition.

'''
Example:
Based on a list of fruits, we want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension we will have to write a for statement with a conditional test inside:
'''
fruits = ['apple' , 'banana', 'cherry' , 'mango']

fruits_with_a = [] # initialize empty list

for fruit in fruits:
    if 'a' in fruit:
        fruits_with_a.append(fruit)
        
print(fruits_with_a)

# With list comprehension we can do all that with only one line of code:
print("\nlist comprehension :")
new_list =[x for x in fruits if "a" in x]


print(new_list)

'''
Note: this is the syntax 
        newlist = [expression for item in iterable if condition == True]
        
-  
'''
# without if statement or coditional statement

list_1 = [x for x in range(1,100)]
# print(list_1)

# with if statement or coditional statement

list_2 = [x for x in range(1,100) if x % 2 == 0]
print(list_2)

'''
Expression : 
The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
'''
name = ['ram','sham','gunsham','mohan','sam','evil']

new_name =[nam.upper() for nam in name if 'a' in nam]
print(new_name)