# By default , input() function store the input in the String format.
# But we change the type by type casting the input function

num = input("enter a number :")

print(type(num)) # this give <class 'str'>

num_1 = int(input('enter a number again :'))

print(type(num_1)) # this gives <class 'int'>

num_2 = float(input('enter a number again :'))

print(type(num_2)) # this gives <class 'float'>


num_3 = bool(input('enter a number again :'))

print(type(num_3)) # this gives <class 'bool'>


list_1 = ['apple', 'banana', 'cherry']

print(type(list_1)) # <class 'list'>

list_2 = tuple(list_1)

print(type(list_2))  # <class 'tuple'>