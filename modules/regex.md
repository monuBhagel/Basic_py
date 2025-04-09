# __**Regular expression in python**__

- A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
- For example, \d+ could be a pattern to match one or more digits.
- Python has a built-in package called "re", which can be used to work with Regular Expressions.


## RegEx Functions : 
the re module provides us function which allow us to search for patterns in the string . 

|function      |Description                 |
|--------------|----------------------------|
|findall      |Returns a list containing all matches                  |
|search      |Returns a Match object if there is a match anywhere in the string                 |
|split      |Returns a list where the string has been split at each match                 |
|sub      |Replaces one or many matches with a string                 |


## Meta characters :
- Meta-characters: Special characters that have a specific meaning in a regular expression.
    - . : matches any character except a new line.
    - [] : A character class, for example, [aeiou] matches any vowel.
    - ^ : Starts with.
    - $ :  Ends with.
    - "*" : Zero or more occurrences
    - "+" : One or more occurrences
    - ? : Zero or one occurrences
    - {} : Exactly the specified number of occurrences 
    - \ : Signals a special sequence (can also be used to escape special characters)
    - \d : Matches any digit (equivalent to [0-9]).
    - \w : Matches any word character (letters, digits, and underscore).
    - \s : Matches any whitespace character (spaces, tabs, line breaks).
    - () : Groups patterns together, for example, (abc)+ matches one or more occurrences of "abc".
    - | : Acts as an OR operator. For example, a|b matches either 'a' or 'b'.


