'''
- reading a file in python is easy . just 
    - open it in read mode.
    - take content in a varible.
    - print it .
'''

# reading example
from file_path import example_txt

try :
    file = open(example_txt,'r')
    
except FileNotFoundError  :
    print("file not found. check the path.")

else : 
    print("file opened successfully.👍")   
# above code open the file and throw error if it is not present.
    
# now reading the content of it.
    content = file.read()
    print(content)
    
finally :
    try :
        file.close()
        print(f"file closed successfully.")
    except Exception as e:
        print("file not found to close.")
'''
- Once a file is opened, we can read its contents using various methods:
  
   -  file.read(size): Reads the entire file or a specified number of   bytes.
   -  file.readline(): Reads the next line from the file.
   -  file.readlines(): Reads all lines into a list.
'''

# we can also read file line by line and not all at once using readline and readlines methods.

# opening the file in read mode.
try :
    file = open(example_txt,'r')
    
except FileNotFoundError  :
    print("file not found. check the path.")

else : 
    print("file opened successfully.👍")   
# above code open the file and throw error if it is not present.
    
# now reading the first line of it.
    first_line = file.readline()
    print("first line of file is :")
    print(first_line , end= " ")
    
finally :
    try :
        file.close()
        print(f"file closed successfully.")
    except Exception as e:
        print("file not found to close.")
        

# reading multiple line .

# opening the file in read mode.
try :
    file = open(example_txt,'r')
    
except FileNotFoundError  :
    print("file not found. check the path.")

else : 
    print("file opened successfully.👍")   
# above code open the file and throw error if it is not present.
    
# now reading the first line of it.
    lines = file.readlines() # this provides a list of line .
    
    # accessing list of lines using  loop
    for line in lines:
        print(line)
    
finally :
    try :
        file.close()
        print(f"file closed successfully.")
    except Exception as e:
        print("file not found to close.")
        
