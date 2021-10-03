#write a program to verify the 1st letter of the input string is correct as it was entered without using ^ operator
import re
my_string = "Avadh is good boy"
pattern = re.search("\AAvadh", my_string)
print(pattern)
if(pattern):
    print("Yes it matches ")
else:
    print("It does not matches")