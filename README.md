# TuteDude-Assignments
Assignment For Python

Task 1

Basic Mathematical Operations

This is a simple Python program that performs basic mathematical operations (addition, subtraction, multiplication, and division) on two numbers entered by the user.

How It Works

1. The program prompts the user to input two numbers.


2. It then calculates:

Addition of the two numbers

Subtraction (first number minus second number)

Multiplication of the two numbers

Division (first number divided by second number)



3. If the second number is 0, division is not performed and a warning is displayed instead (to prevent division by zero).


4. Finally, the results of all operations are printed.



Code

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
print("Addition: ", addition)
print("Subtraction: ", subtraction)
print("Multiplication: ", multiplication)
print("Division: ", division)

Example Usage

Enter the first number: 10
Enter the second number: 5

Results:
Addition: 15.0
Subtraction: 5.0
Multiplication: 50.0
Division: 2.0

Notes

Make sure to input valid numerical values.

Division by zero is handled safely and will not crash the program.