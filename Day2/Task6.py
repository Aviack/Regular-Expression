#write a program to search for an upper case character in the beginning of a word  ,and print its position
'''
ATTRUIBUTE RELATED TO SEARCH OPERATION
.span() ==  returns a tuples containing the start and end positions of the matching characters
.string == returns the string passed into the function function
.group() ==  returns the part of the string where there was a match 

'''
import re
my_str = "I am Iron Man"
result = re.search(r"\bI\w*", my_str)
print(result)