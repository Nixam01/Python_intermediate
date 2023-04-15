import datetime as dt

class MillionDays:

    def __init__(self, year, month, day, maxdays):
        self.date = dt.datetime(year, month, day)
        self.maxdays = maxdays

    def __getitem__(self, item):
        if item <= self.maxdays:
            return self.date + dt.timedelta(days=item)
        else:
            raise StopIteration()

md = MillionDays(2000, 1, 1, 20)

it = iter(md)

print(next(it))
print(next(it))
print(next(it))

for d in md:
    print(d)