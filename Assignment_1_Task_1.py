#TASK 1
# Basic Mathematical Operations

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
# Division
if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (division by zero is not possible)"

# Results
print("\nResults:")
print("Addition: ",addition)
print("Subtraction: ", subtraction)
print("Multiplication: ", multiplication)
print("Division: ", division)