"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615

5 + 55 + 555
"""

n = input("Enter a number N: ");
print("N: ",n);

sum = int(n) + int("%s%s"%(n,n)) + int("%s%s%s"%(n,n,n));
print(sum);





