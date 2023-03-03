'''
for i in range(10):
    print(i)
'''
'''
for i in range(1,11,2):
    print(i)

for i in range(10, 0, -2):
    print(i)

list = list(range(10))
print('List:', list, type(list))

print(list[5:7])
print(list[:-1])
print(list[-2:])

list2 = list.copy()
print(list, type(list), id(list))
print(list2, type(list2), id(list2))
'''
colors = ['red', 'orange', 'green', 'violet', 'blue', 'yellow']

def copyColorList(colorslist, n):
    newColors = colorslist.copy()
    newColors = newColors[:n]
    return newColors

lenOfList = len(colors)
for n in range(lenOfList):
    print(copyColorList(colors, n))

text = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli.'
print(text[text.index('(')+1:text.index(')')])