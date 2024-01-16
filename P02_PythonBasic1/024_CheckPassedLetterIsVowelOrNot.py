"""
Write a Python program to test whether a passed letter is a vowel or not.

string abc
char d
char 'd' is not in string "abc" -> false
else true

"""

def is_vowel(char, string):
  return char in string

result = is_vowel('a',"bcd");
print(result);
