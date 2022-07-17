"""
 - [x] Create a generic greeting to welcome the customer.
 - [x] Make an array of items for the shop.
 - [x] Display a terminal menu for customer to make a decision so they don't have to type in anything. If the decision is making is too long quit program.
 - [x] Mention the price and ask how would the customer like to pay. only accept intergers or floats.
 - [x] Wait to see how the customer would like to pay and then include the total after tax.
 - [] Create a function to calculate the customers cash amount after paying.
 - [] Ask if they would like to include a tip. -- If they do give a percentage and include a new price, if not move onto next step.
 - [] Make a generic greeting to the customer for purchasing at store.
 - [] Exit program.
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

ResturantTitle = [
    f"{str(results['house_favourites'][0]['title'])}",
    f"{str(results['house_favourites'][1]['title'])}",
    f"{str(results['house_favourites'][2]['title'])}",
    f"{str(results['house_favourites'][3]['title'])}",
    f"{str(results['house_favourites'][4]['title'])}",
    f"{str(results['off_the_grill'][0]['title'])}",
    f"{str(results['off_the_grill'][1]['title'])}",
    f"{str(results['off_the_grill'][2]['title'])}",
    f"{str(results['off_the_grill'][3]['title'])}",
    f"{str(results['off_the_grill'][4]['title'])}",
    f"{str(results['off_the_grill'][5]['title'])}",
    f"{str(results['off_the_grill'][6]['title'])}",
    f"{str(results['off_the_grill'][7]['title'])}",
    f"{str(results['off_the_grill'][8]['title'])}",
    f"{str(results['sandwiches_and_poboys'][0]['title'])}",
    f"{str(results['sandwiches_and_poboys'][1]['title'])}",
    f"{str(results['sandwiches_and_poboys'][2]['title'])}",
    f"{str(results['sandwiches_and_poboys'][3]['title'])}",
    f"{str(results['sandwiches_and_poboys'][4]['title'])}",
    f"{str(results['sandwiches_and_poboys'][5]['title'])}",
    f"{str(results['sandwiches_and_poboys'][6]['title'])}",
    f"{str(results['sandwiches_and_poboys'][7]['title'])}",
    f"{str(results['sandwiches_and_poboys'][8]['title'])}",
    f"{str(results['sandwiches_and_poboys'][9]['title'])}",
    f"{str(results['sandwiches_and_poboys'][10]['title'])}",
    f"{str(results['sandwiches_and_poboys'][11]['title'])}",
    f"{str(results['sandwiches_and_poboys'][12]['title'])}",
    f"{str(results['sandwiches_and_poboys'][13]['title'])}",
    f"{str(results['sandwiches_and_poboys'][14]['title'])}",
    f"{str(results['fish_fry'][0]['title'])}",
    f"{str(results['fish_fry'][1]['title'])}",
    f"{str(results['fish_fry'][2]['title'])}",
    f"{str(results['fish_fry'][3]['title'])}",
    f"{str(results['fish_fry'][4]['title'])}",
    f"{str(results['fish_fry'][5]['title'])}",
    f"{str(results['fish_fry'][6]['title'])}",
    f"{str(results['fish_fry'][7]['title'])}",
    f"{str(results['fish_fry'][8]['title'])}",
    f"{str(results['fish_fry'][9]['title'])}",
    f"{str(results['soups'][0]['title'])}",
    f"{str(results['soups'][1]['title'])}",
    f"{str(results['soups'][2]['title'])}",
    f"{str(results['soups'][3]['title'])}",
    f"{str(results['soups'][4]['title'])}",
    f"{str(results['soups'][5]['title'])}",
    f"{str(results['on_their_own'][0]['title'])}",
    f"{str(results['on_their_own'][1]['title'])}",
    f"{str(results['on_their_own'][2]['title'])}",
    f"{str(results['salads'][0]['title'])}",
    f"{str(results['salads'][1]['title'])}",
    f"{str(results['salads'][2]['title'])}",
    f"{str(results['salads'][3]['title'])}",
    f"{str(results['salads'][4]['title'])}",
    f"{str(results['salads'][5]['title'])}",
]
ResturantPrice = [
    f"{str(results['house_favourites'][0]['price'])}",
    f"{str(results['house_favourites'][1]['price'])}",
    f"{str(results['house_favourites'][2]['price'])}",
    f"{str(results['house_favourites'][3]['price'])}",
    f"{str(results['house_favourites'][4]['price'])}",
    f"{str(results['off_the_grill'][0]['price'])}",
    f"{str(results['off_the_grill'][1]['price'])}",
    f"{str(results['off_the_grill'][2]['price'])}",
    f"{str(results['off_the_grill'][3]['price'])}",
    f"{str(results['off_the_grill'][4]['price'])}",
    f"{str(results['off_the_grill'][5]['price'])}",
    f"{str(results['off_the_grill'][6]['price'])}",
    f"{str(results['off_the_grill'][7]['price'])}",
    f"{str(results['off_the_grill'][8]['price'])}",
    f"{str(results['sandwiches_and_poboys'][0]['price'])}",
    f"{str(results['sandwiches_and_poboys'][1]['price'])}",
    f"{str(results['sandwiches_and_poboys'][2]['price'])}",
    f"{str(results['sandwiches_and_poboys'][3]['price'])}",
    f"{str(results['sandwiches_and_poboys'][4]['price'])}",
    f"{str(results['sandwiches_and_poboys'][5]['price'])}",
    f"{str(results['sandwiches_and_poboys'][6]['price'])}",
    f"{str(results['sandwiches_and_poboys'][7]['price'])}",
    f"{str(results['sandwiches_and_poboys'][8]['price'])}",
    f"{str(results['sandwiches_and_poboys'][9]['price'])}",
    f"{str(results['sandwiches_and_poboys'][10]['price'])}",
    f"{str(results['sandwiches_and_poboys'][11]['price'])}",
    f"{str(results['sandwiches_and_poboys'][12]['price'])}",
    f"{str(results['sandwiches_and_poboys'][13]['price'])}",
    f"{str(results['sandwiches_and_poboys'][14]['price'])}",
    f"{str(results['fish_fry'][0]['price'])}",
    f"{str(results['fish_fry'][1]['price'])}",
    f"{str(results['fish_fry'][2]['price'])}",
    f"{str(results['fish_fry'][3]['price'])}",
    f"{str(results['fish_fry'][4]['price'])}",
    f"{str(results['fish_fry'][5]['price'])}",
    f"{str(results['fish_fry'][6]['price'])}",
    f"{str(results['fish_fry'][7]['price'])}",
    f"{str(results['fish_fry'][8]['price'])}",
    f"{str(results['fish_fry'][9]['price'])}",
    f"{str(results['soups'][0]['price'])}",
    f"{str(results['soups'][1]['price'])}",
    f"{str(results['soups'][2]['price'])}",
    f"{str(results['soups'][3]['price'])}",
    f"{str(results['soups'][4]['price'])}",
    f"{str(results['soups'][5]['price'])}",
    f"{str(results['on_their_own'][0]['price'])}",
    f"{str(results['on_their_own'][1]['price'])}",
    f"{str(results['on_their_own'][2]['price'])}",
    f"{str(results['salads'][0]['price'])}",
    f"{str(results['salads'][1]['price'])}",
    f"{str(results['salads'][2]['price'])}",
    f"{str(results['salads'][3]['price'])}",
    f"{str(results['salads'][4]['price'])}",
    f"{str(results['salads'][5]['price'])}",
]

# Function that displays a terminal menu.
def main():
    # list of options inside the menu.
    options = [
      ResturantTitle[0],
      ResturantTitle[1],
      ResturantTitle[2],
      ResturantTitle[3],
      ResturantTitle[4],
      ResturantTitle[5],
      ResturantTitle[6],
      ResturantTitle[7],
      ResturantTitle[8],
      ResturantTitle[9],
      ResturantTitle[10],
      ResturantTitle[11],
      ResturantTitle[12],
      ResturantTitle[13],
      ResturantTitle[14],
      ResturantTitle[15],
      ResturantTitle[16],
      ResturantTitle[17],
      ResturantTitle[18],
      ResturantTitle[19],
      ResturantTitle[20],
      ResturantTitle[21],
      ResturantTitle[22],
      ResturantTitle[23],
      ResturantTitle[24],
      ResturantTitle[25],
      ResturantTitle[26],
      ResturantTitle[27],
      ResturantTitle[28],
      ResturantTitle[29],
      ResturantTitle[30],
      ResturantTitle[31],
      ResturantTitle[32],
      ResturantTitle[33],
      ResturantTitle[34],
      ResturantTitle[35],
      ResturantTitle[36],
      ResturantTitle[37],
      ResturantTitle[38],
      ResturantTitle[39],
      ResturantTitle[40],
      ResturantTitle[41],
      ResturantTitle[42],
      ResturantTitle[43],
      ResturantTitle[44],
      ResturantTitle[45],
      ResturantTitle[46],
      ResturantTitle[47],
      ResturantTitle[48],
      ResturantTitle[49],
      ResturantTitle[50],
      ResturantTitle[51],
      ResturantTitle[52],
      ResturantTitle[52],
    ]

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

    if customer_selection_payment == payment_options[0]:
        card_transaction()
    elif customer_selection_payment == payment_options[1]:
        card_transaction()
    elif customer_selection_payment == payment_options[2]:
        pass
    else:
        pass

if __name__ == "__main__":
    main()