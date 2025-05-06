'''
Write a function named remove_duplicates that takes a list of numbers as an argument
and returns a new list with duplicates removed while preserving the original order of elements.

Example Input:

numbers = [1, 2, 2, 3, 4, 4, 5]
Example Output:

[1, 2, 3, 4, 5]
Use the properties of sets to simplify your solution while keeping the order intact!
'''

def remove_duplicates(numbers):
    # Write code here
    new_numbers_list = []
    my_set = set(numbers)
    for el in my_set:
        new_numbers_list.append(el)
    return new_numbers_list