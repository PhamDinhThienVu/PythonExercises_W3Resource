"""
36. Write a Python program to add two objects if both objects are integers.

"""

def twoInterger(a,b):
    if( isinstance(a,int) and isinstance(b,int)):
        return True;
    else:
        return False;

def add_twoIntergers(a,b):
    if(twoInterger(a,b)):
        return a + b;
    else:
        return None;

print(add_twoIntergers(3, 4))
print(add_twoIntergers(3, 4.5))
print(add_twoIntergers(3, True))
print(add_twoIntergers(-3, True))