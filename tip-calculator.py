"""
 - [x] Create a generic greeting to welcome the customer.
 - [x] Make an array of items for the shop.
 - [] Display a terminal menu for customer to make a decision so they don't have to type in anything. If the decision is making is too long quit program.
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

# Opening JSON file
# f = open('data.json')

def introduction():
  print("Hello Welcome To Bot-World!")
  name = input("Can I ask you for your name?")
  print("Nice to meet you", name)
  time.sleep(0.400)
  print("Bot: What can I get for you today? ", name)
introduction()

def customer():
  print("Customer: Nice to meet you too Bot. ")
  oreder = input("Customer: Could I get? ")
customer()