'''
Project Overview

The Inventory Management System helps manage a store's inventory by adding items,
updating stock, checking availability, and generating sales reports.
It integrates dictionaries for structured data, error handling for invalid inputs,
and logic operations for decision-making, making it a comprehensive and practical project.

Challenge task3

Easy
Create a function named update_stock that takes two arguments: item (string) and quantity (int). The function should:

Check if the item exists in the inventory dictionary.
If it does not exist, print "Error: Item '<item>' not found.".
If the item exists, calculate the new stock by adding the quantity to the current stock.
If the new stock is negative, print "Error: Insufficient stock for '<item>'." and do not update.
Otherwise, update the stock in the inventory.
Print "Stock for '<item>' updated successfully.".

Add (replace) the following block of code at the bottom of your code:
add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
add_item("Apple", 0.6, 30)  # Should print an error
update_stock("Apple", -20)
update_stock("Banana", 30)
update_stock("Orange", 10)  # Should print an error
update_stock("Apple", -90)
print(inventory)
'''

def add_item(item, price, stock):
    if item in inventory:
        print(f"Error: Item '{item}' already exists.")
    else:
        inventory[item] = {"price": float(price), "stock": int(stock)}
        print(f"Item '{item}' added successfully.")


def update_stock(item, quantity):
    if item not in inventory:
        print(f"Error: Item '{item}' not found.")
    elif inventory[item]["stock"] + quantity < 0:
        print(f"Error: Insufficient stock for '{item}'.")
    else:
        inventory[item]["stock"] += quantity
        print(f"Stock for '{item}' updated successfully.")



inventory = {}

add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
add_item("Apple", 0.6, 30)  # Should print an error
update_stock("Apple", -20)
update_stock("Banana", 30)
update_stock("Orange", 10)  # Should print an error
update_stock("Apple", -90)
print(inventory)


'''
Item 'Apple' added successfully.
Item 'Banana' added successfully.
Error: Item 'Apple' already exists.
Stock for 'Apple' updated successfully.
Stock for 'Banana' updated successfully.
Error: Item 'Orange' not found.
Error: Insufficient stock for 'Apple'.
{'Apple': {'price': 0.5, 'stock': 80}, 'Banana': {'price': 0.2, 'stock': 80}}
'''