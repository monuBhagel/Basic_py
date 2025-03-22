'''
- in python we cannot just copy a list into other list like this:
        list_2 = list_1
  because this will only copy the reference to the list_1 , so in future any changes made to list_1 will automatically reflected in list_2.

- to avoid such problem python provides us some method to copy 
    1.copy()
    2.list()
    3.slice()
'''

# Use the copy() method

list_1 = list(range(1,20))
print(f"list 1 is : {list_1}")

list_2 = list_1.copy()

print(f"list 3 is : {list_2}")

# check is both list are same
print(list_1 == list_2)


# Use the list() method

list_3 = list(list_1)
print(f"list 3 is : {list_3}")


# Use the slice Operator

list_4 = list_1[:]
print(f"list 4 is : {list_4}")

'''
Note: we can use these 
    copy() , list() , slice operator for copying because these operation return a list as a result.
'''