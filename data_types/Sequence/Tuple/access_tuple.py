'''
In python tuples can be accessed using various ways :

1.using index
2.using negative index
3.using range of index

'''
# creating tuple 

tuple_example = ('mango', 'banana', 'papaya','cherry',
                 1,2,3,4,
                 True,False)

# accessing 2 , 4 and 8 item through index
item_2 = tuple_example[1]
item_4 = tuple_example[3]
item_8 = tuple_example[7]

print(f"item 2 is {item_2}")
print(f"item 4 is {item_4}")
print(f"item 8 is {item_8}")

# accesing last, third last and first item using neagtive index 

last_item = tuple_example[-1]
third_last_item = tuple_example[-3]
first_item = tuple_example[-len(tuple_example)]

print(f"last item is {last_item}")
print(f"third last item is {third_last_item}")
print(f"first item is {first_item}")


# accessing  through Range of Indexes :

'''access from item 2 to 5(included) through +ve and -ve indexing'''

item_2_to_5 = tuple_example[1:5]
print(f"through +ve indexing : {item_2_to_5}")

item_2_to_5_neg = tuple_example[-9:-5]
print(f"through -ve indexing : {item_2_to_5_neg}")


# Check if Item Exists

''' 
Our tuple contains multiple datatypes so normal membership operation might return error . 
'''
contains_a = 'a' in tuple_example
print(contains_a) # gives false why

'''The reason why contains_a = 'a' in tuple_example gives False is that the in operator is checking if the exact element 'a' exists in the tuple tuple_example, not whether 'a' is a character in any of the elements of the tuple. '''


contains_a = any('a' in str(item) for item in tuple_example) # if we don't do type converson of tuple's item this error will popup argument of type 'int' is not iterable
print(contains_a)

'''
- any() checks if at least one element of the tuple contains 'a'.
- str(item) ensures that we check each element as a string, even if it's not a string (like the integers 1, 2, etc.).
- 'a' in str(item) checks if the letter 'a' is in the string representation of each tuple element.
- This will return True because there are several strings in the tuple ('mango', 'banana', 'papaya', and 'cherry') that contain the letter 'a'
'''

# the simpler version of above code :

#1. using for loop

result = False 
for item in tuple_example:
    if 'a' in str(item):
        result = True
        break
    else:
        print("we didn't find any a in tuple")
        
print(f"present 'a' : {result}")


# 2. Using filter() and any():

filtered = any(filter(lambda item: 'a' in str(item),tuple_example))
print(f"present 'a' : {filtered}")


# 3. Using list comprehension:

present_a = any(['a' in str(item) for item in tuple_example])
print(f"present 'a' : {present_a}")

 