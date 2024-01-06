"""
Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
"""

def newString(text, noOfCopies):
  result = ""
  for i in range(noOfCopies):
    result += text
  return result


str_input = input("Enter the string: ")
int_noOfCompies = int(input("Enter the num of compies: "))

str_newString = newString(str_input, int_noOfCompies)
print("Result: ",str_newString);
    