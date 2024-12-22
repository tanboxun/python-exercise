"""
A simple calculator application that performs basic arithmetic operations.

The user is prompted to enter two numbers and an arithmetic operation
(addition, subtraction, multiplication, or division). The program then
calculates and prints the result of the operation.

Functions:
    None

Variables:
    first_number (int): The first number entered by the user.
    second_number (int): The second number entered by the user.
    operation (str): The arithmetic operation chosen by the user.
    result (int or float): The result of the arithmetic operation.
"""
first_number = input("Enter the first number:")
first_number = int(first_number)
print(f'number:{first_number}')

second_number = input("Enter the second number:")
second_number = int(second_number)
print(f'number:{second_number}')

operation = input("Choose an operation (+, -, *, /):")
print(f'operation: {operation}')

if operation == '+':
    result = first_number + second_number
    print(f"result:{result}")
elif operation == '-':
    result = first_number - second_number
    print(f"result:{result}")
elif operation == '*':
    result = first_number * second_number
    print(f"result:{result}")
elif operation == '/':
    result = first_number / second_number
    print(f"result:{result}")
else:
    print('please choose an correct opertaion (+, -, *, /)')
