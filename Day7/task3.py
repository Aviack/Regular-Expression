#From a given email ID in input string determine the username and hostname of
import re 
My_file = open("Day7/Email.txt","r")
data = My_file.read() ## read the whole file to a string

match = re.findall(r"(\w+)@(\w+.+)",data)
print(match)
print(type(match[0]))

for a,b in match:
    print("Username=", a, "HostName=" ,b) 
exit()


