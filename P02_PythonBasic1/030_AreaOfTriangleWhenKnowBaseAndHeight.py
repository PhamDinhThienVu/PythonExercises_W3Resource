"""
Write a Python program that will accept the base and height of a triangle and compute its area.

Python: Area of a triangle

A triangle is a polygon with three edges and three vertices. It is one of the basic shapes in geometry. A triangle with vertices A, B, and C is denoted triangle ABC.

Vertex of a triangle: The point at which two sides of a triangle meet.
Altitude of a triangle: The perpendicular segment from a vertex of a triangle to the line containing the opposite side.
Base of a triangle: The side of a triangle to which an altitude is drawn.
Height of a triangle: The length of an altitude.
"""

base = int(input("Enter the base: "));
height = int(input("Enter the height: "));

area = base * height / 2;

print("Area = ", area);