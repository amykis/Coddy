"""
Challenge task4

Create a function named get_prime_numbers that takes a list of integers numbers as an argument.
The function should use the filter() function along with a lambda function to select prime numbers from the list.
A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
The function should return a list containing the selected prime numbers.
"""


def get_prime_numbers(numbers):
    return list(filter(lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)), numbers))

numbers = [23, 29, 31, 32, 33, 37, 39, 41, 42, 43]
print(get_prime_numbers(numbers))

