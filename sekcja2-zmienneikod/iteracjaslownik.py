workDays = [19, 21, 22, 21, 20, 22]
months = ['I', 'II', 'III', 'IV', 'V', 'VI']

monthDays = dict(zip(months, workDays))
print(monthDays)

for key in monthDays:
    print('Key is', key, 'value is', monthDays[key])

for value in monthDays.values():
    print('the value is', value)


banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]

lenOflist = len(banknotes_coins)
newlist =[]
for i in range(lenOflist):
    newlist.append(0)
dict_denominations = dict(zip(banknotes_coins, newlist))
print(dict_denominations)

dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1

dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2

dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1


for key in dict_denominations:
    print("Denominate: {0:6.2f} - amount {1:5}".format(key, dict_denominations[key]))