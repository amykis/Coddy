'''
Write a program that performs the following tasks:

Create a set called numbers containing the values 10, 20, 30, 40, 50.
Use the discard() method to remove 35 from the set.
Use the pop() method to remove an arbitrary element and store it in a variable called popped_element.
Use the clear() method to empty the set.
Print the following:
The set after using discard().
The value of popped_element.
The set after using clear().
'''

# Write code here
numbers = {10, 20, 30, 40, 50}
numbers.discard(35)
print(numbers)
popped_element = numbers.pop()
print(popped_element)
numbers.clear()
print(numbers)