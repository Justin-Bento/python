"""
  - [x] Program make a simple calculator.
  - [x] Creat a function to handle these math functions.
       - [x] Add.
       - [x] Subtract.
       - [x] Multiplication.
       - [x] Divide.
  - [] Take input from the user for an list of numbers.
  - [] Ask the user to Select the operation.
  - [] Print out calulation.
  - [] Check if user wants another calculation and close if answer is no.
"""

import time

# This function returns two args for addition.
def addition(first, second):
  return first + second

# This function returns two args for subtraction.
def subtraction(first, second):
  return first - second

# This function returns two args for division.
def division(first, second):
  return first / second

# This function returns two args for multiplication.
def multiplication(first, second):
  return first * second

# While the condition is met it checks the choice is one of the four options.
while True:
  
  print("Welcome to Bot World Calulator")
  
  time.sleep(0.500)

  print("Please Select Math Operator")

  user_choice = int( input("Enter a number 1 / 2 /3 / 4 / 5: ")  )

  if user_choice == 1:
    print("You have selected addition")
  elif user_choice == 2:
    print("You have selected subtraction")
  elif user_choice == 3:
    print("You have selected division")
  elif user_choice == 4:
    print("You have selected multiplication")
  elif user_choice == 5:
    break

  break

else: 
  print("Invalid Input")