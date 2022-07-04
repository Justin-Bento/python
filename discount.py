"""
  Create a function in Python that accepts two parameters.
  The first should be the full price of an item as an integer.
  The second should be the discount percentage as an integer.
  The function should return the price of the item after the discount has been applied.
  For example, if the price is 100 and the discount is 20, the function should return 80.
"""

def grand_total():
    global total
    total = input("What is the total for groceries amount after tax? \n")
    print(f'The grand total is: {total}$')
grand_total()

def sale_price():
    sale = input("Was there any sale today? \n")
    if sale in [True, "Yes", "yes"]:
        discount = input("What is the discount for groceries after tax? \n")
        print(f'The discount is: {discount}%')
        result = float(total) / float(discount)
        print(f'Your new total is: {result}$')
    else:
        print(f'Your total is stil: {total}$')
sale_price()