#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('                                      MINI CALCULATOR                                        ')
def add(numbers):
    return sum(numbers)

def sub(numbers):
    res = numbers[0]
    for i in numbers[1:]:
        res -= i
    return res

def mul(numbers):
    res = numbers[0]
    for i in numbers[1:]:
        res *= i
    return res

def div(numbers):
    res = numbers[0]
    for i in numbers[1:]:
        if i != 0:
            res /= i
        else:
            return "Error: Division by zero"
    return res


def f_div(numbers):
    res = numbers[0]
    for i in numbers[1:]:
        if i != 0:
            res //= i
        else:
            return "Error: Division by zero"
    return res

def calc():
    while True:
        n = int(input('Enter the number of values to perform the operation in the calculator: '))
        out = []
        for i in range(1, n + 1):
            a = int(input(f'Enter the {i}st no: '))
            out.append(a)
        print('The values you entered to perform the operation are : ', out)

        print('''The choices are :
             1. Addition
             2. Subtraction
             3. Multiplication
             4. Division
             5. Floor Division
             6. All the above operations
             ''')

        x = int(input('Enter your choice to perform the operation in the calculator: '))

        if x == 1:
            print('Sum is: ', add(out))
        elif x == 2:
            print('Difference is: ', sub(out))
        elif x == 3:
            print('Multiplication result is: ', mul(out))
        elif x == 4:
            print('Division result is: ', div(out))
        elif x == 5:
            print('Value of floor division is: ', f_div(out))
        elif x == 6:
            print('Sum is: ', add(out))
            print('Difference is: ', sub(out))
            print('Multiplication result is: ', mul(out))
            print('Division result is: ', div(out))
            print('Value of floor division is: ', f_div(out))
        else:
            print("Enter a valid choice!")

        j = input("If you want to continue further, enter '1' or enter '0' to end the calculator: ")
        if j == '0':
            print('Thank you! Have a nice day.')
            break

calc()

