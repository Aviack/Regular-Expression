#Matching the new line with dot character

'''

he dot-star will match everything except a newline. By passing re.DOTALL as 
the second argument to re.compile(), you can make the dot character match 
all characters, including the newline character.

'''

import re 
pattern1 = re.compile(r".*")
pattern2 = re.compile(r".*", re.DOTALL)

String  = 'Serve the public trust.\nProtect the innocent. \nUphold the law'

search = pattern1.search(String)
search2 = pattern2.search(String)
print("----------------------------")
print(search.group())
print("----------------------------")
print(search2.group())
print("----------------------------")
