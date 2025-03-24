'''
In python tuple is one of the 4 data-types which is used to store collection of data in one variable.

- Tuple is a collection which is "Ordered and Immutable" in nature.
- tuples are declared using round bracket "()".
- tuple is ordered , immutable and allows duplicate values.

Question : what is meant by ordered , immutable and allow duplicates ?

Answer :
> Ordered , it means items in tuple are indexed i.e every item in tuple  have an index attached with it .
> Immutable , it means once created we cannot change the values of it or say we cannot modify tuple after creation. we can only access it
> Allow duplicates , as items in tuple are index so complier have no problem in uniquly indentifying the items.

- there are two ways of creating a tuple.
    1. using round bracket 
    2. using tuple method

- just like list tuple can also store multiple data-types at once.
'''

# creating a tuple
empty_tuple = ()
print(type(empty_tuple))

empty_tuple_2 = tuple()
print(type(empty_tuple_2))

# creating tuple with items
tuple_example = ('mango', 'banana', 'papaya','cherry',1,2,3,4,True,False)

print(tuple_example)

# accessing tuple through index

print(tuple_example[2])
print(tuple_example[2:6])
print(tuple_example[-1])

# checking length of tuple

print(len(tuple_example))


# trying to modify tuple

# tuple_example.add('hello')
#AttributeError: 'tuple' object has no attribute 'add'