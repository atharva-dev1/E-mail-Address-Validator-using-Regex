import re #ye ek regex module hai
#condition check:
"""
a-z
A-Z
0-9
._ one time
@ one time
. 2 ,3 
"""
email_cond = "^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$" #email ki conditions hain
user_mail = input("Enter your email address: ")
if re.search(email_cond, user_mail): #function hota h search naam ka regex me
    print(f"Email address entered {user_mail} is VALID")
else:
    print(f"E mail address entered {user_mail} is NOT valid")