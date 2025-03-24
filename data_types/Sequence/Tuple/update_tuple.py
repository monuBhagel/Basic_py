'''
We known from start that tuples are immutable .
but there are other ways to modify tuple.
such as:
    1. converting tuple into list  - the best way
    2. add one tuple into another.
'''

# inital tuple
numbers = (1,2,3,4,5)
print(type(numbers))

'''
- we can not directly add, append , extend or remove items from tuple,
- but we can do so by converting it into a list.
'''

# converting tuple into list

numbers_list = list(numbers)
print(type(numbers_list))

# modifying 

numbers_list.append(8)
print(numbers_list)
numbers_list.insert(3,'banana')
print(numbers_list)
numbers_list.remove(3)
print(numbers_list)

# now change it back if needed.

numbers = tuple(numbers_list)
print(f"numbers is {numbers}\ntype of it : {type(numbers)}")

# we can add one tuple into another 

tup_1 = (1,2,3,4)
print(tup_1)
tup_2 = ('a','b','c','d')
print(tup_2)

tup_1 += tup_2

print(tup_1)

'''
lastly we can remove the tuple completely using del 
'''
del numbers
# print(numbers)
# the result -> NameError: name 'numbers' is not defined. Did you forget to import 'numbers'?