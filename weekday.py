# weekday.py
# Author: Damien Farrell
# Write a program that outputs whether or not today is a weekday.


# In order to retrieve the date I must import the date method from the datetime module.
from datetime import date 

# Assigning a variable using the imported date method.
today = date.today() 

# Using this method to assign a number to the week 1-7.
weekday_number = date.isoweekday(today)

# Using a if statement to determine whether it is a weekday with over 5 being the weekend.
if weekday_number > 5:
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")