#
# Author: Alfonso Zepeda
# Created: 22 - July - 2023
#
# Password Generator
# You can choose to add your password: uppercase, lowercase, numbers and/or symbols
# You can choose the lenght of the password
# (c) GPL-3.0 license
#
# Original code from: http://instagram.com/p/Cu3nUuQrKUy
# 


# Random library
import random

# Function choose characters
def chooseChar(choosenString, selectedString):
    ''' Function will return the complete string if selected

        This function will receive the complete char collection and string that represents,
        with this information it will return the complete char collection if selected.

        Args:
            choosenString(string): Complete char collection
            selectedString(string): Name of the collection
        
        Returns:
            choosenString(string): if selected it returns the complete char colection if not just an empty string.
            
    '''
    while(True):
        message = "Do you want, your password, with " + selectedString + "? (Y\\N): "
        x = input(message)
        if(x.lower() == "yes" or x.lower()== 'y'):
            return choosenString
            break
        elif (x.lower() == "no" or x.lower()== 'n'):
            return ""
            break
        else:
            print('please choose Y\\N')

# Function choose lenght
def chooseLenght():
    ''' Function will return the lenght of the password

        This function will ask for the lenght of the password to keep it between 1-20 chars.

        Args:
            none
        
        Returns:
            lenghtPass(int): It returns the lenght as integer number.
            
    '''
    while(True):
        message = "Please type the lenght of your password? (1-20): "
        try:
            lenghtPass = int(input(message))
            if (lenghtPass < 1):
                print("Please type a number greater than 0")
            elif (lenghtPass > 20):
                print("Please type a number lower than 20")
            else:
                return lenghtPass
        except:
            print("Please type integer characters.")
        

# Welcome message
print("Welcome to Password Generator 2 \n")

# Defining lowercase, uppercase, numbers and symbols variables 
lower = "abcdefghijklmnñopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-!?#$%&="

all_chars = ""

# Choose variables and join them to "all_chars"

all_chars += chooseChar(lower, "lowercase")
all_chars += chooseChar(upper, "uppercase")
all_chars += chooseChar(numbers, "numbers")
all_chars += chooseChar(symbols, "symbols")

# Password lenght
lenght = chooseLenght()

# Creatng password with random.sample()
# https://www.geeksforgeeks.org/python-random-sample-function/
# Syntax : random.sample(sequence, k)
# Parameters:
# sequence: Can be a list, tuple, string, or set.
# k: An Integer value, it specify the length of a sample.
# Returns: k length new list of elements chosen from the sequence.
password = "".join(random.sample(all_chars, lenght))

# Print final password
print("\nYour password is: \n\n")
print(password)
print("\n")