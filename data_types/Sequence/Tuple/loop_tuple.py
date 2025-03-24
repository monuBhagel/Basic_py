# Loop Through a Tuple
'''
- we can use various kinds of loop on tuple to go through its item one by one.
    > for loop
    > for loop with index
    > while loop
'''

# tuple

num = (range(1,11))

# for loop

for i in num:
    print(f"item {i} is {i}")
    
# for loop with index

for x in range(1,len(num)+1):
    print(f"item {x} is {x}")
    

# using while loop

tuple_example = ('mango', 'banana', 'papaya','cherry',
                 1,2,3,4,
                 True,False)

i = 0
while i < len(tuple_example):
    print(tuple_example[i])
    i = i + 1