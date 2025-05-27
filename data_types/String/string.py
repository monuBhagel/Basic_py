''' String in python are immutable.
String in python are surrounded by either single qotes and double quotes.
python does not have a char type for single letter, so any single letter is a string of length 1.
'''

# string example.

name  = "sam willson" #double quotes
post = 'captain america' # single quotes

print(f"{name} is {post}")

# Quotes Inside Quotes
'''to put quotes inside quotes use the escape character "\" '''
print("before that he was known as \"falcon\" . ")

#or just use the quotes which is not used in the string i.e if string is in double quote use single quotes inside it.

print("he was the part of the team called 'avengers' . ")

# Assign String to a Variable

gretting = "hello"
print(gretting)

# multiline strings

avengers = '''iron man , falcon, captain america ,
hulk, thor , black widow and hawkeye.'''



# Strings are Arrays
'''strings in python are arrays of bytes representing unicode characters
square brackets can be used to access elements of the strings.'''

name = "tony stark"
#frist character
print(name[0])



# Looping Through a String
''' we can loop through a string using a loop as if its an array'''

for x in name :
    print(x)
    
# String Length

print(f"length of name is {len(name)}")


# Check String 
''' to check if certain phrase or character is present in the string we can use the 'in' keyword or say the membership operator.'''

if "tony" in name  : 
    print("tony is present.")
else :
    print("tony is not present.")
    

txt = "the best thing is python is just like english."

print("english" in txt) # this return boolean value 



# Check if NOT
'''this is  just the reverse of 'in' keyword result'''

print(f"this is check if in statement \n {"tony" in name}") 

print(f"this is check if not in statement \n {"window" not in name}")

