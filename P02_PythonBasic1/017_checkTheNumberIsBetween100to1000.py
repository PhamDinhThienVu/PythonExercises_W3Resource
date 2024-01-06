"""
Write a Python program to test whether a number is within 100 of 1000 or 2000.



"""

def checkNumberBetween100to1000(number):
  return (number >= 100 and number <= 1000)


n = int(input("Enter number to check is it between 100 and 1000: "))
bool_result = checkNumberBetween100to1000(n);

print("Result: ",bool_result);