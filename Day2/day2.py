#Write the progranm using the regex that will replace all the digits in a string with a  exclamation ! sign 
#Quantifier  == quantity of character to match

'''
______________________________________________________________________
Quantifier    |      Description    |     Example     |  SampleMatch  |
_______________________________________________________________________
+             |    One  or more     |  \w+            | ABC-DEF097    |
_______________________________________________________________________
{2}           | Exactly 2 times     | \d{2}           |  01           | 
_______________________________________________________________________
{1,}          |  One or more time   |     \w{1,}      |      smiling  |
_______________________________________________________________________
{2,4}         |     2,3 or 4 times  |      \w{2,4}    |        1234   |
_______________________________________________________________________
*             |  zero or more times |  A*B            | AAAAAAAB      |
_______________________________________________________________________
?             |  once or none       | \d+?            | 1 in 12345    |
_______________________________________________________________________
'''

import re
routine = re.compile(r"")
myString = input("Enter the string : ")
pattern = re.compile("\d{2,4}")
FinalOne=pattern.sub("!", myString)
print(FinalOne)


'''
Set      |           Description
----------------------------------------------------------------------------------------
[arn]    | Returns a match where one of the specified characters(a , r or n) are present   
________________________________________________________________________________________
[a-n]    | Returns a match for any lower case character , alphabetically between a and  n 
_________________________________________________________________________________________
[^arn]   | Returns a match for any character EXCEPT a , r, and n characters
_________________________________________________________________________________________
[0123]   | Returns a match where any of the specified digits(0,1 ,2 or 3)  are present 
_________________________________________________________________________________________
[0-9]    | Returns a match where any digits between 0 to 9 
_________________________________________________________________________________________
[0-5]    | Returns a match for any two digits number from 00 to 59 
[0-9]    | 
_________________________________________________________________________________________
[a-zA-Z] | Returns a match for any character  alphabetically between a and z , lower or upper case
_________________________________________________________________________________________
[+]      | In sets +*.|()${} has no special meaning : returns a match for any + character in the string
________________________________________________________________________________________________________


'''
