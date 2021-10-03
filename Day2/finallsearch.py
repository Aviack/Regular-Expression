# difference between findall and search

import re 
string1 = "All is well and all is All"
pattern = "All"
match = re.search(pattern,string1)
print(match)


# out put of findall 
#['All', 'All']
#output of search
#<re.Match object; span=(0, 3), match='All'>