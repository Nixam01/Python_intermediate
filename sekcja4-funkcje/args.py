def calculate_paint(efficiency_ltr_per_m2, *args):
    total_area = sum(args)
    return total_area*efficiency_ltr_per_m2

print(calculate_paint(3, 10, 5, 7))
surfaces = [10, 20, 15, 8]
print(calculate_paint(2, *surfaces))

import os

def log_it(*args):
    path = r'C:\Users\marci\PycharmProjects\Python_sredniozaawansowany\data\log_it.txt'
    with open(path,'a') as f:
        for line in args:
            f.write(line)
            f.write(" ")
        f.write("\n")

log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')


