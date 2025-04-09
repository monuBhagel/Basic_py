'''
- Regular expression in python have a dedicated module called "re" module

- A regex or regular expression is a sequence of characters that forms a search pattern

- Match Object
    - A Match Object is an object containing information about the search and the result.
    - If there is no match, the value None will be returned, instead of the Match Object.

- The Match object has properties and methods used to retrieve information about the search, and the result:

    - .span() returns a tuple containing the start-, and end positions of the match.
    - .string returns the string passed into the function
    - .group() returns the part of the string where there was a match

### for more detail refer to "regex.md" file.
'''

import re 

greet = "hello  world lo , what's up .."

# Functions in the re module:

'''
1. re.match(): Checks if the pattern matches at the beginning of the string.
    it returns a match object.
'''
matched = re.match('hello',greet)

print(matched) # <re.Match object; span=(0, 5), match='hello'>

print(matched.string)
print(matched.span())
print(matched.end())
print(matched.start())
print(matched.lastindex)


'''
2. re.search(): Searches for the pattern anywhere in the string.
    it returns a match object.
'''

searched = re.search('lo' , greet)

print(searched) # <re.Match object; span=(0, 2), match='he'>


'''
3. re.findall(): Finds all occurrences of the pattern in the string and returns them as a list.
'''
findall = re.findall('lo', greet)
print(findall) # ['lo', 'lo']

'''
4. re.sub(): Replaces occurrences of the pattern with a specified string.
'''
greet = "hello world lo , what's up .."

subString = re.sub('lo', 'LO' , greet)

print(subString)
print(greet)

'''
5. re.split(): Splits the string by occurrences of the pattern.
'''

splited = re.split("\s" , greet)
print(splited)