'''
Challenge Easy
Create a program that takes an integer score from the user. The program should use the ternary operator to determine the status based on the score:

If the score is greater than or equal to 50, the status should be "Pass".
If the score is less than 50, the status should be "Fail".
The program should output the determined status.
'''

takes = int(input())
status = "Pass" if takes >= 50 else "Fail"
print(status)