# validate the aadhar card numer 

import re 
pattern = re.compile(r"")

pattern  = re.compile(r"([\d]{4})(-|\/)([\d]{4})(-|\/)([\d]{4})")

while True:
    aadhar = input("Enter your aadhar card number")
    if (len(aadhar)!=14):
        print("please enter the valid aadhar card number")
        
    else:
        if(pattern.match(aadhar) is not None):
            print("Your aadhar number is correct ")
            break
        

