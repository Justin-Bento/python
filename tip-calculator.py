"""
 - [x] Create a generic greeting to welcome the customer.
 - [x] Make an array of items for the shop.
 - [x] Display a terminal menu for customer to make a decision so they don't have to type in anything. If the decision is making is too long quit program.
 - [] Mention the price and ask how would the customer like to pay. only accept intergers or floats.
 - [] Wait to see how the customer would like to pay and then include the total after tax.
 - [] Create a function to calculate the customers cash amount after paying.
 - [] Ask if they would like to include a tip. -- If they do give a percentage and include a new price, if not move onto next step.
 - [] Make a generic greeting to the customer for purchasing at store.
 - [] Exit program.
 """

# imported timer module to sleep on final greeting
import time
import json
from simple_term_menu import TerminalMenu

def introduction():
  print("Hello Welcome To Bot-World!")
  name = input("Can I ask you for your name?")
  print(f"Nice to meet you {name}")
  time.sleep(0.400)
  print(f"Bot: What can I get for you today? {name}")
  print("Customer: Nice to meet you too Bot. Could I get? ")
introduction()

with open('assets/busters_sea_cove_menu.json', 'r') as myfile:
    data=myfile.read()
results = json.loads(data)

def main():
    global options
    options = [
      f"{str(results['house_favourites'][0]['title'])}",
      f"{str(results['house_favourites'][1]['title'])}",
      f"{str(results['house_favourites'][2]['title'])}",
      f"{str(results['house_favourites'][3]['title'])}",
      f"{str(results['house_favourites'][4]['title'])}",
      f" ",
      f"{str(results['off_the_grill'][0]['title'])}",
      f"{str(results['off_the_grill'][1]['title'])}",
      f"{str(results['off_the_grill'][2]['title'])}",
      f"{str(results['off_the_grill'][3]['title'])}",
      f"{str(results['off_the_grill'][4]['title'])}",
      f"{str(results['off_the_grill'][5]['title'])}",
      f"{str(results['off_the_grill'][6]['title'])}",
      f"{str(results['off_the_grill'][7]['title'])}",
      f"{str(results['off_the_grill'][8]['title'])}",
      f" ",
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
      f" ",
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
      f" ",
      f"{str(results['soups'][0]['title'])}",
      f"{str(results['soups'][1]['title'])}",
      f"{str(results['soups'][2]['title'])}",
      f"{str(results['soups'][3]['title'])}",
      f"{str(results['soups'][4]['title'])}",
      f"{str(results['soups'][5]['title'])}",
      f" ",
      f"{str(results['on_their_own'][0]['title'])}",
      f"{str(results['on_their_own'][1]['title'])}",
      f"{str(results['on_their_own'][2]['title'])}",
      f" ",
      f"{str(results['salads'][0]['title'])}",
      f"{str(results['salads'][1]['title'])}",
      f"{str(results['salads'][2]['title'])}",
      f"{str(results['salads'][3]['title'])}",
      f"{str(results['salads'][4]['title'])}",
      f"{str(results['salads'][5]['title'])}",
      f" ",
    ]
    terminal_menu = TerminalMenu(options, title="Busters Sea Cove Menu")
    global user_options
    menu_entry_index = terminal_menu.show()
    user_options = options[menu_entry_index]

    if user_options == " ":
      print("Sorry can you try again?")
    elif user_options in options:
      print(f"You ordered {user_options}! Your total would be")
    else:
      print("Have a nice day. :)")

if __name__ == "__main__":
    main()