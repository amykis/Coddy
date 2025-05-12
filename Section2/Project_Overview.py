'''
Project Overview

The Inventory Management System helps manage a store's inventory by adding items,
updating stock, checking availability, and generating sales reports.
It integrates dictionaries for structured data, error handling for invalid inputs,
and logic operations for decision-making, making it a comprehensive and practical project.

Challenge task4

Create a function named check_availability that takes one argument: item (string). The function should:

Check if the item exists in the inventory dictionary.
If it does not exist, return "Item not found".
If the item exists, return the current stock of the item.
Add (replace) the following block of code at the bottom of your code:

add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
update_stock("Apple", -20)
update_stock("Banana", 30)
print(check_availability("Apple"))  # Should return 80
print(check_availability("Banana"))  # Should return 80
print(check_availability("Orange"))  # Should return "
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


def check_availability(item):
    if item in inventory:
        return inventory[item]["stock"]
    else:
        return "Item not found"


inventory = {}

add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
update_stock("Apple", -20)
update_stock("Banana", 30)
print(check_availability("Apple"))  # Should return 80
print(check_availability("Banana"))  # Should return 80
print(check_availability("Orange"))  # Should return "


'''
Item 'Apple' added successfully.
Item 'Banana' added successfully.
Stock for 'Apple' updated successfully.
Stock for 'Banana' updated successfully.
80
80
Item not found
'''