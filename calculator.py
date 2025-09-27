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