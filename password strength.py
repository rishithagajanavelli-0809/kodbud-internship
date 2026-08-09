import re

password = input("Enter your password: ")

if (len(password) >= 8 and
    re.search(r"[A-Z]", password) and
    re.search(r"[0-9]", password) and
    re.search(r"[^A-Za-z0-9]", password)):

    print("Password Strength: Strong")
else:
    print("Password Strength: Weak")