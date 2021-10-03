# My own regex to find the email ids = (\w|\W)+(\.|\_)?([\w]+)[@][\w]+(\.[a-z]{1,255})(\.[a-z]+)?


import re 
pattern = re.compile(r"")
user_login = input("Enter the second part of the email ID: ")
pattern = re.match(r"(\w|\W)+(\.|\_)?([\w]+)[@][\w]+(\.[a-z]{1,255})(\.[a-z]+)?",user_login)
if pattern == None:
    print("Invalid email ID")
else:
    print(pattern)