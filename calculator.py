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
  
  # Intoduces user to what the program is supposed to be.
  print("Welcome to Bot World Calculator")
  
  # Stops the next stantement from being used in 0.5s.
  time.sleep(0.500)

  # Shows users what infromation you can put in.
  print("Please Select Math Operator from 1 to 4")

  # Collects a number the user selected .
  user_choice = int( input("Enter a number 1 / 2 /3 / 4 / 5: ")  )

  # If the users enters 1 it will do addition.
  if user_choice == 1:
    print("You have selected addition")
  # If the users enters 2 it will do subtraction.
  elif user_choice == 2:
    print("You have selected subtraction")
  # If the users enters 3 it will do division.
  elif user_choice == 3:
    print("You have selected division")
  # If the users enters 4 it will do multiplication.
  elif user_choice == 4:
    print("You have selected multiplication")
  # If the users enters 5 it will close the loop.
  elif user_choice == 5:
    break

  # Closes the loop.
  break

else: 
  print("Invalid Input")