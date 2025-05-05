'''
Adding The Twist

Challenge

Easy
Add a small twist to the game:

Numbers that contain the digit "3" but aren't divisible by 3 or 7 will output Almost Fizz

To check if a string contains a char use in for instance, "a" in word
'''

def fizzbuzz(number):
    if number % 3 == 0 and number % 7 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 7 == 0:
        return 'Buzz'
    else:
        return f'{number}'


print('Welcome to FizzBuzz!')
number = int(input())
for i in range (1, number + 1):
    print(fizzbuzz(i))