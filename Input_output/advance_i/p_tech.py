# taking multiple inputs using split and map function
# the split() method splits the space-separated inputs and returns an iterable
# whereas when this function is used with the map() function it can convert the 
# inputs to float and int accordingly.

x , y = input("enter two number :").split()

print(f"type of x = {type(x)} and type of y is {type(y)}")

# the above code retrun string 

# we want input in other format so we do this

i , f = map(int , input("enter two number :").split() )
print(f"type of x = {type(i)} and type of y is {type(f)}")

'''---------------------------------------------------------'''

# Taking input as a list or tuple: 

n = list(map(int,input("type numbers :").split()))
print(n)

'''---------------------------------------------------------'''

# Taking Fixed and variable numbers of input: 
str, *lst = input().split()
lst = list(map(int, lst))
 
print(str, lst)