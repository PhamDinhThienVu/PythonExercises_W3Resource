""""
Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.



"""

a = int(input("Enter a: "));
b = int(input("Enter b: "));
c = int(input("Enter c: "));
sum = 0;
if( a == b == c):
  sum = (a + b + c) * 3;
else:
  sum = (a + b + c);

print("Sum: ",sum);