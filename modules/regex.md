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


## Flags in regex :

- we can modify regex behavior with flags:
    - "re.IGNORECASE "(or re.I): Makes the regex case-insensitive.
    - "re.MULTILINE" (or re.M): Changes the behavior of ^ and $ to match the start and end of each line, not just the start/end of the string.
    - "re.DOTALL" (or re.S): Allows the dot (.) to match newline characters as well.

## Special Sequences :

- A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

| Sequence   | Description                                                  |
|------------|--------------------------------------------------------------|
| `\d`       | Matches any digit (equivalent to `[0-9]`)                    |
| `\D`       | Matches any non-digit                                         |
| `\w`       | Matches any word character (letters, digits, and underscore) |
| `\W`       | Matches any non-word character                               |
| `\s`       | Matches any whitespace character (space, tab, newline)       |
| `\S`       | Matches any non-whitespace character                         |
| `\b`       | Matches a word boundary                                      |
| `\B`       | Matches a non-word boundary                                  |
| `\A`       | Matches the start of the string                              |
| `\Z`       | Matches the end of the string                                |
| `\z`       | Matches the end of the string, ignoring line breaks          |


## SETS :
- A set is a set of characters inside a pair of square brackets [] with a special meaning:

| Set          | Description                                                      |
|--------------|------------------------------------------------------------------|
| `[abc]`      | Matches any one of the characters 'a', 'b', or 'c'               |
| `[^abc]`     | Matches any character except 'a', 'b', or 'c'                    |
| `[a-z]`      | Matches any lowercase letter from 'a' to 'z'                     |
| `[A-Z]`      | Matches any uppercase letter from 'A' to 'Z'                     |
| `[0-9]`      | Matches any digit from '0' to '9'                                |
| `[a-zA-Z]`   | Matches any letter, either lowercase or uppercase                |
| `[a-zA-Z0-9]`| Matches any alphanumeric character (letters or digits)           |
| `[aeiou]`    | Matches any vowel (lowercase in this case)                       |
| `[^0-9]`     | Matches any character that is not a digit                        |
| `[a-z&&[aeiou]]` | Matches any lowercase vowel (intersection of sets)            |
