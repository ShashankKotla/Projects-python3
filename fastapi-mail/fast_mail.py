import smtplib

import datetime as dt

now = dt.datetime.now()
year = now.year
week = now.weekday()
print(week)
print(type(now))

birthday = dt.datetime(year=2001, month=7, day=25)
print(birthday)


connection = smtplib.SMTP('smtp.gmail.com')