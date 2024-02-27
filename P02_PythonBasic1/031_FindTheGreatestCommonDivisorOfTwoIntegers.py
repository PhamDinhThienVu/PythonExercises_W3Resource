""""
Write a Python program that computes the greatest common divisor (GCD) of two positive integers.

The greatest common divisor (GCD) of two nonzero integers a and b is the greatest positive integer d such that d is a divisor of both a and b; that is, there are integers e and f such that a = de and b = df, and d is the largest such integer. The GCD of a and b is generally denoted gcd(a, b).

"""


def greatestCommonDivisor(a , b):
  while(a != b):
    if(a > b):
      a = a - b;
    if(b > a):
      b = b-a;
  
  return a;

print("GCD of 12 & 17 =", greatestCommonDivisor(12, 17))
print("GCD of 4 & 6 =", greatestCommonDivisor(4, 6))
print("GCD of 336 & 360 =", greatestCommonDivisor(336, 360))