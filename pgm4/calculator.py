# Simple Calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Addition
print("Addition:", a + b)

# Subtraction
print("Subtraction:", a - b)

# Multiplication
print("Multiplication:", a * b)

# Division
if b != 0:
    print("Division:", a / b)
else:
    print("Division: Cannot divide by zero")