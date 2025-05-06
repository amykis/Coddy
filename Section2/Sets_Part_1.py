'''
Create a function named manage_set that takes three arguments: set1 (a set),
element_to_add, and element_to_remove. The function should perform the following operations:

Add element_to_add to set1.
Attempt to remove element_to_remove from set1. If the element is not in the set, do nothing.
Check if the number 5 is in set1. If it is, return the string "5 is in the set".
Otherwise, return the string "5 is not in the set".
'''

def manage_set(set1, element_to_add, element_to_remove):
    # Write code here
    set1.add(element_to_add)
    if element_to_remove in set1:
        set1.remove(element_to_remove)
    if 5 in set1:
        return "5 is in the set"
    else:
        return "5 is not in the set"