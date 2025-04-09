'''
-  so far we did -> open a file -> do the operation such as read /write -> close it manually.

- we can avoid this by using the context managers the "with" statement.
- syntax :
        with open(fileName , mode) as alias
        
its the replacement of :
        alias = open(file_name , mode)
        
-  also we don't need to clsoe the file now. as it is done implicitly.
'''

# opening file to read .
from file_path import example_txt
from file_path import Write_example_txt

with open(example_txt) as reader :
    content = reader.read()
    print(content)
    
    
    
# opening a file in write mode

with open(Write_example_txt,'a') as writer:
    lines = ["this is line 4." , "this is line 5.","👍"]
    writer.writelines(lines)
    