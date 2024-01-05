"""
Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days




"""


import datetime
from datetime import date


now = datetime.datetime.now();
today = date(now.year,now.month,now.day);
print("Today: %s" %today);



date_input = input("Enter the date you want to caculate: ");
date_string = tuple(date_input.split("-"));
#date_int = tuple(int(x) for x in date_string)
date_int = tuple(map(int, date_string))
date_user = date(date_int[0],date_int[1],date_int[2])
print("Day you enter: %s" %date_user);


print("Distance between two days is: %s" %(date_user - today));







