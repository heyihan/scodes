# https://projecteuler.net/problem=19

def is_leap(year):
    if year%4 != 0:
        return False
    if year%100 == 0 and year%400 != 0:
        return False
    return True

def year_days(year):
    if is_leap(year):
        return 366
    return 365

def month_days(month, year):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    if month == 2:
        if is_leap(year):
            return 29
        return 28
    return 31


day_19000101 = 1
days_1900 = year_days(1900)

day_next_day1 = (day_19000101 + days_1900)%7
print(day_19000101, days_1900, day_next_day1)

sum = 0
for i in range(1901, 2001):
    for j in range(1, 13):
        if day_next_day1 == 0:
            print(i, j)
            sum = sum + 1
        days = month_days(j, i)
        day_next_day1 = (day_next_day1 + days)%7
        #print(i, j, days, day_next_day1)


print(sum)
