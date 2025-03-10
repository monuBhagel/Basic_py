#Keywords in python are special word which have special meaning and serves special purposes.

# these word can not be used as the name for variable , function and classes or any other kind type of indentifer


# Getting List of all Python keywords through python program
import keyword
import os

# Get the list of all Python keywords
keywords = keyword.kwlist


# Specify the path to the folder where you want to save the file
folder_path = "general_syntax"  # path to the txt file


# Ensure the folder exists
os.makedirs(folder_path, exist_ok=True)


# Specify the full path for the output file
file_path = os.path.join(folder_path, "keywords.txt")

# Open the text file in write mode
with open(file_path, "w") as file:
    # Write each keyword on a new line
    for kw in keywords:
        file.write(kw + "\n")

print(f"Keywords have been written to '{file_path}'.")
