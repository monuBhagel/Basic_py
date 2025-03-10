# Output formatting in Python with various techniques including the format()
# method, manipulation of the sep and end parameters, f-strings and the 
# versatile % operator. These methods enable precise control over how data is 
# displayed, enhancing the readability and effectiveness of your Python programs.

'''--------------------------------------------------------------------------'''
#  Using Format()

name = 'sonu'

print('name of student is {}'.format(name))

'''--------------------------------------------------------------------------'''

#  Using sep and end parameter

# By default end = newline

print("Python", end='@')
print("is awesome")


# Seprating with Comma
print('h','e','l','l','o', sep='__')

# for formatting a date
print('09', '12', '2016', sep='-')

'''--------------------------------------------------------------------------'''

# Using f-string

name = 'sonu'
standard = 12

print(f'hello, my name is {name} and i study in {standard}th class. ')

'''--------------------------------------------------------------------------'''

#  Using % Operator

# We can use ‘%’ operator. % values are replaced with zero or more value of 
# elements. The formatting using % is similar to that of ‘printf’ in the C 
# programming language.

# %d –integer
# %f – float
# %s – string
# %x –hexadecimal
# %o – octal

num = 8

add = num + 10

print('number after sum is %d' %add)


'''--------------------------------------------------------------------------'''