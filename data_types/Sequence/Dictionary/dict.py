'''
- A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
 { As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered. }
 
- Key Characteristics of a Dictionary: 
    - Ordered : In Python 3.6+, dictionaries maintain insertion order, meaning the order of keys is preserved as they are added to the dictionary. 
    - Mutable : You can add, modify, and remove key-value pairs after the dictionary is created.
    
    - Key-value pair : A dictionary consists of pairs where each key maps to a corresponding value. Keys must be immutable (e.g., strings, numbers, tuples) and unique. Values can be of any data type, and they can be duplicated.
    
    - Efficient lookups : Dictionaries are implemented using hash tables, making lookups, inserts, and deletions generally very fast, with an average time complexity of O(1).
    
    - NO indexing : You cannot access dictionary items using an index (like lists or tuples). Instead, you use the keys to access the values.
    
- Python has a set of built-in methods that you can use on dictionaries. 

    - clear()	: Removes all the elements from the dictionary
    - copy()	: Returns a copy of the dictionary
    - fromkeys()	Returns a dictionary with the specified keys and value
    - get()	 : Returns the value of the specified key
    - items()	: Returns a list containing a tuple for each key value pair
    - keys()	: Returns a list containing the dictionary's keys
    - pop() :	Removes the element with the specified key
    - popitem() : 	Removes the last inserted key-value pair and return it
    - setdefault()	Returns the value of the specified key. If the key does not
                    exist: insert the key, with the specified value 
    - update()	: Updates the dictionary with the specified key-value pairs
    - values()	: Returns a list of all the values in the dictionary
    
- we can create dictinory using: 
    1.Using curly braces
    2.Using the dict() constructor
'''

# creating a dict

car = {
    "brand" : "Ford",
    "model"  : "Mustang" , 
    "year" : 1964
}

print(car)

# checking size or say how many key-value pair are in the dict:

print(len(car))


# accessing dict :
'''
- we can do that using [object key] or using get(object key) method 
'''
print(car["brand"])

print(car.get('brand'))

# accessing all key , value and then all the key-value pair:

keys = car.keys()
print(keys)

value = car.values()
print(value)

key_value = car.items()
print(key_value)

# Check if Key Exists
if "brand" in car:
    print(f"yes brand exist : {car['brand']}")
    

# update or add new key-value pair:
'''
- we can do that by :
    using dict["key"] = "value"
    or
    dict.update({ "key" , "value" }) # update method replaces the old key value if it exist.
'''

car["color"] = "red"
print(car)

car.update({"color" : ["red","blue","yellow"]})
print(car)


# remove item from dict 
''' 
- we can do that using :
    1. del dict["key"]  this removes the specified item
            or
        del dict  : this removes  the whole dict
    
    2. pop("key")
    3. popitem() this remove the last inserted item
    4. clear() this clear the dict
'''

del car["model"]
print(car)

car.pop("brand")
print(car)

car.popitem()
print(car)

car.clear()
print(car)


