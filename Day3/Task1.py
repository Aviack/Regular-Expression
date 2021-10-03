#Write a program to simply generate a password which consists of numbers and characters
'''
\w is equivalent to \d and \D together
\w is equivalent to [a-zA-Z0-9] || \w does not match special character
\W do matches the special character
@#avadh


'''


import re
pattern = re.compile(r"")
password= input("Enter your password: ")
pattern = re.compile(r'[a-zA-Z0-9!@#$%^&*]')
result = pattern.match(password)
print(result)
if(result):
    print("You password is correct " + password)
else:
    print("your password does not match")

