# accounts.py
# This program reads a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
# Author: Damien Farrell

accountnumber = input("Please enter an 10 digit account number: ")
n = 6
replacement_string = "XXXXXX"
displayed_accountnumber = replacement_string + accountnumber[n:]

print(f"{displayed_accountnumber}")