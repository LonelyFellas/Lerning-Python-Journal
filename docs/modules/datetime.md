# `datetime` 模块


## Today's Date

Use datatime.date.today()

datetime.date class has the following integer attributes, date(year, month, day)

get day of the week using date.weekday() 
 
Monday is 0

 ```py3
from datetime import date

todays_date = date.today()
print(todays_date) # today
print(todays_date.month, todays_date.day, todays_date.year) # month day , year
print(todays_date.weekday()) # monday is 0
```

## ISO format is a string format, yyyy-mm-dd

 date_object.isoformat() dones the some thing as str(date_object)

```py3
from datetime import date
todays_date = date.formisoformat('2024-06-02')
print(todays_date)
print(str(todays_date))
print(todays_date.isoformat)
```

## Comparision, addition, sutraction of dates

Comparison gives boolean result. Later date is greater than earlier date.

Date addition & subtraction give result as a datetime.timedelta object (explained more below).

The same comparison and add/subtract operations can be used with time objects.

```py3
from datetime import date
todays_date = date.today()
d2  = date(2022, 2, 2)
print(todays_date > d2)
print(todays_date - d2)
```

## Time

两个时间对象进行比较（时，分，秒，毫秒）

```py3
from datetime import time
t1 = time(14, 25, 36, 18625)
print(t1)

t2 = time(2, 19)
print(t2)
print(t1 < t2)
```

使用 `datetime.datetime.now()` 去获得当前的日期和时间

 ```py3
t3 = datetime.now()

print(t3.time())
print(t3.date())
print(t3.hour, t3.minute)
print(str(t3.month) + '-' + str(t3.day) + '-' + str(t3.year))
 ```
