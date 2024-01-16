"""
Write a Python program that checks whether a specified value is contained within a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""

def is_in(value, array):
  return value in array;

result = is_in(3 , [1,5,8,3]);
print(result);