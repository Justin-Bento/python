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
      f"[1] {str(results['house_favourites'][0]['title'])}",
      f"[2] {str(results['house_favourites'][1]['title'])}",
      f"[3] {str(results['house_favourites'][2]['title'])}",
      f"[4] {str(results['house_favourites'][3]['title'])}",
      f"[5] {str(results['house_favourites'][4]['title'])}",
    ]
    terminal_menu = TerminalMenu(options, title="House Favourites")
    global user_options
    menu_entry_index = terminal_menu.show()
    user_options = options[menu_entry_index]
    print(f"You have selected {user_options}!")

if __name__ == "__main__":
    main()
