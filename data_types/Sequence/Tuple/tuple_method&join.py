# we can join two tuple using + operator

tup_1 = (1,2,3)

tup_2 = (4,5,6)

tup_3 = tup_1 + tup_2

print(tup_3)

'''
Multiply Tuples
If we want to multiply the content of a tuple a given number of times, you can use the * operator:
'''

tup_4 = tup_1 * 2

print(tup_4)

'''
- tuple method are :
    1. count
    2. index 
'''

fruits = ('apple','banana','cherry','apple','apple','cherry')

print(fruits.count('apple')) # return the no. of ocurrence

print(fruits.index('cherry')) # return the index of first ocurence
