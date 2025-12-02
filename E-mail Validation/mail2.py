import re #ye ek regex module hai
email_cond = r"^(?:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@" \
             r"(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+" \
             r"[a-zA-Z]{2,})$"
user_mail = input("Enter your email address: ")
if re.search(email_cond, user_mail): #function hota h search naam ka regex me
    print(f"Email address entered {user_mail} is VALID")
else:
    print(f"E mail address entered {user_mail} is NOT valid")