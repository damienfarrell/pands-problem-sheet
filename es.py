# es.py
# A program that reads in a text file and outputs the number of e's it contains. The program takes the filename from an argument on the command line.
# Author: Damien Farrell


# Assume that the input file exists within the root directory folder
# Import sys in order to use cmd with arguments
import sys

letter_to_count = "e"

# If statement - if the argument in the cmd line is not entered it requests one to be added.
if len(sys.argv) < 2:
    print("Please enter the filename of the text file to search after 'python es.py'")
else:
    filename = sys.argv[1] # The string after the py file will be the argument for the txt file to search.
    # Open the file in read mode.
    with open(filename, "r") as txt_file:
        # Reading it.
        book = txt_file.read()
        # Counting the number of letters.
        number_of_letters = book.count(letter_to_count)
    print(number_of_letters)