"""
 - [x] Create a generic greeting to welcome the customer.
 - [x] Make an array of items for the shop.
 - [x] Display a terminal menu for customer to make a decision so they don't have to type in anything. If the decision is making is too long quit program.
 - [x] Mention the price and ask how would the customer like to pay. only accept intergers or floats.
 - [x] Wait to see how the customer would like to pay and then include the total after tax.
 - [x] Create a function to calculate the customers cash amount after paying.
 - [x] Display the final price before and after tax.
 - [x] Even out transaction if customer pays by card.
 - [x] Retun additional change during the transaction if customer pays by cash.
 - [x] Create a generic greeting to thank the customer.
 """

# imported timer, json and Simple Terminal modules
import time
import json
from simple_term_menu import TerminalMenu


# Warm greeting to store.
print("Hello Welcome To Bot-World!")

# Askes for your name to make things personal.
user_name = input("Can I ask you for your name? ")
print(f"Nice to meet you {user_name}")

# Wait a while for orders.
time.sleep(0.400)

# Asks customer what they would like to order.
print(f"Bot: What can I get for you today? {user_name}")
print("Customer: Nice to meet you too Bot. Could I get? ")

# Fetch local json file that holds busters sea cove menu.
with open('assets/busters_sea_cove_menu.json', 'r') as myfile:
    data = myfile.read()
results = json.loads(data)

resturant_title = [
    str(results[0]['title']),
    str(results[1]['title']),
    str(results[2]['title']),
    str(results[3]['title']),
    str(results[4]['title']),
    str(results[5]['title']),
    str(results[6]['title']),
    str(results[7]['title']),
    str(results[8]['title']),
    str(results[9]['title']),
    str(results[10]['title']),
    str(results[11]['title']),
    str(results[12]['title']),
    str(results[13]['title']),
    str(results[14]['title']),
    str(results[15]['title']),
    str(results[16]['title']),
    str(results[17]['title']),
    str(results[18]['title']),
    str(results[19]['title']),
    str(results[20]['title']),
    str(results[21]['title']),
    str(results[22]['title']),
    str(results[23]['title']),
    str(results[24]['title']),
    str(results[25]['title']),
    str(results[25]['title']),
    str(results[26]['title']),
    str(results[27]['title']),
    str(results[28]['title']),
    str(results[29]['title']),
    str(results[30]['title']),
    str(results[31]['title']),
    str(results[32]['title']),
    str(results[33]['title']),
    str(results[34]['title']),
    str(results[35]['title']),
    str(results[36]['title']),
    str(results[37]['title']),
    str(results[38]['title']),
    str(results[39]['title']),
    str(results[40]['title']),
    str(results[41]['title']),
    str(results[42]['title']),
    str(results[43]['title']),
    str(results[44]['title']),
    str(results[45]['title']),
    str(results[46]['title']),
    str(results[47]['title']),
    str(results[48]['title']),
    str(results[49]['title']),
    str(results[50]['title']),
    str(results[51]['title']),
    str(results[52]['title']),
]
resturant_price = [
    str(results[0]['price']),
    str(results[1]['price']),
    str(results[2]['price']),
    str(results[3]['price']),
    str(results[4]['price']),
    str(results[5]['price']),
    str(results[6]['price']),
    str(results[7]['price']),
    str(results[8]['price']),
    str(results[9]['price']),
    str(results[10]['price']),
    str(results[11]['price']),
    str(results[12]['price']),
    str(results[13]['price']),
    str(results[14]['price']),
    str(results[15]['price']),
    str(results[16]['price']),
    str(results[17]['price']),
    str(results[18]['price']),
    str(results[19]['price']),
    str(results[20]['price']),
    str(results[21]['price']),
    str(results[22]['price']),
    str(results[23]['price']),
    str(results[24]['price']),
    str(results[25]['price']),
    str(results[25]['price']),
    str(results[26]['price']),
    str(results[27]['price']),
    str(results[28]['price']),
    str(results[29]['price']),
    str(results[30]['price']),
    str(results[31]['price']),
    str(results[32]['price']),
    str(results[33]['price']),
    str(results[34]['price']),
    str(results[35]['price']),
    str(results[36]['price']),
    str(results[37]['price']),
    str(results[38]['price']),
    str(results[39]['price']),
    str(results[40]['price']),
    str(results[41]['price']),
    str(results[42]['price']),
    str(results[43]['price']),
    str(results[44]['price']),
    str(results[45]['price']),
    str(results[46]['price']),
    str(results[47]['price']),
    str(results[48]['price']),
    str(results[49]['price']),
    str(results[50]['price']),
    str(results[51]['price']),
    str(results[52]['price']),
]

# Loops and return the info inside restutrant_title array.
def resturant_menu():
   for items in range(52):
       resturant_title[items]
   return resturant_title

# Function that displays a terminal menu.
def main():
    # list of options inside the menu.
    options = resturant_menu()

    # title for the temrinial menu.
    terminal_menu = TerminalMenu(options, title="Busters Sea Cove Menu")
    menu_entry_index = terminal_menu.show()
    customer_selection = options[menu_entry_index]

    # Calculates the produt price's after HST tax 13%.
    def sales_tax(product, price):
      return print( f"Bot: Your new total comes to {product} is {float(price) * float(1.13)}" ) 

    # Says the product a user selected and outputs the new price after tax.
    print(f"Bot: One {customer_selection} for {user_name}!")

    # Wait for asking payment.
    time.sleep(0.800)

    # list of payment options inside the menu
    payment_options = [ "Credit", "Debit", "Cash" ]

    # Created a new menu with the title.
    terminal_menu_payment = TerminalMenu(payment_options, title="How Would you like to pay?")
    
    # added show command to update payment.
    menu_entry_index_payment = terminal_menu_payment.show()

    # added a selection to grab user selection 
    customer_selection_payment = payment_options[menu_entry_index_payment]

    # Card transaction would even out the payment.
    def card_transaction():
        print(f"Bot: You selected {customer_selection_payment}. :)")
        time.sleep(0.800)
        print(f"Bot: Your {customer_selection_payment} transaction was successful. :)")
        time.sleep(0.800)
        print(f"Bot: Thank you for ordering at Bot World. :)")

    # Card transaction would return the cash and output final payment.
    def cash_transaction():
        print(f"Bot: You selected {customer_selection_payment}.")
        time.sleep(0.800)
        cash_amount = float(input("Enter number : "))
        if float( cash_amount ) < float( resturant_price[0] ):
            return cash_transaction()
        else:
            grand_total = cash_amount - float( resturant_price[0] )
            print( f"Your Final Amount is {grand_total}" )
            print( f"Bot: Thanks for ordering at Bot World" )

    # No transaction that takes place for 10s the program will quit.
    def lengthy_transaction():
        pass

    # If a customer pays credit transaction will even out.
    if customer_selection_payment == payment_options[0]:
        card_transaction()
    # If a customer pays debit transaction will even out.
    elif customer_selection_payment == payment_options[1]:
        card_transaction()
    # If a customer pays cash it will give cash back.
    elif customer_selection_payment == payment_options[2]:
        cash_transaction()
    # Else if the transaction takes too long the program will end.
    else:
        lengthy_transaction()

if __name__ == "__main__":
    main()