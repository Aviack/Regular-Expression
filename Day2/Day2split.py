import re
my_string = "avadh is 12very good boy"
pattern = re.split(r"\b[12]\w",my_string )
print(pattern)