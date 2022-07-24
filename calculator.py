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
  - [x] Check if user wants another calculation and close if answer is no.
"""

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

  # Shows users what infromation you can put in.
  print("Please Select Operator: addition, subtraction, division, mulitplication")

  # Collects a number the user selected .
  user_choice = int( input("Enter a number from 1 to 4: ")  )

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

  # Closes the loop if the user selects no.
  calculation = input("Another calculation? (y/n): ")
  if calculation == "n":
    break

# When entering anything else the loop should return invalid input.
else: 
  print("Invalid Input")