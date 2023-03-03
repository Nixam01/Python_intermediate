def BuyMe(prefix ='chuj', what='something nice'):
    print(prefix, what)

BuyMe('Please buy me', 'a new car')
BuyMe(prefix = 'Please buy me', what = 'a car')
BuyMe(what = 'a brand new car', prefix = 'Please buy me')
BuyMe(prefix = 'please')
BuyMe(what = 'something sweet')

def show_progress(how_many, character='*', ):
    print(character*how_many)

show_progress(10)
show_progress(15)
show_progress(30)

show_progress(10, '-')
show_progress(15, '+')
  