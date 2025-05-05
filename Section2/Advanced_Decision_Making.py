'''
Create a function named compare_strings that takes two strings, str1 and str2, as arguments.
The function should perform the following operations:

Check if str1 is a substring of str2.
Check if str2 starts with str1.
Check if str2 ends with str1.
Check if str1 and str2 are equal (case-insensitive).
Return a dictionary containing the results of these operations, with the keys "is_substring", "starts_with", "ends_with", and "is_equal".
'''

def compare_strings(str1, str2):
    # Write code here
    dictionary = {}
    dictionary["is_substring"] = True if str1 in str2 else False
    dictionary["starts_with"] = True if str2.startswith(str1) else False
    dictionary["ends_with"] = True if str2.endswith(str1) else False
    dictionary["is_equal"] = True if str1.lower() == str2.lower() else False

    return dictionary


str1 = 'hello'
str2 = 'Hello'

print(compare_strings(str1, str2))