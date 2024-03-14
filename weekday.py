#Import datetime module- 
import datetime 
#Getting today's date
today = datetime.date.today()
# date.weekday() method returns numbers for each day of the week (0=Monday, 6=Sunday)- https://www.educative.io/answers/what-is-the-datetime-dateweekday-function-in-python
if today.weekday() < 5:
    print("Yes, unfortunately today is a weekday")
else:
    print("It is the weekend, yay!")