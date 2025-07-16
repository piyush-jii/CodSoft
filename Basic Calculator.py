def calculator():
    print("Welcome to Simple Calculator!")    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operation = input("Enter your choice (1/2/3/4): ")
    if operation == '1' or operation == '+':
        result = num1 + num2
        op = '+'
    elif operation == '2' or operation == '-':
        result = num1 - num2
        op = '-'
    elif operation == '3' or operation == '*':
        result = num1 * num2
        op = '*'
    elif operation == '4' or operation == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2
        op = '/'
    else:
        print("Invalid operation choice.")
        return
    print(f"\nResult: {num1} {op} {num2} = {result}")
calculator()
