# define the arithmetic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
def modulo(x, y):
    return x % y

# take user input for operation and numbers
operation = input("Enter operation (+,-,*,/,%): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# perform operation based on user input
if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
elif operation == "%":
    result = modulo(num1, num2)
else:
    print("Invalid operation")

# display the result
print("Result:", result)
