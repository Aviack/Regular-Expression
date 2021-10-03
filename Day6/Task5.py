# Write the program to validate the IP Address




import re 
pattern = re.compile(r"(\d{1,3}[\.]){3}\d{1,3}")
ip = input("Enter your IP address ")
if(pattern.match(ip) is not None):
    print("Correct")
else:
    print("OOOPs you are screwed")
