number = 10
print('Variable number:', number, id(number))
number += 2
print('Variable number:', number, id(number))

text = 'Africa'
print('Variable text', text, id(text))
text += ' is hot'
print('Variable text', text, id(text))

list = [1,2,3]

print('Variable list', list, id(list))

list.append(4)
print('Variable list', list, id(list))

days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

workdays = days.copy()
workdays.remove('sat')
workdays.remove('sun')
print(days, workdays)
