def simple_calculator():
    print("Welcome to the Simple Calculator Program!")
    
    # Input first number
    num1 = float(input("Enter the first number: "))
    
    # Input second number
    num2 = float(input("Enter the second number: "))
    
    # Input operation (+, -, *, /)
    operation = input("Enter the operation (+, -, *, /): ")
    
    # Perform calculation based on operation
    if operation == '+':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Invalid operation. Please enter one of +, -, *, /")

# Run the calculator function
simple_calculator()
print("""")