def calculator():
    # Display the menu
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("s. modulus")

    # Get user input for operation
    choice = input("Enter choice (1/2/3/4): ")

    # Get user input for numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the selected operation
    if choice == '1':
        result = num1 + num2
        print(f"The result of addition is: {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"The result of subtraction is: {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"The result of multiplication is: {result}")
    elif choice == '5':
        result = num1 % num2
        print(f"the result of modulus is: {result}")
    elif choice == '4':
    
        # Handle division by zero
        if num2 != 0:
            result = num1 / num2
            print(f"The result of division is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input. Please choose a valid operation.")

# Example usage
calculator()
