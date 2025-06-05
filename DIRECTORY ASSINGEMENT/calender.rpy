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
print(f"You are {age_in_year} Years {age_in_month} Months and {age_in_days} days")

from datetime import datetime
date_of_birth=input("Enter your date of Birth YYYY-MM-DD:")
try:
  DOB=datetime.strptime(date_of_birth,"%Y-%m-%d")
  today=datetime.today()
  age_in_days=(today-DOB).days
  age_in_year=age_in_days //365
  print(f"your approximate age is: {age_in_year} Years")
  print(f"You are {age_in_days} days old")

except ValueError:
 print("Invalid date format. Please enter in YYYY-MM-DD format.")
   
