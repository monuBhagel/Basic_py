# The file contains the use of comments and indentation in pyhton .

# Comments in Python .
# the comment in python is denoted by '#' symbole.

"""for multi-line comment we use ''' ''' or """ """ i.e triple quotes
this is multi-line comment in python.
Also comments are not executed by python interpreter and are used for understanding the code / documentation and debugging purpose.
"""

# important note : when we use multi-line comments in python, we can use it for documentation purpose and it is called docstring. 
# the docstring can be used to define the purpose of the function, class, module ,etc. and can be accessed using __doc__ attribute.



# Python Indentation

# Indentation is very important in Python. It is used to define the level of nesting of code blocks.
# For example, in conditional statements and loops, indentation is used to define the scope of the code block.

if True:
    # This is an indented block
    print("This is indented")
    if True:
        # This is a nested indented block
        print("This is nested and indented")
