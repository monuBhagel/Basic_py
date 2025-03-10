# we can take multiple input from user in single line , spliting the values 
# entered by the user into multiple variables using split() method


# keep that in mind that you have to enter input using space not the enter key
# if you enter i=one input and press enter than the Value Error will happen
x , y = input("enter two numbers : ").split()


print(x)
print(y)