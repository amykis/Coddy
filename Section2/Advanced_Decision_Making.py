'''
You are given a list of product names and a dictionary of product quantities for a grocery store.
Write a function named check_inventory that takes two parameters: products (a list) and quantities (a dictionary).
The function should perform the following checks:

Check if 'Apples' is in the product list.
Check if 'Oranges' is not in the product list.
Check if 'Bananas' is in the quantities dictionary.
Check if 'Grapes' is not in the quantities dictionary.
For each check, print an appropriate message as shown in the test cases.
'''

def check_inventory(products, quantities):
    # Write code here
    print("Apples are in stock.") if "Apples" in products else None
    print("Oranges are not in stock.") if "Oranges" not in products else None
    print("Bananas quantity is tracked.") if "Bananas" in quantities else None
    print("Grapes quantity is not tracked.") if "Grapes" not in quantities else None


product = ["Apples", "Bananas", "Milk", "Bread", "Eggs"]
quantities = {"Bananas": 30, "Milk": 10, "Bread": 20}

check_inventory(product, quantities)