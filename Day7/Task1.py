#Split the given string to form a list
import re
my_str = input("Enter the String")
pattern = re.compile(r"\s+")
splitted = pattern.split(my_str)
print(splitted)