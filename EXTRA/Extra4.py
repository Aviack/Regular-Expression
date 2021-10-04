# Sometimes you may need to use the matched text itself as part of the substitution

'''
In the first argument to sub(), you can type \1, \2, \3, and so 
on, to mean “Enter the text of group 1, 2, 3, and so on, in the substitution.


'''


import re 
pattern = re.compile(r"Agent (\w)\w*")

string = "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent"

substitution = pattern.sub('\1', string)
print(substitution)