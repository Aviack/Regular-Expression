#Write the program to validate the Debit Card Number

import re 
pattern = re.compile(r"[\d]{4}(\/|\s|\-)[\d]{4}(\/|\s|\-)[\d]{4}(\/|\s|\-)[\d]{4}")
while True:
    card = input("Enter the Sixteen digit debit card Number in format 1234 1234 1234 1234 =")
    if(len(card)!=19):
        print("Card is not validated")
    else:
        if(pattern.match(card) is not None):
            print("Number is correct")
        break
