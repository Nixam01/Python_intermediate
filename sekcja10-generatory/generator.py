import datetime as dt

def MillionDays(year,month,day,maxdays):
    date = dt.date(year,month,day)

    for i in range(maxdays):
        date + dt.timedelta(days=i)
        yield(date + dt.timedelta(days=i))
#md = MillionDays(2000, 1, 1, 3)
for d in MillionDays(2000, 1, 1, 3):
    print(d)
