'''
- control statements are used on decision making process :
- these are as follow :
    1. if statement
    2. elif statement
    3. else statement
    4. Switch statement
    5. short hand if else or ternary
    
- Python supports the usual logical conditions from mathematics:

    - Equals: a == b
    - Not Equals: a != b
    - Less than: a < b
    - Less than or equal to: a <= b
    - Greater than: a > b
    - Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.


'''

a = 5 
b = 10 

# simple if statement 

if a < b :
    print(a)
    
# if statement with else block

if a > b :
    print(a)
else :
    print(b)
    
# if statement with elif block

if a == 6:
    print(a)
elif a < b :
    print("in elif")
    
# if -elif-else statement
print("if -elif-else statement")
if a == 7:
    print("in if")
elif a > b:
    print("in elif")   
else :
    print("in else")
   
    
# short hand if 
'''
If you have only one statement to execute, you can put it on the same line as the if statement.
syntax :  if expression : statement
'''
if a < b : print("a is samller than b")

# short hand if - else 
'''
If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
syntax ->
        statement_when_true if condition else statement_when_false

This technique is known as Ternary Operators, or Conditional Expressions.
'''

# print("in if ") if a < b else print("in else") 

print("in if ") if a > b else print("in else") 


# Nested if 
'''
You can have if statements inside if statements, this is called nested if statements.
'''

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
    
    
# the pass statement
'''
if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
'''

if a > b :
    pass