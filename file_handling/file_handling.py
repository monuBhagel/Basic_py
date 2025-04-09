'''
- file handling is an important task every programmer should known how to do .
- python provides us several functions for creating, reading, updating, and deleting files.
- such as :
    1. Opening a File :
        - using open()
        - using with statement
    
    2. Reading from a File :
        - using read()
    
    3. Writing to a File :
        - using write()
        
    4. closing a file :
        - using close()
'''

# 1. opening a file. & closing it.
'''
- we can open a file using open(). this take an arg as name/path of file.
- default mode of opening is read mode -> r
- various mode of opening a file :
    1.read r : opens a file for reading. If the file does not exist, it throws a FileNotFoundError.
    
    2.write w : opens a file for writing. Creates a new file if the file doesn’t exist or truncates the file if it exists.
    
    3.append a : opens a file for appending. If the file does not exist, it creates a new file.
    
    4.binary b : used with other modes (e.g., "rb" or "wb") for reading or writing binary files (like images or audio files).
    
    5.exclusive creation x : creates a new file, but raises an error if the file already exists.
    
'''
file_path = "file_handling/example.txt"
try :
    file = open(file_path, "r")  # Open for reading
    
except Exception as e:
    print(f"error : {e}\nfile not found to open." )
    
else :
    print("file opened successfully")
    
finally:
    try :
        file.close()
        print(f"file closed successfully.")
    except Exception as e:
        print("file not found to close.")
    
    
