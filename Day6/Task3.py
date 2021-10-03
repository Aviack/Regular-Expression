#Write the program to validate the PAN card number 

import re 
pattern = re.compile(r"[a-z]{5}[\d]{4}[a-z]{1}")
while True:
    pan = input("Enter the  10 digit pan card number")
    if(len(pan)!=10):
        print("please enter the valid Pan number")
    else:
        if(pattern.match(pan) is not None):
            print("you have Enter the valid PAN number")
        break