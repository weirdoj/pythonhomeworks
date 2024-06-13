"""
Randomly return two numbers between 1 and 6

Author: Jimmy
Date:  03152024
"""
import random

# generate two random number between 1 and 6

number1 = random.randint(1,6)
number2 = random.randint(1,6)

# Tell user the result
print("You rolled a " + str(number1) + " and a " + str(number2))
