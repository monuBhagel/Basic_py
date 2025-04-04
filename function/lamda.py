'''
- A lambda function is a small anonymous function.
- it can take any number of args but can have only one expression.

- syntax :
    lambda arguments : expression
    
- the expression is executed and the result is returned.

'''

x = lambda a : a+10

print(x(3)) # 13

# we can use lambda with filter , map , reduce also