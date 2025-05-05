'''
You are given a list of names and a dictionary of student grades. Write a program that:

Checks if the name "Alice" is in the list.
Checks if the name "David" is not in the list.
Checks if the key "Bob" exists in the dictionary.
Checks if the key "Eve" does not exist in the dictionary.
'''

# Given data
names = ["Alice", "Bob", "Charlie"]
grades = {"Alice": 85, "Bob": 90, "Charlie": 78}

# Write code here
print('Alice is in the list.') if "Alice" in names else None
print('David is not in the list.') if "David" not in names else None
print('Bob is in the dictionary.') if "Bob" in grades else None
print('Eve is not in the dictionary.') if "Eve" not in grades else None