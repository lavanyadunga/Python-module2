def get_number(prompt):
    value = input(prompt)
    if value.replace('.', '', 1).isdigit():
        return float(value) if '.' in value else int(value)
    print("Error: Please enter a valid number.")
    return None

num1 = get_number("Enter the first number: ")
if num1 is None:
    exit()

num2 = get_number("Enter the second number: ")
if num2 is None:
    exit()

operation = input("Choose an operation (+, -, *, /): ")
result = None
expression = None

if operation == "+":
    result = num1 + num2
    expression = f"{num1} + {num2} = {result}"
elif operation == "-":
    result = num1 - num2
    expression = f"{num1} - {num2} = {result}"
elif operation == "*":
    result = num1 * num2
    expression = f"{num1} * {num2} = {result}"
elif operation == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        exit()
    result = num1 / num2
    expression = f"{num1} / {num2} = {result}"
else:
    print("Error: Unsupported operation. Please choose +, -, *, or /.")
    exit()

print(expression)
