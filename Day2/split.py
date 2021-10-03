import re 
splitPattern = "\d"
input1 = "All is well1Toallnothing2well"
splittedList = re.split(splitPattern,input1 ,1)
print(splittedList)