#write a program to search for an upper case character  in the beginnig of a word and print that complete word

import re 
string = "all is Well and Avadh"
pattern = re.search(r"\b[A-Z][a-zA-Z]+", string)
print(pattern.group())

'''
"\b[A-Z][a-zA-Z]+" or "\b[A-Z]\w+
'''