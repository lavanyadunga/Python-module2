# Simple calculator without using any functions
print("Simple calculator ")

# Read and validate the first number inline
num1_input = input("Enter the first number: ")
try:
    num1 = float(num1_input) if ('.' in num1_input) else int(num1_input)
except Exception:
    print("Error: Please enter a valid number.")
    exit()

# Read and validate the second number inline
num2_input = input("Enter the second number: ")
try:
    num2 = float(num2_input) if ('.' in num2_input) else int(num2_input)
except Exception:
    print("Error: Please enter a valid number.")
    exit()

# Choose operation and compute result using inline conditionals
operation = input("Choose an operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    expr = f"{num1} + {num2} = {result}"
elif operation == "-":
    result = num1 - num2
    expr = f"{num1} - {num2} = {result}"
elif operation == "*":
    result = num1 * num2
    expr = f"{num1} * {num2} = {result}"
elif operation == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        exit()
    result = num1 / num2
    expr = f"{num1} / {num2} = {result}"
else:
    print("Error: Unsupported operation. Please choose +, -, *, or /.")
    exit()

print(expr)
