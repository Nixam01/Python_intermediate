isOk = 'false'
print("variable isOk", type(isOk))

if isOk:
    print('essa')

# w przypadku napisów napis nie pusty będzie interpretowany jako prawda

# podczas konwersji liczby na wartość logiczną jeśli w zmiennej jest cokolwiek to zostaje wartość true; 0 jest konwertowane do wartości false

listOfErrors = [100,101,102]

if len(listOfErrors) > 0:
    print('TRUE')

x = input("Please press a button")
options = ['load data', 'export data', 'analyze & predict']
choice='x'

def DisplayOptions(options):
    for i in range(len(options)):
        print("{} - {}".format(i + 1, options[i]))

    choice = input('Select option above or press enter to exit: ')
    return choice


'''while x:
    print('Options: \n1. Load Data \n2. Export Data \nAnalyze&Predict')
    if not x.isdigit():
        print("value is not a digit")
    elif x.isdigit():
        if x == 1:
            print('Loading data...')
        if x == 2:
            print('Exporting data...')
        if x == 3:
            print('Analyzing and predicting...')
'''
while choice:
    choice = DisplayOptions(options)
    if choice:
        try:
            choice_num = int(choice) - 1
            if choice_num >= 0 and choice < len(options):
                print("you have selected {} - {}".format(choice_num + 1, options[choice_num]))
            else:
                print("choose a value from a list or press enter")
        except:
            print('Ma być wprowadzana liczba ')
    else:
        print('----- END -----')
