# records = []
#
# for line in file:

def get_records(filePath):
    print('----opening file ----')
    file = open(filePath)

    for line in file:
        if ';' in line:
            type, action = line.rstrip("\n").split(':',1)
            record = (type, action)
            yield record
    print('---closing file---')
    file.close()

for record in get_records(r'C:\Users\marci\PycharmProjects\Python_sredniozaawansowany\data\data.txt'):
    print("The type is {} and the action is {}".format(record[0], record[1]))