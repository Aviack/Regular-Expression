#Task 1 (Day1) to write a program that will replace all the digites in a string with an underscore
import re
pattern = re.compile(r"")
my_string = input("Enter the string: ")
pattern = re.compile(r"\daf")
result = pattern.sub("$", my_string)
print(result)

# What is the difference betweent the "[0-9]" and  "[0-9]+"
# + is used when the character is used one or  more times 

'''
"."   ==  Matches any single character except newline character
"\d"  ==  This matches any digit[0-9]
"\D"  ==  This mathces any non-digit character[^0-9]
"\s"  ==  This matches the white space character [\t\n\r\f\v]
"\S"  ==  This matches non-whitespaces character [^\t\n\r\f\v]
"\w"   ==  This matches alpha_numeric character [a-zA-Z0-9_]
"\W"   ==  This matches non alpha_numeric character [a-zA-Z0-9_]
"\A"  ==  Returns a match if the specified characters are at the beginning of the STRING
"\b"  ==  Returns a match if the specified character are at the beginning or at the  end  of  a WORD
"\B"   ==  Returns a match where the specfied  character are present , but NOT at the beginning (or at the end ) of WORD
"\Z"  ==  Returns a match if the specifies character are at the  end of the STRING
'''
