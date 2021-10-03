#Write a program to verify the first letter of the input is correct as it was entered.

'''
^, and $ are boundaries . ^ marks the start and is also known as Hat , while $ marks tha end of the regular expression.
But keep in mind that if you use ^ inside it meaning changes completely []

'''

import re
my_string = "Avadh is very good boyyy"
pattern = re.findall("^Av" , my_string)
if(pattern):
    print("Yes the string start with the Avadh")
else:
    print("No matches")