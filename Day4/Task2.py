## Write e program where user and ID password should not be same 
import re
pattern1 = re.compile(r"^[\w]([._](?![._])|[\w]){7,20}[\w]$")
pattern2 = re.compile(r"[a-zA-Z0-9@#$%^&*]{1,6}")

username = ""
password=""

while not pattern1.match(username):
    username = input("Enter your username: ")
