#Day 2 Task one  ==  to write  a program that will replace all the non digits in a string with a '_' sign


'''
FUNCTION  : - findall

'''


import re
routine = re.compile(r"")
String = input("Enter your String: ")
pattern  = re.compile("\D+")
ans=pattern.sub("_", String)
print(ans)
