listA = list(range(6))
listB = list(range(6))
gen = ((a,b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0)
print(gen)

print(next(gen))
print(next(gen))
print('-'*30)
for x in gen:
    print(x)

print('-'*30)
for x in gen:
    print(x)

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ','LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

connections1 = ((a,b) for a in ports for b in ports)
counter = 0
for (start, stop) in connections1:
    print(start,stop)
    counter+=1

print(counter)
print('-'*30)
connections2 = ((a,b) for a in ports for b in ports if a!=b)

counter = 0
for (start, stop) in connections2:
    print("{} - {}".format(start, stop))
    counter += 1

print(counter)
connections3 = ((a,b) for a in ports for b in ports if a<b)

counter = 0
for (start, stop) in connections3:
    print("{} - {}".format(start, stop))
    counter += 1

print(counter)
while True:
    try:
        print(connections1)
        print(connection2)
        print(connections3)
        print(len(connections1)+len(connection2)+len(connections3))
    except:
        print("end of connections")
        break

        