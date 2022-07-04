"""
  Create a function in Python that accepts two parameters.
  The first should be the full price of an item as an integer.
  The second should be the discount percentage as an integer.
  The function should return the price of the item after the discount has been applied.
  For example, if the price is 100 and the discount is 20, the function should return 80.
"""

def grand_total():
    # Created a global variable called total.
    global total
      # Added the total as an input to grab and collect the a final price of a receipt. 
    total = input("What is the total for groceries amount after tax? \n")
      # Then printed out the current grand total, to confirm that this is the amount a user inputed.
    print(f'The grand total is: {total}$')
grand_total()

#  Created a seprate function to determin discounts.
def sale_price():
    # If the user says there was a sale it would ask you for the percentage. Eg. a seniors discount in Canada 10%,
    # Then it would output the discount amount notifing the user that it has been stored.
    sale = input("Was there any sale today? \n")
    if sale in [True, "Yes", "yes"]:
        discount = input("What is the discount for groceries after tax? \n")
        print(f'The discount is: {discount}%')
        # A new total would be calculate and printed by dividing the grand_total and sale_percentage the user inputed.
        result = float(total) / float(discount)
        print(f'Your new total is: {result}$')
      # If there was no sale your total would still be the same.
    else:
        print(f'Your total is stil: {total}$')
sale_price()

# This closes the program to ensure nothing is runing.