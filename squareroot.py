# squareroot.py
# This program takes a positive floating-point number as input and outputs an approximation of its square root.
# Author: Damien Farrell


# Define the function 'sqrt' with one argument of 'number'.
def sqrt(number):
# The calcuation part.
# The guess variable.
    n = 5
# The iterator.
    y = 0
    while y < 20:
        #The newton formula for square roots.
        answer = 0.5 * (n + (number / n))
        n = answer
        y += 1
    # Return both the input number and answer for the print statement.
    return number, answer

# The input.
input_number = float(input("Please enter a positive number: "))
# Getting the returns out of the fuction.
number, answer = sqrt(input_number)

print(f"The square root of {number} is approx. {answer}.")