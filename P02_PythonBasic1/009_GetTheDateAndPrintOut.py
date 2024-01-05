"""
Write a Python program to display the examination schedule. (extract the date from exam_st_date).

exam_st_date = (11, 12, 2014)
Sample Output: The examination will start from : 11 / 12 / 2014

The said code creates a tuple called "exam_st_date" containing three integers: 11, 12, and 2014. It then uses string formatting to print a string that states "The examination will start from :" followed by the integers in the tuple in the order they appear, formatted as day/month/year. The placeholders %i are used to format the integers.

The output would be: "The examination will start from : 11 / 12 / 2014".

"""

date_input = input("Enter the date: ");

date_string = tuple(date_input.split("/"));
#date_int = tuple(int(x) for x in date_string)
date_int = tuple(map(int, date_string))

print("The examination will start form: %i/%i/%i" %(date_int));
