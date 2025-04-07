'''
- Iterators in python are objects which can be iterated upon , it means that we can traverse through all the values . 
- An iterator is an object which implements the iterator protocol , such as __iter__() and __next__() methods.

- Iterabels are lists, tuples, dictionaries , sets , Strigns , etc can be iterated over.

- syntax to create an iterator object .
    iter_obj_name = iter(iterable)
'''

numbers = list(range(1, 10))

# creating an iterable object

iter_obj = iter(numbers) # object created.

print(numbers)
print(iter_obj)

# using next() method to iterate through the iterator object.
try:
    print(next(iter_obj)) # 1
    print(next(iter_obj)) # 2
    print(next(iter_obj)) # 3
    print(next(iter_obj)) # 4
    print(next(iter_obj)) # 5
    print(next(iter_obj)) # 6
    print(next(iter_obj)) # 7
    print(next(iter_obj)) # 8
    print(next(iter_obj)) # 9
    print(next(iter_obj)) # 10 -> raises StopIteration error.

except StopIteration:
    print("no more item to iterate. Reached end !!")
    
    
# experiment

class Numbers:
  def __iter__(self):
    self.a = 0
    return self

  def __next__(self):
      try:
        if self.a < 10 :
          x = self.a
          self.a +=2
          return x
      except StopIteration:
          print("no more item to iterate. Reached end !!")
     

myclass = Numbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))