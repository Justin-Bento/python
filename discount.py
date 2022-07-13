"""
  Create a function in Python that accepts two parameters.
  The first should be the full price of an item as an integer.
  The second should be the discount percentage as an integer.
  The function should return the price of the item after the discount has been applied.
  For example, if the price is 100 and the discount is 20, the function should return 80.
"""

def grand_total():
  # Created a global variable.
  global total
  # Collects the a final price of a receipt.
  total = input("What is the total for groceries amount after tax? \n")
  # Prints out the amount a user inputed.
  print(f'The grand total is: {total}$')
grand_total()

# This function determins discount price.
def sale_price():
  # User Input Verifies if a sale took place,
  sale = input("Was there any sale today? \n")
  # If there was a sale it would output the discount amount.
  if sale in [True, "Yes", "yes"]:
      discount = input("What is the discount for groceries after tax? \n")
      print(f'The discount is: {discount}%')
      # Sale is calculated by dividing the grand_total and sale_percentage the user inputed.
      result = float(total) / float(discount)
      print(f'Your new total is: {result}$')
    # If there was no sale it would output the origional amount.
  else:
      print(f'Your total is stil: {total}$')
sale_price()
