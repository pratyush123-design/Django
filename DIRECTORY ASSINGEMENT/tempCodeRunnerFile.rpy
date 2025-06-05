import calendar
year=int(input("Enter a year:"))
month=int(input("Enter a month (1-12):"))
day=int(input("Emter a day:"))
current_year=int(input("Enter curret year:"))
current_month=int(input("Enter current month:"))
current_day=int(input("Enter curent day:"))
age_in_year=abs(current_year-year)
age_in_month=abs(current_month-month)
age_in_days=abs(current_day-day)
 
print("/nHere is the calendar")
# print(calendar.month(year, month, day))
print(f"{age_in_year} Years {age_in_month} Months and {age_in_days} days")