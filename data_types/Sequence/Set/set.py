'''
- Sets in python , are used to store multiple items in a single variable.
- A set is a collection that is unordered, mutable, and unindexed."
    - note that : a set is mutable but the set items must be immutable.
- Hashable Elements: Elements of a set must be hashable. This means they need to be immutable types, like numbers, strings, or tuples. 
- * Lists or dictionaries, which are mutable, cannot be added to sets.

- Set Items :
    - Set items are unordered, unchangeable(immutable), and do not allow duplicate values.
    - Set items are unchangeable(immutable), but you can remove items and add new items.
    - Set items can appear in a different order every time you use them, and cannot be referred to by index or key. this is why they are called unordered.
    - set can not have duplicates .
        -  The values True and 1 are considered the same value in sets, and are treated as duplicates:
        - The values False and 0 are considered the same value in sets, and are treated as duplicates:
        
- The Set is created and declared using round brackets
    - there are two ways to do this :
        1. using paranthesis {} 
        2. using set constructor

- can see the type using type()
- can see the length using len()

'''

# creating set 

# 1. using round bracket : 

fruits = {"mango" ,"banana","cherry", "tomato", "avocado" }

print(fruits)

# 2. using set constructor :

set_example = set(("hello" , "world" ,0,1,2,3 , True , False ))
print(set_example)

# size and type : 
print(len(set_example))
print(type(set_example))

# accessing item of set :
#   1. using for loop:

for fruit in fruits:
    print(fruit)
    
# 2.Using for loop with enumerate: we can use enumerators when we want to access the index with the values .

for index , value in enumerate(set_example):
    print(f"Index {index} has value {value}")
    
# Check if  value/ item exist 

if "cherry" in fruit:
    print("cherry exist")
else:
    print("cherry not exist")

