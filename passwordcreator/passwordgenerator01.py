# Original code from: http://instagram.com/p/Cu3nUuQrKUy
# Password Generator
# This password generator mix uppercase, lowercase, numbers and symbols
# Lenght is hardcoded

# Random library
import random

# Defining lowercase, uppercase, numbers and symbols variables 
lower = "abcdefghijklmnñopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-!?#$%&="

# Joining all variables
all_chars = lower + upper + numbers + symbols

# Password lenght
lenght = 16

# Creatng password with random.sample()

# Syntax : random.sample(sequence, k)
# Parameters:
# sequence: Can be a list, tuple, string, or set.
# k: An Integer value, it specify the length of a sample.
# Returns: k length new list of elements chosen from the sequence.
password = "".join(random.sample(all_chars, lenght))

# Print final password
print(password)
