'''
- some of the various file opertions.
'''

#  Checking if a File Exists : use os module

import os
from file_path import example_txt

if os.path.exists("example.txt"):
    print("file exist")
else:
    print("file not found.") 
    # this result in file not founf


if os.path.exists(example_txt): # this result in file exist.
    print("file exist")
else:
    print("file not found.")


# Renaming a File
try : 
    os.rename("new.txt" , "file_handling/example.txt")
    
except Exception as e :
    print(f"error : {e}")
    print ("renaming failed")
else:
    print("renaming done")


# Deleting a File
os.remove("file_handling/__pycache__/file_path.cpython-312.pyc")
print("file deleted")
# deleting folder :

os.rmdir("file_handling/__pycache__")
print("folder deleted")