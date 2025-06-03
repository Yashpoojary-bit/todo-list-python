# Simple Calculator in Python

# Step 1: Input numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Choose operation
print("Choose the operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Step 3: Input operation
choice = input("Enter the operation (+, -, *, /): ")

# Step 4: Perform and show result
if choice == '+':
    result = num1 + num2
    print("Result:", result)
elif choice == '-':
    result = num1 - num2
    print("Result:", result)
elif choice == '*':
    result = num1 * num2
    print("Result:", result)
elif choice == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")
