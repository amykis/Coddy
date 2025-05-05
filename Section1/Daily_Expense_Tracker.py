print('Welcome to the Daily Expense Tracker!')
print('''
Menu:
1. Add a new expense
2. View all expenses
3. Calculate total and average expense
4. Clear all expenses
5. Exit
''', end='')

expenses_list = []
while True:
    value = int(input())
    if value == 5:
        print('Exiting the Daily Expense Tracker. Goodbye!')
        break
    elif value == 1:
        expenses_list.append(float(input()))
        print('Expense added successfully!')
    elif value == 2:
        if len(expenses_list) == 0:
            print('No expenses recorded yet.')
        else:
            print('Your expenses:')
            for i in range(0, len(expenses_list)):
                print(f'{i + 1}. {expenses_list[i]}')
    elif value == 3:
        if len(expenses_list) == 0:
            print('No expenses recorded yet.')
        else:
            total = 0
            for i in range(0, len(expenses_list)):
                total += expenses_list[i]
            average = total / len(expenses_list)
            print(f'Total expense: {total}', f'Average expense: {average}', sep='\n')
    elif value == 4:
        expenses_list.clear()
        print('All expenses cleared.')