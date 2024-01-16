"""
Write a Python program to create a histogram from a given list of integers.
"""

def histogram(items):
  for item in items:
    output = ''
    times = item
    while(times > 0):
      output += '*'
      times = times - 1

    print(output)

histogram([2,3,6,5])