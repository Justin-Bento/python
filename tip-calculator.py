"""
 - [x] Create a generic greeting to welcome the customer.
 - [] Make an array of items for the shop.
 - [] Wait for customer to make a decision.
 - [] Mention the price and ask how would the customer like to pay. only accept intergers or floats.
 - [] Wait to see how the customer would like to pay and then include the total after tax.
 - [] Create a function to calculate the customers cash amount after paying.
 - [] Ask if they would like to include a tip. -- If they do give a percentage and include a new price, if not move onto next step.
 - [] Make a generic greeting to the customer for purchasing at store.
 - [] Exit program.
 """

# imported timer module to sleep on final greeting
import time

def introduction():
 print("Hello Welcome To Bot-World!")
 name = input("Can I ask you for your name?")
 print("Nice to meet you", name)
 time.sleep(1)
 print("Bot: What can I get for you today? ", name)
introduction()
