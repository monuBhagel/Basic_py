'''
- writing to a file or creating it can be done using write() and append().
-  we can pass a string , a iterable in the write or append ()

'''

# opening a file with write method.
from file_path import Write_example_txt

file = open(Write_example_txt, 'w')

file.write("this is new file created through write method .👍")

file.close()

# writing multiple line at once .

# file = open(Write_example_txt, 'w') # this is rewrite the already present content so to avoid this we use append.
content = ["\nLorem ipsum is typically a corrupted version of De finibus bonorum et malorum, a 1st-century BC text by the Roman statesman and philosopher Cicero, with words altered, added, and removed to make it nonsensical and improper Latin.\nThe first two words themselves are a truncation of dolorem ipsum (\"pain itself\")."]

try:
    file = open(Write_example_txt, 'a')
    print("file opened in write mode .")
except Exception as e :
    print(f"error : {e}")
    
else:
    file.writelines(content)
    print("content written successfully.👍")
    
finally:
    file.close()
    print("file closed .")