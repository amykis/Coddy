'''
What To Buy

Challenge Medium

Write a program that receives three inputs (given):

 A list of prices
A list of item names
A budget per item


The program should print:

A list of items that you can afford within your budget
How much budget would you need if you bought all of the affordable items
How many items you couldn't afford
Check the test cases for the output format
'''

prices = input().split(",")
for i in range(len(prices)):
    prices[i] = int(prices[i])
items = input().split(",")
budget_per_item = int(input())

affordable_items = []
cant_afford = 0
total_needed = 0


# Write your code below




print("Can buy:", affordable_items)
print("Total budget needed:", total_needed)
print("Can't afford:", cant_afford)
