#Write a program to simply generate password which consist of numbers and characters and it should be atleast 6 characters long
import re
pattern = re.compile(r'')
while True:
    my_str = input("Enter the string: ")
    if(len(my_str)<6):
        print("Password must be minimum of 6 characters long")
    elif(re.match(r"[a-zA-Z0-9!@#$%^&*_+]{6,}",my_str)):
        pattern = re.compile(r"[a-zA-Z0-9!@#$%^&*_+]{6,}")
        result = pattern.match(my_str)

        print("Your password is valid : " , my_str)
        break;
    else:
        print("Your password is invalid")
