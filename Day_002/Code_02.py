import datetime
print("************Welcome to Day 2 of Coding****************")

now = datetime.datetime.now()
print("Current date and time is : ", now)
print("Current year is : ", now.year)
print("Current month is : ", now.month)
print("Current day is : ", now.day)
print("Current hour is : ", now.hour)
print("Current minute is : ", now.minute)
print("Current second is : ", now.second)
print("Current weekday is : ", now.strftime("%A"))
print("Current date inn formatted string : ", now.strftime("%Y-%m-%d %H:%M:%S"))

print("In this way we can use datetime module to get current date and time .")
print("========================================")

