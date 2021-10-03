#Write a program to verify the last letter of the input is correct as it was entered.

import re
my_string = "Avadh is very good boy"
pattern = re.findall("yo$" , my_string)
if(pattern):
    print("It ends with the boy")
else:
    print("No match")
