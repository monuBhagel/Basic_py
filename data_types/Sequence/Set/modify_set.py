'''
- You can modify a set by adding or removing elements after it has been created. For example, you can use methods like add(), remove(), or discard() to modify a set.

- However, elements within a set must be immutable. This means you cannot add mutable objects like lists or dictionaries to a set, but you can modify the set itself.

- Common method used on set :
   - to add item/s
        - add()
        - update()
   - to remove item/s
        - remove()
        - discard()
        - clear()
        - pop()

- set opertaions :
    1. union()  or |
    2. update()
    3. intersection() or &
    4. difference() or -
    5. symmetric_difference() or ^

- The union() method returns a new set with all items from both sets.
    can use the | operator instead of the union() method. but it will only take sets as input.
    
- The update() method inserts all items from one set into another.   
    The update() changes the original set, and does not return a new set.
    
- The intersection() method will return a new set, that only contains the items that are present in both sets.
    The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.
    
- The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

- The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
    
- The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.

- The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
'''

set_1 = {1,2,3}
set_2 = {"a", "b" , "c"}

# union : return a new set

union_set = set_1.union(set_2)

print(union_set)

union_by_pipe = set_1 | set_2
print(union_by_pipe)

# Join a Set and a Tuple

tuple_1 = ("hello" ,"world")

set_union_tupel  = set_1.union(set_2 , tuple_1)

print(set_union_tupel)


# upadte : this change the original set and not return a set.

print(f"set_1 before update : {set_1}")

set_1.update(set_2) # can also use other sequence in bracket.

print(f"set_1 after update : {set_1}")


# intersection or & : this return a new set

in_set_1 = {'h','e','l','l','o'}

in_set_2 = {'b','y','e'}

in_set_3 = in_set_1 & in_set_2  # common item is "e"

print(in_set_3)

in_set_4 = in_set_1.intersection(in_set_2)

print(in_set_3)

#  intersection_update() : this will change the original set :

print(f"in_set_1 before intersection update : {in_set_1}")

in_set_1.intersection_update(in_set_2)

print(f"in_set_1 after intersection update : {in_set_1}")


# difference : this return a new set : 

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(f"difference btw set1 and set2 : {set3}")

set4 = set1 - set2
print(set4)

# difference update changes the original set :

print(f"set1 before difference update with set2 : {set1}")

set1.difference_update(set2)

print(f"set1 after difference update with set2 : {set1}")



# symmetric difference : return a new set
# method will keep only the elements that are NOT present in both sets

fruits = {"apple", "banana", "cherry"}
company = {"google", "microsoft", "apple"}

set_syd = fruits.symmetric_difference(company)

print(f"symmetric difference : {set_syd}")

# symmetric difference update : this changes the original set:

print(f"fruiits before symmetric difference update with company : {fruits}")

fruits.symmetric_difference_update(company)

print(f"fruiits after symmetric difference update with company : {fruits}")