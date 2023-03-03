# collatz.py

# Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.

# Author: Damien Farrell


number = int(input("Please enter a positive integer: "))

# The end goal is to let the number equal 1. The number of steps are unkown. 
# So a loop until the input number is equal to 1 would work.
while number != 1:
# Using the mod remainder with a if statement to check whether the number is odd or even.
    if number % 2 == 0:
# Condition if even and true
        number = number // 2
    else:
# Condition if odd and false
        number = (number * 3) + 1
    print(number, end=" ")