# write the program to validate the date of birth and
#input should be in the format 12/12/2021


import re
pattern = re.compile(r"([\d]{2})[\/|\-]([\d]{2})[\/|\-]([\d]{4})")
while True:
    Date = input("Enter your birthDate :")
    print(len(Date))
    if(len(Date)!=10):
        print("Please enter the valid birth date in format 12/12/2021 or 12-12-2021")
    else:
        if(pattern.match(Date) is not None):
            print("You have enter the correct birthdate")
            break

