"""
bank.py
The program should:
    Prompt the user and read in two money amounts (in cent)
    Add the two amounts
    Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount
Author: Damien Farrell
"""


# Inputs as variables.
amount1 = int(input("Enter amount1(in cent): "))
amount2 = int(input("Enter amount2(in cent): "))

# Calculation to put as two decimal places for euros & cent. Also converted the string to int here.
total = amount1 + amount2

euros = total // 100
cent = total % 100

 # Printing the answer in a formatted string to two decimal places ":.2f".
print(f'The sum of these is €{euros + cent/100:.2f}')