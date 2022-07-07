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

bakery = [
  {
    id: 1,
    product: 'Black Forest Ham',
    price: 9.70,
  },
  {
    id: 2,
    product: 'bacon, lettuce, and tomato',
    price: 9.95,
  },
  {
    id: 3,
    product: 'Roast Beef or Turkey',
    price: 9.70,
  },
  {
    id: 4,
    product: 'Tuna Salad',
    price: 9.70,
  },
  {
    id: 5,
    product: 'Egg Salad',
    price: 8.90,
  },
  {
    id: 6,
    product: 'Swis Or Chedder Cheese',
    price: 8.60,
  },
  {
    id: 7,
    product: 'Brie',
    price: 9.75,
  },
  {
    id: 8,
    product: 'Grilled Vegtables',
    price: 9.25
  },
  {
    id: 9,
    product: 'Garden Vegtables',
    price: 7.25
  },
  {
    id: 10,
    product: 'Bagel With Cheese Sandwitch',
    price: 7.50,
  },
  {
    id: 11,
    product: 'Bagel & Butter',
    price: 2.55,
  },
  {
    id: 12,
    product: 'Bagel and Cream Cheese',
    price: 4.00,
  },
  {
    id: 13,
    product: 'Bagel With Ham',
    price: 9.70,
  },
  {
    id: 14,
    product: 'Omelette',
    price: 6.95,
  },
  {
    id: 15,
    product: 'Bagel Eggs and Toast',
    price: 5.70,
  }
]

def introduction():
 print("Hello Welcome To Bot-World!")
 name = input("Can I ask you for your name?")
 print("Nice to meet you", name)
 time.sleep(1)
 print("Bot: What can I get for you today? ", name)
introduction()
