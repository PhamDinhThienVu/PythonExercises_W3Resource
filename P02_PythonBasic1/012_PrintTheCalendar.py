"""
Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module.


Input the year : 2017                                                                                         
Input the month : 04                                                                                          
     April 2017                                                                                               
Mo Tu We Th Fr Sa Su                                                                                          
                1  2                                                                                          
 3  4  5  6  7  8  9                                                                                          
10 11 12 13 14 15 16                                                                                          
17 18 19 20 21 22 23                                                                                          
24 25 26 27 28 29 30 


"""





import calendar
import datetime

now = datetime.datetime.now();

y = now.year;
m = now.month;




print(calendar.month(y,m));

