"""

Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.


"""

def checkEven(n):
  if(n % 2 == 0):
    return True
  else:
    return False
  

number = int(input("Enter a number: "));
if(checkEven(number)):
  print("Is Even Number!");
else:
  print("Odd number!");
