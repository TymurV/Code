num1 = int(input('Enter the 1st number: '))
num2 = int(input('Enter the 2nd number: '))
symbol = input('Enter symbol(+, -, /, *, %): ')
sum = 0
if symbol == '+':
    sum = num1 + num2
    print(f'Sum: {sum}')
elif symbol == '-':
    sum = num1 - num2
    print(f'Sum: {sum}')
elif symbol == '/':
    sum = num1 / num2
    print(f'Sum: {sum}')
elif symbol == '*':
    sum = num1 * num2
    print(f'Sum: {sum}')
elif symbol == '%':
    sum = num1 % num2
    print(f'Sum: {sum}')
else:
    print('Incorrectly entered character')