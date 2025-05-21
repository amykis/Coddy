"""
Challenge task6

Create function named process_numbers that takes a list of numbers and processes them according to specific rules.

Requirements:

First filter out all negative numbers and zero
Then for the remaining positive numbers:
Double even numbers
Triple odd numbers
Use map() and filter() to solve the problem.
"""


def process_numbers(numbers):
    cleaned = filter(lambda number: number > 0, numbers)
    processed_numbers = map(lambda number: number * 2 if number % 2 == 0 else number * 3, cleaned)

    return list(processed_numbers)


numbers = [-4, 0, 5, 2, 8, -3, 7]
print(process_numbers(numbers))
