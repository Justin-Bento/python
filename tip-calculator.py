"""
 - [x] Create a generic greeting to welcome the customer.
 - [x] Make an array of items for the shop.
 - [x] Display a terminal menu for customer to make a decision so they don't have to type in anything. If the decision is making is too long quit program.
 - [x] Mention the price and ask how would the customer like to pay. only accept intergers or floats.
 - [x] Wait to see how the customer would like to pay and then include the total after tax.
 - [x] Create a function to calculate the customers cash amount after paying.
 - [x] Display the final price before and after tax.
 - [x] Even out transaction if customer pays by card.
 - [] Retun additional change during the transaction if customer pays by cash.
 - [] Create a generic greeting to thank the customer.
 """

# imported timer, json and Simple Terminal modules
from math import prod
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
    str(results['house_favourites'][0]['title']),
    str(results['house_favourites'][1]['title']),
    str(results['house_favourites'][2]['title']),
    str(results['house_favourites'][3]['title']),
    str(results['house_favourites'][4]['title']),
    str(results['off_the_grill'][0]['title']),
    str(results['off_the_grill'][1]['title']),
    str(results['off_the_grill'][2]['title']),
    str(results['off_the_grill'][3]['title']),
    str(results['off_the_grill'][4]['title']),
    str(results['off_the_grill'][5]['title']),
    str(results['off_the_grill'][6]['title']),
    str(results['off_the_grill'][7]['title']),
    str(results['off_the_grill'][8]['title']),
    str(results['sandwiches_and_poboys'][0]['title']),
    str(results['sandwiches_and_poboys'][1]['title']),
    str(results['sandwiches_and_poboys'][2]['title']),
    str(results['sandwiches_and_poboys'][3]['title']),
    str(results['sandwiches_and_poboys'][4]['title']),
    str(results['sandwiches_and_poboys'][5]['title']),
    str(results['sandwiches_and_poboys'][6]['title']),
    str(results['sandwiches_and_poboys'][7]['title']),
    str(results['sandwiches_and_poboys'][8]['title']),
    str(results['sandwiches_and_poboys'][9]['title']),
    str(results['sandwiches_and_poboys'][10]['title']),
    str(results['sandwiches_and_poboys'][11]['title']),
    str(results['sandwiches_and_poboys'][12]['title']),
    str(results['sandwiches_and_poboys'][13]['title']),
    str(results['sandwiches_and_poboys'][14]['title']),
    str(results['fish_fry'][0]['title']),
    str(results['fish_fry'][1]['title']),
    str(results['fish_fry'][2]['title']),
    str(results['fish_fry'][3]['title']),
    str(results['fish_fry'][4]['title']),
    str(results['fish_fry'][5]['title']),
    str(results['fish_fry'][6]['title']),
    str(results['fish_fry'][7]['title']),
    str(results['fish_fry'][8]['title']),
    str(results['fish_fry'][9]['title']),
    str(results['soups'][0]['title']),
    str(results['soups'][1]['title']),
    str(results['soups'][2]['title']),
    str(results['soups'][3]['title']),
    str(results['soups'][4]['title']),
    str(results['soups'][5]['title']),
    str(results['on_their_own'][0]['title']),
    str(results['on_their_own'][1]['title']),
    str(results['on_their_own'][2]['title']),
    str(results['salads'][0]['title']),
    str(results['salads'][1]['title']),
    str(results['salads'][2]['title']),
    str(results['salads'][3]['title']),
    str(results['salads'][4]['title']),
    str(results['salads'][5]['title']),
]
resturant_price = [
    str(results['house_favourites'][0]['price']),
    str(results['house_favourites'][1]['price']),
    str(results['house_favourites'][2]['price']),
    str(results['house_favourites'][3]['price']),
    str(results['house_favourites'][4]['price']),
    str(results['off_the_grill'][0]['price']),
    str(results['off_the_grill'][1]['price']),
    str(results['off_the_grill'][2]['price']),
    str(results['off_the_grill'][3]['price']),
    str(results['off_the_grill'][4]['price']),
    str(results['off_the_grill'][5]['price']),
    str(results['off_the_grill'][6]['price']),
    str(results['off_the_grill'][7]['price']),
    str(results['off_the_grill'][8]['price']),
    str(results['sandwiches_and_poboys'][0]['price']),
    str(results['sandwiches_and_poboys'][1]['price']),
    str(results['sandwiches_and_poboys'][2]['price']),
    str(results['sandwiches_and_poboys'][3]['price']),
    str(results['sandwiches_and_poboys'][4]['price']),
    str(results['sandwiches_and_poboys'][5]['price']),
    str(results['sandwiches_and_poboys'][6]['price']),
    str(results['sandwiches_and_poboys'][7]['price']),
    str(results['sandwiches_and_poboys'][8]['price']),
    str(results['sandwiches_and_poboys'][9]['price']),
    str(results['sandwiches_and_poboys'][10]['price']),
    str(results['sandwiches_and_poboys'][11]['price']),
    str(results['sandwiches_and_poboys'][12]['price']),
    str(results['sandwiches_and_poboys'][13]['price']),
    str(results['sandwiches_and_poboys'][14]['price']),
    str(results['fish_fry'][0]['price']),
    str(results['fish_fry'][1]['price']),
    str(results['fish_fry'][2]['price']),
    str(results['fish_fry'][3]['price']),
    str(results['fish_fry'][4]['price']),
    str(results['fish_fry'][5]['price']),
    str(results['fish_fry'][6]['price']),
    str(results['fish_fry'][7]['price']),
    str(results['fish_fry'][8]['price']),
    str(results['fish_fry'][9]['price']),
    str(results['soups'][0]['price']),
    str(results['soups'][1]['price']),
    str(results['soups'][2]['price']),
    str(results['soups'][3]['price']),
    str(results['soups'][4]['price']),
    str(results['soups'][5]['price']),
    str(results['on_their_own'][0]['price']),
    str(results['on_their_own'][1]['price']),
    str(results['on_their_own'][2]['price']),
    str(results['salads'][0]['price']),
    str(results['salads'][1]['price']),
    str(results['salads'][2]['price']),
    str(results['salads'][3]['price']),
    str(results['salads'][4]['price']),
    str(results['salads'][5]['price']),
]

def resturant_menu():
   for items in range(0, 52):
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

    # Card transaction would even out the payment and the time simulates a customer entering details.
    def card_transaction():
        print(f"Bot: You selected {customer_selection_payment}. :)")
        time.sleep(0.800)
        print(f"Bot: Your {customer_selection_payment} transaction was successful. :)")
        time.sleep(0.800)
        print(f"Bot: Thank you for ordering at Bot World. :)")

    # Cash transaction handles the amount of cash given and returns the exact amount.
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
    def no_transaction():
        pass

    if customer_selection_payment == payment_options[0]:
        card_transaction()
    elif customer_selection_payment == payment_options[1]:
        card_transaction()
    elif customer_selection_payment == payment_options[2]:
        cash_transaction()
    else:
        no_transaction()

if __name__ == "__main__":
    main()