import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def exponentiate(a, b):
    return a ** b

def square_root(a): 
    if a < 0:
        return "Error: Square root of a negative number is not defined."
    return math.sqrt(a)
def trig_function(operation, angle):
    radians = math.radians(angle)
    if operation == "sin":
        return math.sin(radians)
    elif operation == "cos":
        return math.cos(radians)
    elif operation == "tan":
        return math.tan(radians)
    else:
        return "Error: Invalid trigonometric function."

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculator():
    history = []
    
    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exponentiation (^)")
        print("6. Square Root (√)")
        print("7. Trigonometric Functions (sin, cos, tan)")
        print("8. View History")
        print("9. Exit")
        
        choice = input("Enter your choice: ")