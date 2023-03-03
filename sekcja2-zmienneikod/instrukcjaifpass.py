import datetime

price = 123
bonus = 23
bonus_granted = True

if bonus_granted:
    price -= bonus

print(price)

rating = 5

if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')

today_weekday = datetime.date.today().strftime("%A")

if today_weekday == 'Monday':
    print('Pomagam mamie')
elif today_weekday == 'Tuesday' or today_weekday == 'Wednesday':
    print('Masz w domu pranie')
elif today_weekday == 'Thursday':
    print('Mam dyżur')
elif today_weekday == 'Friday':
    print('Dwa zebrania')
elif today_weekday == 'Saturday':
    print('Nie możesz, bo na lekcje ganiasz')
else:
    print('Niedziela jest dla nas')

print('Pomagam mamie' if today_weekday == 'Monday' else
      "Masz w domu pranie" if today_weekday == 'Tuesday' or today_weekday == 'Wednesday' else
      'Mam dyżur' if today_weekday == 'Thursday' else 'Dwa zebrania' if today_weekday == 'Friday' else
      r'Nie możesz, bo na lekcje ganiasz' if today_weekday == 'Saturday' else
      'Niedzela jest dla nas')