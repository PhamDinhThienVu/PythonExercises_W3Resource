"""
Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

if condition :
indentedStatementBlockForTrueCondition
else:
indentedStatementBlockForFalseCondition

These statement blocks can have any number of statements, and can include about any kind of statement.

"""


import math

def caculateDifferenceBetweenNand17(n):
  return n-17

def checkAndReturnAbsoluteTwiceDifference(diff):
  if(diff>17):
    return abs(diff)*2
  else:
    return diff


n = int(input("Enter n: "));
diff = caculateDifferenceBetweenNand17(int(n))
result = checkAndReturnAbsoluteTwiceDifference(diff)
print("Result: ", result)


