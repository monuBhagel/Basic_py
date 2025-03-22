# Change List Items
'''
- Change or Modify list items :
    > we can change or modify list through various way such as:
        1. using indexing .
        2. using append.
        3. using insert.
        4. usign remove.
        5. using pop.
        6. using extend.
        7. using sort.
        8. using reverse.
        and many more.
'''

# creating inital  list

fruits = ['apple' , 'banana', 'cherry' , 'mango']

print(f"list initial state : \n {fruits}")
print(f"list initial size : {len(fruits)}")

# changing item value using indexing

fruits[1] = 'kela'
print('list changed :')
print(fruits)

# Change a Range of Item Values

fruits[1:4] = ['watermelon','kiwi','tomato']
print('list changed :')
print(fruits)
print(f"list  size : {len(fruits)}")


'''Note: The length of the list will change when the number of items inserted does not match the number of items replaced .
it is true for both the cases when inserted items size is greater than original and also for when it is less than original.'''


fruits[1:4] = ['watermelon','kiwi','tomato','guava']
print('list changed :')
print(fruits)
print(f"list  size : {len(fruits)}")

# original list
fruits = ['apple' , 'banana', 'cherry' , 'mango']


# using insert 
'''
- insert is used to add item at certain index in the list.
- insert method take 2 parameters first : index and second : item to be inserted.
'''

fruits.insert(2,'watermelon') 
print("watermelon inserted")
print(fruits)
print(f"list  size : {len(fruits)}")

# using append
'''
- append method is used to insert an item in the end of the list. 
- it takes item/value as input.
'''

print(f"list before append is used :\n{fruits}")

fruits.append('tomato')
print(f"list after append is used :\n{fruits}")

# using extend
'''
- extend is used to insert items at once .
- this appends elements from other iterable into the list.
'''
print(f"list before extend is used :\n{fruits}")
fruits.extend([1,2,3,4,4])
print(f"list after extend is used :\n{fruits}")


# using remove
'''
- the remove method remove the specified item from the list .
- if there are more than one specified item in the list the remove will eleminate the first occurance.
- the remove method do not provide you the removed item , it just clear it from the list.
'''
print(f"list before remove is used :\n{fruits}")
# removed_fruit = fruits.remove('banana')
# print(f"list after remove is used :\n{removed_fruit}")
fruits.remove('banana')
print(f"list after remove is used :\n{fruits}")

fruits.remove(4)
print(f"list after remove is used :\n{fruits}")


# Remove Specified Index
'''
- we can do that using 2 method :
    1. pop
    2. del
'''

# 1. pop 
'''
- the pop method return the item from the list 
- also it can be used for removing item from the end if we don't specify the index.
'''
print(f"list before pop is used :\n{fruits}")
poped_item = fruits.pop(4)
print(f"poped item from list :\n{poped_item}")


# 2. del
'''
- del is used to pop item from ths list .
- it can also be used to clear the list completely.
'''
print(f"list before del with index is used :\n{fruits}")
del_item = fruits.pop(2)
print(f"del item from list :\n{del_item}")


# Clear the List
'''
- clear method is used to clear the list
'''
print(f"list before clear is used :\n{fruits}")
fruits.clear()
print(f"list after clear is used :\n{fruits}")
