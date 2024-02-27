

"""
Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.

"""


def sum(x,y):
    sum = x + y
    if(sum > 15 and sum < 20):
        sum = 20
    return sum


print(sum(15,1))
print(sum(20,1))