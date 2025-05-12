'''
Project Overview

The Inventory Management System helps manage a store's inventory by adding items,
updating stock, checking availability, and generating sales reports.
It integrates dictionaries for structured data, error handling for invalid inputs,
and logic operations for decision-making, making it a comprehensive and practical project.

Challenge task2

Easy
Create a function named add_item that takes three arguments: item (string), price (float), and stock (int). The function should:

Check if the item already exists in the inventory dictionary.
If it does, print "Error: Item '<item>' already exists.".
If the item does not exist, add it to the inventory with the provided price and stock.
Store the price as a float and the stock as an integer.
Print "Item '<item>' added successfully.".
Add (replace) the following block of code at the bottom of your code:

add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
add_item("Apple", 0.6, 30)  # Should print an error
print(inventory)
'''

def add_item(item, price, stock):
    if item in inventory:
        print(f"Error: Item '{item}' already exists.")
    else:
        inventory[item] = {"price": float(price), "stock": int(stock)}
        print(f"Item '{item}' added successfully.")


inventory = {}

add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
add_item("Apple", 0.6, 30)  # Should print an error
print(inventory)


'''
Item 'Apple' added successfully.
Item 'Banana' added successfully.
Error: Item 'Apple' already exists.
{'Apple': {'price': 0.5, 'stock': 100}, 'Banana': {'price': 0.2, 'stock': 50}}
'''