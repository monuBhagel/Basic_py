# Boolean in python represent True or False .
# boolean is a subclass of int.

print(issubclass(bool, int))  # this return true.

'''Booelean are used in decision making and control structures and flow of program.
Boolean are used in conditional statements like if, while, for, etc.'''

# example :

a =10 
b =20

result  = "hello" if a>b else "bye bye"

print(result)

# the bool() function can be used to evaluate any value and return a true or false value.

'''Almost any value is evaluated to true if it has some sort of content in it.
any string is tre , but the empty one
any number is true , but not the number 0
any list, tuple, dic,set is true , but not the empty one.
'''

#example  of true values:
print(bool("hello"))
print(bool(15))
print(bool([1,2,3,4,4]))
print(bool((1,2,3,4,5,6)))
print(bool({"name" : "sam",
            "age" : 20}))

# example of false values:

print(bool(""))
print(bool())
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(0))