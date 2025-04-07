'''
- dates in python have a dedicated module called datetime.
'''

# datetime module.

import datetime as dt

# datetime module has a class called datetime. which has a method called "now" 

current_datetime = dt.datetime.now()
print(current_datetime)  # 2025-04-07 19:58:37.790814

# The date contains year, month, day, hour, minute, second, and microsecond.

# The datetime module has many methods to return information about the date object. some of them are :

# 1.year
print(current_datetime.year) # 2025

# 2. month 
print(current_datetime.month) # 4 

# 3. day
print(current_datetime.day) # 7 

# 4. hour
print(current_datetime.hour) # 20

# 5 . minute
print(current_datetime.minute) # 2
# 6. second
print(current_datetime.second) # 12
# 7. microsecond
print(current_datetime.microsecond) # 123456
# 8. weekday
print(current_datetime.weekday()) 
'''
0 = monday
1 = tuesday
.
.
.
6 = sunday
'''
# Creating Date Objects

'''
- to create a date object we need three arguments : year , month and day.
- The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).
'''

date = dt.datetime(2025 , 4 , 7)
print(date) # 2025-04-07 00:00:00

