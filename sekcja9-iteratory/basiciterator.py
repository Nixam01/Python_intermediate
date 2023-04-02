import datetime as dt
import sys


class MillionDays():
    def __init__(self, year, month, day, maxdays):
        self.date = dt.date(year, month, day)
        self.maxdays = maxdays

    def __next__(self):
        if self.maxdays <= 0:
            raise StopIteration()
        ret = self.date
        self.date += dt.timedelta(days=1)
        self.maxdays -= 1
        return ret

    def __iter__(self):
        return self

md = MillionDays(2000, 1, 1, 2500000)
print('size of Million object is: {}'.format(sys.getsizeof(md)))
for days in md:
    pass