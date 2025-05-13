"""
Challenge task3

Create a function named get_long_strings that takes a list of strings strings as an argument.
The function should use the filter() function along with a lambda function to select strings
that have a length greater than 5. The function should return a list containing the selected strings.
"""


def get_long_strings(strings):
    # Use filter() with a lambda function to select strings with length greater than 5
    long_strings = filter(lambda word: len(word) > 5, strings)

    # Return the list of selected strings
    return list(long_strings)


string = ["apple", "banana", "cherry", "dragonfruit"]
print(get_long_strings(string))
