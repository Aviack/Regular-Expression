#From the given input string determine the longest word in the string

import re 
my_str = input("Enter the string: ")
my_str = re.findall(r"\S+",my_str)
max_len = max(len(word) for word in my_str)
print("The maximum length of the word in sentence is ", max_len)
for word in my_str:
    if(len(word))==max_len:
        print(word, "is the the longest of all")
        