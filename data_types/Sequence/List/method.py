# Get all attributes of a list object
list_methods = dir(list)

# Filter out non-method attributes (like dunder methods)
list_methods_filtered = [method for method in list_methods if callable(getattr(list, method))]

# Create markdown content
markdown_content = "# List Methods in Python\n\n"
markdown_content += "Here is a list of methods that can be used on Python lists:\n\n"
for method in list_methods_filtered:
    markdown_content += f"- {method}\n"

# Save it to a .md file
file_path = "data_types/Sequence/List/list_methods.md"
with open(file_path, "w") as file:
    file.write(markdown_content)

print(f"Markdown file saved as {file_path}")
