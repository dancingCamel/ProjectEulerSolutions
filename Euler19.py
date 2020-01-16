# You are given the following information, but you may prefer to do some research for yourself.
#
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


number_of_Sundays = 0
days = 0
year = 1901

days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

while year < 2001:

    if year % 4 == 0:
        days_in_month[2] = 29
    if year % 100 == 0:
        days_in_month[2] = 28
    if year % 400 == 0:
        days_in_month[2] = 29
    else:
        days_in_month[2] = 28

    for i in range(1, 13):
        days += days_in_month[i]
        if (days + 1) % 7 == 0:
            number_of_Sundays += 1
    year += 1

print(number_of_Sundays)