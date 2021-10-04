'''
This is the important task. Say, I have a file ... a big file in notepad or doc file .Along with 
some data , it also contains numerous emailIDs . I have to extract all email IDs . 
Task is to extract all the emailID


'''

import re 
My_file = open("Day7/Email.txt","r")
data = My_file.read() ## read the whole file to a string
print(type(data))


pattern = re.compile(r"\S+@\S+")

emails = pattern.findall(data)
print(emails)
My_file.close()