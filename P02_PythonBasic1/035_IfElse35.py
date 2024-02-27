"""
Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.z
"""

def sub(x,y):
    return x - y;

def sum(x,y):
    return x + y;

def solve(x, y):
    if(x == y):
        return True
    elif(sum(x,y) == 5):
        return True;
    elif(sub(x,y)==5):
        return True;
    else:
        return False;

print(solve(3,2));
print(solve(15,10));
print(solve(7,6));