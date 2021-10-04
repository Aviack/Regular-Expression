# Case insensitive matching

'''
But sometimes you care only about matching the letters without worrying whether they’re uppercase or lowercase. To make your regex case-insensitive, you can pass 
re.IGNORECASE or re.I as a second argument to re.compile().

'''

import re

pattern = re.compile(r"robocop", re.IGNORECASE)

string1 = "RoboCop is part man, part machine, all cop."
string2 = "RoboCop is part man, part machine, all cop."
string3 = "Al, why does your programming book talk about robocop so much?"

match1 = pattern.search(string1).group()
match2 = pattern.search(string2).group()
match23 = pattern.search(string3).group()
print(match1)
print(match2)
print(match23)
