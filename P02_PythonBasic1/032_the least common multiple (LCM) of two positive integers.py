""""

Write a Python program to find the least common multiple (LCM) of two positive integers.

From Wikipedia,
In arithmetic and number theory, the least common multiple, lowest common multiple, or smallest common multiple of two integers a and b, usually denoted by lcm(a, b), is the smallest positive integer that is divisible by both a and b. Since division of integers by zero is undefined, this definition has meaning only if a and b are both different from zero. However, some authors define lcm(a,0) as 0 for all a, which is the result of taking the lcm to be the least upper bound in the lattice of divisibility.
"""
from math import gcd  z

def lcm(x, y):
    """Calculates the least common multiple (LCM) of two positive integers."""
    
    # Ensure both inputs are positive integers
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Inputs must be positive integers.")
    if x <= 0 or y <= 0:
        raise ValueError("Inputs must be positive.")

    # Use the efficient formula LCM(x, y) = (x * y) / GCD(x, y)
    
    return (x * y) // gcd(x, y)

# Get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and print the LCM
lcm_result = lcm(num1, num2)
print("The LCM of", num1, "and", num2, "is", lcm_result)