# List in pyhton is one of 4 the built-in data types , used to store collection of data 

'''
- list are used to store multiple items in a single variable.
- list are created or decleared using a square bracket [] .
- list items or values are "mutable , indexed and allow duplicate values".
- when we say list are ordered or index it means , if you add new items to a list, the new items will be placed at the end of the list.

- we can find the list's length using .len()
- list can be of any single data-type or a collection of multiple data-types.
- type() can be used to identify the type of a variabel if it is list then this will be the return value <class 'list'>

- There are two possible ways of creating a list 
    1. using square brackets []
    2. using list() method
'''

# empty list creation

empty_list = []
print(type(empty_list))

using_list_method = list() # if no argument is give the costructor will creates a new empty list.

print(type(using_list_method))

# list with items

fruits = ['apple', 'banana', 'cherry', 'watermelon']

print(fruits)

fruit_1 = fruits[0]

print(fruit_1)

# length of list
print(f"length of empty list : \n {len(empty_list)}")
print(f"length of fruits : \n {len(fruits)}")