F = input("Enter Your First name: ")
L = input("Enter Your Last name: ")
U = input("Enter Your Username: ")
s = input("Enter email id: ")

import re

# Validating email
pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
while True:
    if re.match(pat, s):
        print("Valid Email")
    break
s = input("re-Enter email id: ")
# creating password
pwd = input("Create password: ")
reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

while True:
    bat = re.compile(reg)  # compiling regex
    mat = re.search(bat, pwd)  # searching regex
    # validating conditions
    if mat:
        R = input("Re-Enter password: ")
        if pwd == R:
            print("strong Password.")
            break
        print("Password not same")
    pwd = input("Try again: ")

from pathlib import Path
import csv

fields = ['First Name', 'Last_Name', 'username', 'email_id', 'Password']  # file header names
filename = "User_details.csv"  # name of csv file

# creating a file
csvwriter = Path("User_details.csv")
csvwriter.touch(exist_ok=True)
with open(filename, 'a') as csvfile:
    csvwriter = csv.writer(csvfile)  # creating a csv writer object
    csvwriter.writerow(fields)
    data = [(F, L, U, s, pwd)]
    csvwriter.writerows(data)
    print("login created")
