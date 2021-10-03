#Write a validatory code to check a user ID which satisfies the following conditions:
'''
1.Only contains alphanumeric chararcter , underscore and dot 
2.Underscore and dot can't be next to each other character
3.Underscore or dot can't be used in multiple times in a row 
4.Underscore and dot  can't be at the end or start of a username 
'''

#pipe in Regexx | 
#positive and negative look ahead || We have to deal with negative look ahead  a[?!b] which means a not followed by b
'''
A positive lookahead will look to make sure the element in the search pattern is there , but won't actually match it 
A positive lookahead is used as (?=...) where the ... is the required part that is not matched.

A negative lookahead will look to make sure the element in the search pattern is not there , 
A negative lookahead is used as (?=...) where the ... is the pattern that you do not want to be there 

'''

import re
pattern = re.compile(r"")
username = input("Enter your username ; ")
pattern = re.compile(r"^[a-zA-Z0-9]|[a-zA-Z0-9]$") # What is difference between ^[a-zA-Z0-9._]$ and ^[a-zA-Z0-9._]
result = pattern.match(username)
print(result)
if(result):
    print("Username Formation is Successful")
else:
    print("Invalid Username")