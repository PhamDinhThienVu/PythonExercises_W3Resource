"""""

Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.

string = "abcdef"
no of copies = 2
return abab


"""

def newString(text,n):
  flen = 2

  if(flen > len(text)):
    flen = len(text)

  subStr = text[0:flen];

  result = "";
  for i in range(n):
    result += subStr;

  return result;


text = input("Enter the string: ");
n = int(input("Enter the no of copies: "));

newString = newString(text,n);
print(newString);


