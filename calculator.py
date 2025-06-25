def calculator():
    print("Welcome to Simple Calculator!")
    
    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    choice = input("Enter your choice (1/2/3/4): ")

    # Perform calculation
    if choice == '1':
        result = num1 + num2
        operation = '+'
    elif choice == '2':
        result = num1 - num2
        operation = '-'
    elif choice == '3':
        result = num1 * num2
        operation = '*'
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            operation = '/'
        else:
            print("Error: Cannot divide by zero.")
            return
    else:
        print("Invalid choice. Please select a valid operation.")
        return

    # Display result
    print(f"\nResult: {num1} {operation} {num2} = {result}")

# Run the calculator
calculator()
