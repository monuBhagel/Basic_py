'''
- Loops in python are used to repeat some things when some condition is true.
- In python , there are primarily  two types of loops: . These are :
        1. for loop
        2. while loop
        
- The for loop in Python is used to iterate over a sequence (like a list, tuple, dictionary, string, or range). it is used when we knonw how many time we need repeatation.

- The while loop is used to execute a block of code as long as a specified condition is True.

- Loop Control Statements : break , continue , else .
    they are used to control the normal flow of loop.
'''

numbers = list(range(1,10)) # list of numbers
print(numbers)

# simple for loop :

for n in numbers:
    print(n )
    
#  for with range()

for n in range(1,5): # 1 is inclusive and 5 is exclusive
    print(n )
    
# simple while loop

i = 1
while i < len(numbers):
    print(i )
    i +=1
    
# looping through string:

for x in "banana":
    print(x , end=" , ")
       
print( ) # to nulify the end=

# Loop Control Statements : 

# break  : used to break out of the loop even when it is true.

for i in range(10):
    if i == 5:
        break  # Exits the loop when i is 5
    print(i)
    
# continue: Skips the current iteration and moves to the next one.

for i in range(10):
    if i == 5:
        continue  # skip the loop when i is 5 and print next number
    print(i)
    
# else in loops:
'''
- The else block can be used with both for and while loops. The code inside the else block will execute when the loop completes normally (i.e., without a break).
'''
for i in range(5):
    print(i)
    # break
else:
    print("Loop finished without a break.")
    
    
# nested for loop

for x in range(1,3):
    for y in range(1,3):
        print(f"{x} {y}")