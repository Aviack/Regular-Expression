#Your password must be atleast 8 character long = {8,}
#Your password must contains at least 1 number and 1 special character == \d+\D+
#Password must have 1st character in upper case == \A[A-Z]

#final match should be == \A[A-Z]\d+\D+{8,}
import re
import getpass
pattern = re.compile(r"")
while True:
    my_str = getpass.getpass("Enter the string: ")
    if(len(my_str)<8):
        print("Password must be minimum of 8 characters long")
    if(re.search(r'[!@#$%]',my_str) is None):
        print("Password should have atleast one special character")
    if(my_str[0].isupper() is False):
        print("First letter of the password should be an Upper case")
    elif(re.match(r"[a-zA-Z0-9!@#$%^&]{8,}",my_str)):
        pattern = re.compile(r"[a-zA-Z0-9!@#$%^&*-+]{8,}")
        result = pattern.match(my_str)
        print("Your password is valid : " , my_str)
        break
    else:
        print("Your password is invalid")
