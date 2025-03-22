# accessing list

'''
- List items are indexed and we can access them by referring to the index number:
        > The indexing start from 0

- Negative Indexing : 
        > in negative indexing , index start from -1 not 0
        > it means start from the end .
        > -1 refer to last item and -2 refer to second last item
        
- Range of Indexes :
        > we can specify the range of index by telling the starting index and ending index .
        > when we do that the return we get is a "new list" containg the items we searched for through indexing.
        > keep in mind when using indexing : the starting index is "inclusive" and the ending index is "exclusive"
        
- Check if Item Exists :
        > to check if a item exist in the list or not use membership operator that is "in" operator
'''

# list created
fruits = ['apple' , 'banana', 'cherry' , 'mango']

# accessing through indexing

fruit_1 = fruits[0]  # apple

print(fruit_1)


# accessing using negative indexing

fruit_sec_last = fruits[-2]

print(fruit_sec_last)  # cherry



# accessing through range

fruits_2_to_4 = fruits[1:4]

print(fruits_2_to_4)  # ['banana', 'cherry', 'mango']


# increasing size of fruits by adding items to it

fruits.append('kiwi')
fruits.append('guava')
fruits.append('melon')
fruits.append('orange')

print(fruits)

# accesing through range 

fruits_from_3_to_end = fruits[3:]

print(fruits_from_3_to_end) # ['mango', 'kiwi', 'guava', 'melon', 'orange']


fruits_from_start_to_kiwi = fruits[ : (fruits.index('kiwi') + 1)]

print(fruits_from_start_to_kiwi) # ['apple', 'banana', 'cherry', 'mango', 'kiwi']


# check if item exist

check_chiku = 'chiku' in fruits

print(f"chiku exist in fruits : {check_chiku}")


# can also do using functions.
'''
def check_chiku():

    return 'yes' if 'chiku' in fruits  else 'no'

print(f"is chiku exist in fruits : {check_chiku()}")'''

# or using if else or ternary operator

if 'chiku' in fruits:
    print("chiku is present in the fruits list")
    
else :
    print("chiku is not in the list don't buy it fool.")