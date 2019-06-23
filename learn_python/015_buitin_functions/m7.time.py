# coding: utf8
import time
import datetime

# 最常用
print(
    time.strftime("%Y-%m-%d %H:%M:%S")
)

# datetime.now --> string
now = datetime.datetime.now()
now_str = now.strftime('%Y-%m-%d %H:%M:%S')

# string --> datetime
t_str = '2012-03-05 16:26:23'
d = datetime.datetime.strptime(t_str, '%Y-%m-%d %H:%M:%S')

# deltatime
delta = datetime.timedelta(
    days=0, 
    seconds=0, 
    microseconds=0, 
    milliseconds=0, 
    minutes=0, 
    hours=2, 
    weeks=0        )

# print: two hours later
two_hours_later = now + delta
print(
    two_hours_later.strftime('%Y-%m-%d %H:%M:%S')
)

# delta: ten years
year = datetime.timedelta(days=365)
ten_years = 10 * year

print(ten_years)
print(ten_years.days)

# n天后的日期
now = datetime.datetime.now()
delta = datetime.timedelta(days=3)
n_days = now + delta
print(n_days.strftime('%Y-%m-%d %H:%M:%S')) 