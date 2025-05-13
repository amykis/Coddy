"""
Challenge task1

Easy
Create a function named convert_to_uppercase that takes a list of strings strings as an argument.
The function should use the map() function along with a lambda function to convert each string in the list to uppercase.
The function should return a list containing the uppercase strings.
"""


def convert_to_uppercase(strings):
    # Use map() with a lambda function to convert strings to uppercase
    uppercase_strings = map(lambda word: word.upper(), strings)

    # Return the list of uppercase strings
    return list(uppercase_strings)


string = ["hello", "world", "python"]
print(convert_to_uppercase(string))
