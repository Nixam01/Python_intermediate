'''
listA = list(range(6))
listB = list(range(6))

print(listA, listB)

product = []
for a in listA:
    for b in listB:
        product.append((a,b))
print(product)

product = [(a,b) for a in listA for b in listB]
print(product)

product = [(a,b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0]
print(product)

product = {a:b for a in listA for b in listB if a % 2 == 1 and b % 2 == 0}
print(product)
'''

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ', 'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

connections = [(a,b) for a in ports for b in ports]
print(connections)
print(len(connections))

connections = [(a,b) for a in ports for b in ports if a!=b ]
print(connections)
print(len(connections))

connections = [ (a, b) for a in ports for b in ports if a < b]
print(connections)

print(len(connections))
