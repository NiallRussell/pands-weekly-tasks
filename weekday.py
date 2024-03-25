#This program outputs whether or not today is a weekday
#Author: Niall Russell

#Import date class from datetime module- date class has everything we need so no need to import full module- https://docs.python.org/3/library/datetime.html
from datetime import date
#Getting today's date
today = date.today()
#date.weekday() method returns numbers for each day of the week (0=Monday, 6=Sunday)- https://www.educative.io/answers/what-is-the-datetime-dateweekday-function-in-python
#If today's weekday number is less than 5 it is is weekday
if today.weekday() < 5:
    print("Yes, unfortunately today is a weekday")
#If today's weekday number is greater than 5 it is the weekend
else:
    print("It is the weekend, yay!")