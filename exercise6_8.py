import string
import random

special = "-_~?*$#!+%"
password = ""
sucess = True

length = int(input("Give a password length:(more than 8)\n"))

#adding values to empty varuable following the exercise rules:
password += random.choice(string.ascii_lowercase)
password += random.choice(string.ascii_uppercase)
password += random.choice(string.digits)
password += random.choice(special)

#cheking user input:
if length < 8:
    print("Password length should be more than 8 characters! Please, start application again!")
    #boolean keeps track on printing
    sucess = False
else:
    #loop creats the rest values of password, from 4 up to the number, that was set by user:
    #4 values already exist.
    for i in range(length-4):
        password += random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + special)

#printing result
if sucess:
    print(password)

