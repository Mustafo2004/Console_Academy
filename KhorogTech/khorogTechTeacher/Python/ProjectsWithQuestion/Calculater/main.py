def calculator():
    print("Welcome to the Simple Calculator!")
    print("Choose an operation:")
    print("1: Addition (+)")
    print("2: Subtraction (-)")
    print("3: Multiplication (×)")
    print("4: Division (÷)")

    operation = int(input("Enter the number corresponding to the operation (1-4): "))
    if operation in [1, 2, 3, 4]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if operation == 1:
            result = num1 + num2
            print(f"The result of {num1} + {num2} is {result}")
        elif operation == 2:
            result = num1 - num2
            print(f"The result of {num1} - {num2} is {result}")
        elif operation == 3:
            result = num1 * num2
            print(f"The result of {num1} × {num2} is {result}")
        elif operation == 4:
            if num2 != 0:
                result = num1 / num2
                print(f"The result of {num1} ÷ {num2} is {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation. Please choose a number between 1 and 4.")

   

calculator()