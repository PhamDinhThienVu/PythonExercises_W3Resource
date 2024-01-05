"""
Write a Python program to get the volume of a sphere with radius six.
"""

import math

radius = float(input("Enter the radius: "));
pi = math.pi;

volume = radius**3*(4/3)*pi;

# diameter = radius*2;
# volume = diameter**3*(1/6)*pi;
print(volume);
