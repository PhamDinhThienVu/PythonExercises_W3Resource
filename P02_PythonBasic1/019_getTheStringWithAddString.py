""""

Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
"""

def new_string(text):
  if(len(text) >= 2 and text[0:2] == "Is"):
    return text;
  else:
    return "Is" + text;


str_input = input("Enter the string: ");

newString = new_string(str_input);
print("Result: ", newString);