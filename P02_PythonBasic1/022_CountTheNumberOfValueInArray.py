"""""

Write a Python program to count the number 4 in a given list.
"""


def countValueInList(value, list):
  count = 0;
  for item in list:
    if(item == value):
      count += 1;
  return count;


print(countValueInList(4,[1,4,6,7,4]));

