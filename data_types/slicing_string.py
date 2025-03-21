# we known that string in python are arrays of bytes representing unicode characters.
# this mean we can preform all the actions that we do with arrays on strings.

gretting = "---hello-worlld---"

# slicing 
''' we can return a range of characters by using the slice method
    [start index : end index : step value ]
'''
slice_4_to_9 = gretting[4:9]
print(slice_4_to_9)

# slice from the start to some index
'''slice_start_to_9 = gretting[0:9]
print(slice_start_to_9)'''

'''OR we can use [ : end index ] this will also retun the same result as [0 : end index]'''
slice_start_to_9 = gretting[:9]
print(slice_start_to_9)

# Slice To the End
''' we can return the characters from the start to the end of the string by using [start index :]'''

slice_from_some_index_to_end =gretting[3:]
print(slice_from_some_index_to_end)

# Negative Indexing

'''we can use negative indexing to start the slice from the end of the string '''
negitive_indexing = gretting[-9 : -3]
print(negitive_indexing)