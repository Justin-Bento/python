"""
  - [x] Program make a simple calculator.
  - [x] Creat a function to handle these math functions.
       - [x] Add.
       - [x] Subtract.
       - [x] Multiplication.
       - [x] Divide.
  - [x] Take input from the user for an list of numbers.
  - [x] Ask the user to Select the operation.
  - [x] Print out calulation.
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

  if user_choice in ( 1 , 2 , 3 , 4):

    first_number = float( input("Enter a first number: ")  )
    second_number = float( input("Enter a second number: ")  )

    # If the users enters 1 it will do addition.
    if user_choice == 1:
      print("You have selected addition")
      print( f"{ first_number } + { second_number } = { addition(first_number, second_number) }" )

    # If the users enters 2 it will do subtraction.
    elif user_choice == 2:
      print("You have selected subtraction")
      print( f"{ first_number } - { second_number } = { subtraction(first_number, second_number) }" )

    # If the users enters 3 it will do division.
    elif user_choice == 3:
      print("You have selected division")
      print( f"{ first_number } / { second_number } = { division(first_number, second_number) }" )

    # If the users enters 4 it will do multiplication.
    elif user_choice == 4:
      print("You have selected multiplication")
      print( f"{ first_number } * { second_number } = { multiplication(first_number, second_number) }" )

  # If the users enters 5 it will close the loop.
  if user_choice in ( 5, 6, 7, 8, 9, 0 ):
    print("Have a great day")
    break

  # Closes the loop.
  break

else: 
  print("Invalid Input")