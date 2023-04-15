import csv

with open('C:/Users/marci/PycharmProjects/Python_sredniozaawansowany/data/data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #for row in csvreader:
    #    print('|'.join(row))
    print(next(csvreader))
    while True:
        try:
            print(next(csvreader))
        except StopIteration:
            break