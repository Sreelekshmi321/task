#How to split the names in based on special character


import re                         #RegEx or regular expression,  used to check if a string contains the specified search.
line ='zlight research'           #line as a variable
split=re.split('\s',line)         #split() is a method , split the string into list string is zlight research
print("first  word:",split[0])       
print("second  word:",split[1])     #print first word and second word
                                    