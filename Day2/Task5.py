#Write a program to search any given word of input string and also verify it's position within

'''
DIFFERENCE BETWEEN FINDALL AND search

So findall is giving all the same words. But it's not giving the span , while 
search is giving the 1st occurence with the span

'''

import re
my_string = "Avadh is good boy"
pattern = re.search("is", my_string)
print(pattern)
if(pattern):
    print("Yes it matches ")
else:
    print("It does not matches")