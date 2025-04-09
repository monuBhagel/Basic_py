'''
- Exception handling in Python is a way of dealing with errors that occur during program execution, ensuring that the program continues running smoothly even when unexpected issues arise.

-  Python provides a powerful mechanism for handling exceptions using try, except, else, and finally blocks.

- Key Components of Exception Handling :
    1. try block :
        - This is where we put the code that might cause an exception.
        - If no exception occurs, the program continues executing after the try block.
    
    2. except block :
        - This block is executed if an exception occurs in the try block.
        - You can specify the type of exception you want to handle, and optionally capture the exception object.
    
    3. else block :
        - This block is optional. It runs if no exception occurs in the try block.
        
    4. finally block :
        - This block is optional but is useful when you need to ensure that some code runs regardless of whether an exception was raised or not.
        - It's often used for cleanup tasks like closing files, releasing resources, etc.
'''
# syntax :
try:
    # Code that might raise an exception
    pass
except SomeException as e:
    # Code that handles the exception
    pass
else:
    # Code to execute if no exception occurs
    pass
finally:
    # Code to execute regardless of whether an exception occurs or not
    pass




# 1.  try block :

try :
    x = 10/2
except ZeroDivisionError :
    print('can not divide by zero')


# 2 .  except block :
try:
    x = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}") #Error: division by zero
    

# 3. else block :
try:
    x = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Division was successful!")
    # Division was successful! printed if no error happens.


# 4. finally block :
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


# Catching Multiple Exceptions :
'''
- we can catch multiple exceptions by specifying more than one except block, or by combining exceptions in a tuple.
'''
try:
    # Some code that could raise multiple exceptions
    y = int("abc")
    x = 10 / 0
except (ZeroDivisionError, ValueError) as e:
    print(f"Caught an error: {e}")


# Catching Generic Exceptions :
try:
    x = 10 / 0
except Exception as e:  # Catching all exceptions
    print(f"An error occurred: {e}") # An error occurred: division by zero



# Raising Exceptions :
'''
- we can raise manull exception using the keyword "raise"
'''

def check_age(age):
    if age < 18:
        # raise exceptionName(output statement.)
        raise ValueError("Age must be 18 or older.")
    return "Age is valid."

try:
    check_age(15)
except ValueError as e:
    print(f"Error: {e}")



# Exception Chaining (Python 3.x)
'''
- In Python 3.x, we can chain exceptions using the from keyword. This allows you to raise a new exception while preserving the context of the original exception.
'''

try:
    x = int("abc")
except ValueError as e:
    raise TypeError("A type error occurred.") from e