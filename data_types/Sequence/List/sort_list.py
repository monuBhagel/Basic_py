# List objects have a sort() method that will sort the list alphanumerically, in ascending order, by default:

# - By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

# Example :

fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits.sort()
print(fruits)



numbers = [4,7,2,12,9,2,1,0]
numbers.sort()
print(numbers)

# Sort Descending
'''
use keyword argument "reverse = true"
'''
fruits.sort(reverse=True)
numbers.sort(reverse=True)

print(fruits)
print(numbers)

# Customize Sort Function
'''
we can customize sort function by using the keyword argument
"key = function_name"
'''

# Example
# Sort the list based on how close the number is to 50:

list_3 = [100, 50, 65, 82, 23]

def myfunc(n):
  return abs(n - 50)

list_3.sort(key= myfunc)

print(list_3)

# Case Insensitive Sort
'''
Case sensitive sorting can give an unexpected result:
    So if you want a case-insensitive sort function, use str.lower as a key function:
'''

fruits_case_sensitive = ["banana", "Orange", "Kiwi", "cherry"]
fruits_case_sensitive.sort()
print(fruits_case_sensitive)

fruits_case_sensitive.sort(key= str.lower)
print(fruits_case_sensitive)


# Reverse Order
# fruits_case_sensitive.sort(reverse=True , key= str.lower)
fruits_case_sensitive.reverse()
print(fruits_case_sensitive)