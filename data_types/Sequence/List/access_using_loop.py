# we can access list elements one by one through loops

# original list
fruits = ['apple' , 'banana', 'cherry' , 'mango']

# using for loop
'''
prints all the elemnts one by one.
'''

for fruit in fruits:
    print(fruit)
    
# Loop Through the Index Numbers
'''
we can also loop through the list by it index number.
using range() and len() method.
'''
for i in range(len(fruits)):
    print(f"index = {i} and item is {fruits[i]}")
    
# Using a While Loop
'''
we can use while loop for accessing the list if we known the length of list.
'''
i = 0 
while i < len(fruits):
    print(fruits[i])
    i+=1
    
# Looping Using List Comprehension
'''
- List Comprehension offers the shortest syntax for looping through lists:
- A short hand for loop that will print all items in a list:
'''
print("list comprehension : ")
[print(x) for x in fruits]