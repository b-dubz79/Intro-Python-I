"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""
import sys
import calendar
from datetime import datetime

today = datetime.now()

currentMonth = 7
new_month = 7
year = 2020

print(today)

# print(sys.argv)

# print("calendar for today", calendar)

print(sys.argv)
print("length of sys.argv", len(sys.argv))

#If no argument, return calendar for current month
if len(sys.argv) == 1:
  calendar = calendar.month(year, currentMonth, 2, 1)
  print(calendar)

#If one argument, return calendar for that month of this year
if len(sys.argv) == 2:
    print(sys.argv[1], "sys.argv[1]")
    print(new_month, "month")

    new_month = sys.argv[1]

    calendar = calendar.month(year, int(new_month), 2, 1)
    print(calendar)

#If two arguments, return calendar for month and year
if len(sys.argv)  == 3:
  year = sys.argv[2]
  new_month2 = sys.argv[1]
  calendar = calendar.month(year, int(new_month), 2, 1)
  print(calendar)

#If invalid arguments, print correct format and exit.
