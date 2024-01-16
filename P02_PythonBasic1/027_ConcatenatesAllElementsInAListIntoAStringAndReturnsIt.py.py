"""
Write a Python program that concatenates all elements in a list into a string and returns it.

"""

def listToString(list):
  output = ""
  for item in list:
    output += str(item);
  return output


list = [1,2,3,4,5];
out_string = listToString(list);
print(out_string)