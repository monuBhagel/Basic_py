'''
There are several ways to join, or concatenate, two or more lists in Python.
    1. using + operator
    2. using append()
    3. using extend()
'''

list_1 = list(range(1,10))
list_2 = list(range(10,20))

list_joined = list_1 + list_2

print(list_joined)


# Another way to join two lists is by appending all the items from list2 into list1, one by one:

'''for i in list_2:
    list_1.append(i)
    
print(list_1)'''

# using extend

print(list_1)

list_1.extend(list_2)

print(list_1)
