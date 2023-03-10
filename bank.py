"""
bank.py
The program should:
    Prompt the user and read in two money amounts (in cent)
    Add the two amounts
    Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount
Author: Damien Farrell
"""


# Inputs as variables.
amount1 = input("Enter amount1(in cent): ")
amount2 = input("Enter amount2(in cent): ")

# Calculation to put as two decimal places for euros & cent. Also converted the string to int here.
total = (int(amount1) + int(amount2))/100

 # Printing the answer in a formatted string to two decimal places ":.2f".
print(f'The sum of these is €{total:.2f}')