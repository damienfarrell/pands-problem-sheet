# squareroot.py
# This program takes a positive floating-point number as input and outputs an approximation of its square root.
# Author: Damien Farrell


import math
# Define the function 'sqrt' with one argument of 'number'.
def sqrt(number):
# The calculation part.
# The guess variable.
    prev_n = 0
    n = number
    # Checks whether the answer and the previous answer are close, the default value is 1e-09. When close it exits.
    while math.isclose(n, prev_n) != True:
        #The newton formula for square roots.
        answer = 0.5 * (n + (number / n))
        prev_n = n
        n = answer
    # Returns the answer for the print statement.
    return answer

# The input.
input_number = float(input("Please enter a positive number: "))
# Getting the return out of the fuction.
answer = sqrt(input_number)

print(f"The square root of {input_number} is approx. {answer}.")