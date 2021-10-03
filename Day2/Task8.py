#Write a program to search for the character in the beginning of a word and print that complete word.
import re as r
my_string = "8Avenger Avenger"
result = r.search(r"\b[a-zA-Z]+" ,my_string)
print(result.group())