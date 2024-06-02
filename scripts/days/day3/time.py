from datetime import date, time, datetime

# todays_date = date.today()
# print(todays_date) # today
# print(todays_date.month, todays_date.day, todays_date.year) # month day , year
# print(todays_date.weekday())


# todays_date1 = date.fromisoformat('2024-06-02')
# print(todays_date1)
# print(str(todays_date1))
# print(todays_date1.isoformat())


# todays_date2 = date.today()
# d2 = date(2022, 2, 2)
# print(todays_date2 > d2)
# # print(todays_date2 + d2)
# print(todays_date2 - d2)


t1 = time(14, 25, 36, 18625)
print(t1)

t2 = time(2, 19)
print(t2)
print(t1 < t2)

t3 = datetime.now()

print(t3.time())
print(t3.date())
print(t3.hour, t3.minute)
print(str(t3.month) + '-' + str(t3.day) + '-' + str(t3.year))