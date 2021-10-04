# Match everything with the .* [greedy] .*?[non greedy]
import re

StringOne = "<To serve man> for dinner.>"

pattern1 = re.compile(r"<.*>")
pattern2 = re.compile(r"<.*?>")

match1 = pattern1.search(StringOne)
match2 = pattern2.search(StringOne)
print(match1.group())
print(match2.group())