# Python divides the operators in the following groups:
'''
1. Arithmetic operators
2. Assignment operators
3. comparison operators
4. Logical operators
5. Identity operators
6. Membership operators
7. Bitwise operators
'''

# Python Arithmetic Operators 
'''these are used with nuerical values to perform common mathematical operations.'''

add = 10 + 5
sub = 10 - 5
mul = 10 * 5
div = 10 / 5
modules = 10 % 5
exponent = 10 ** 5
floor_division = 10 // 5 #the floor division // rounds the result down to the nearest whole number

print(add)
print(exponent)

# Python Assignment Operators
''' these are used to assign values to variables.
these are : = ,+= ,-+ ,*= ,/= ,%= ,//= ,**='''

x = 5

x += 3 # x = x +3
x -= 3 # x = x - 3
x *= 3 # x = x * 3
x /= 3 # x = x / 3
x %= 3 # x = x % 3
x //= 3 # x = x // 3
x **= 3 # x = x ** 3

# Python Comparison Operators
''' these are used to compare values and return a boolean value.
these are : == , != , > , < , >= , <='''

5 == 3 # equal operator
5 != 3 # not equal operator
5 > 3 # greater than operator
5 < 3 # less than operator
5 >= 3 #  greater than or equal to 
5 <= 3 # less than or equal to


# Python Logical Operators
''' these are used to combine conditional statements.
these are : and ,  or , not
and = return true if both statements are true esle false.
or = return true if one of the statements is true.
not = return false if the result is true and vice versa.'''

# example
x = 5
y = 7

AND = "true" if x == 5 and y > x else "not true"

OR  ="true" if x == 5 or y < x else "not true"

NOT = "true" if not(x == 5 and y > x) else "not true"

print(AND)
print(OR)
print(NOT)


# Python Identity Operators
'''these are used to compare the objects ,  not if the are equallls but to see if they are actually the same objects with same memory address.

these are : is , is not'''

# example
fruits = ["apple", "banana"]
fruits_2 = ["apple", "banana"]
print(fruits_2 is fruits)  # returns False because fruits_2 is not the same object as fruits, even if they have the same content
print(fruits_2 == fruits)



# Python Membership Operators
''' these are used to test if a sequence is presented in an object or not.
these are : in , not in'''

# example :
print(fruits)
print(f"is cherry present in fruits : {'cherry' in fruits}")


# Python Bitwise Operators
'''these are used to compare binary numbers.
these are : & , | , ~ , ^ , >> , << 
& = AND
| = OR
~ = NOT
^ = XOR
>> = Singed Right shift
<< = zero fill left shift'''

# example :
x = 5
y = 3 
binary_x = bin(x)[2:]
binary_y = bin(y)[2:]

print(binary_x.zfill(4))
print(binary_y.zfill(4))

print(x & y) # The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

print(x | y) # The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

print(~x ) # The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

print(x ^ y) # The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

print(x<<2) # The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

print(x>>2) # The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.