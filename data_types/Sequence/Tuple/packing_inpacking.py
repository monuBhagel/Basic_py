'''
In python, when we assign value in tuples this is called packing.

but we can also unpack the values to individual variables , this is called unpacking.

'''

# packing

numbers = (1,2,3,4)


# Unpacking

(one,two,three,four) = numbers

print(one)
print(two)
print(three)
print(four)

'''
while doing unpacking the number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
'''

# using asterisk * 

num = (1,2,3,4,5,6,7,8,9)

(one,two, *rest) = num

print(f"one is : {one}")
print(f"two is : {two}")
print(f"the rest  is : {rest}")

'''
If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
'''

# example

numb_2 = (range(1,20))

(first,second,*third_to_18,ninteen) = numb_2

print(f"first is : {first}")
print(f"second is : {second}")
print(f"3rd to 18th is : {third_to_18}")
print(f"ninteen is : {ninteen}")