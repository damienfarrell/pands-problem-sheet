# accounts.py
# This program reads a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
# Author: Damien Farrell


# Took this process from the reference listed in the readme file.
accountnumber = input("Please enter an 10 digit account number: ")
if len(accountnumber) != 10:
    print(f"You have entered: {len(accountnumber)} digits, please enter 10 digits ")
else:
    # Number of characters to replace.
    n = 6
    replacement_string = "XXXXXX"
    # Splicing the string and sticking it together.
    displayed_accountnumber = replacement_string + accountnumber[n:]
    print(f"{displayed_accountnumber}")