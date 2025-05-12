'''
Recap - Shopping Cart Errors

Challenge

Medium
Create a program that simulates a shopping cart with error handling. Your task is to:

Create a function called handle_shopping_cart that processes customer orders
The function should accept a list of order strings in the format "item:quantity"
Process each order by:
Splitting the input string to get the item and quantity
Converting the quantity to an integer
Adding the item to a shopping cart dictionary with the quantity as value
If an item already exists in the cart, update its quantity
Handle these specific errors:
If the input format is incorrect (missing colon), print "Invalid format: {order}"
If the quantity is not a valid number, print "Invalid quantity: {order}"
If the quantity is negative, print "Negative quantity not allowed: {order}"
Return the completed shopping cart dictionary
'''

def handle_shopping_cart(orders):
    # Create an empty dictionary for the shopping cart
    cart = {}
    # Process each order in the list
    for order in orders:
        try:
        # Split the order and add to cart
            value = order.split(":")
            if int(value[1]) < 0:
                print(f"Negative quantity not allowed: {order}")
            elif value[0] in cart:
                cart[value[0]] = cart[value[0]] + int(value[1])
            else:
                cart[value[0]] = int(value[1])
        # Handle potential errors
        except ValueError:
        # Handle value errors
            print(f"Invalid quantity: {order}")
        except Exception as e:
    # Handle unexpected errors
            print(f"Invalid format: {order}")
    # Return the completed cart
    return cart

orders = ["apple:3","banana:2","milk:5"]
print(handle_shopping_cart(orders))

'''
test 1
["apple:3","banana:2","milk:5"]

{'apple': 3, 'banana': 2, 'milk': 5}

test 2
["bread:2","banana:five","eggs:10"]

Invalid quantity: banana:five
{'bread': 2, 'eggs': 10}

test 3
["chocolate:-5","yogurt:3","milk:2"]

Negative quantity not allowed: chocolate:-5
{'yogurt': 3, 'milk': 2}
'''