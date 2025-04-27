"""
Simple Calculator Module
Provides basic arithmetic operations: add, subtract, multiply, divide.
"""

def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the division of x by y. Handle division by zero."""
    if y == 0:
        return "Error: Division by zero."
    return x / y

def main():
    """Run a few test calculations and print the results."""
    print("Simple Calculator")
    print("Add:", add(5, 3))
    print("Subtract:", subtract(5, 3))
    print("Multiply:", multiply(5, 3))
    print("Divide:", divide(5, 3))

if __name__ == "__main__":
    main()
