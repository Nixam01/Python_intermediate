instruction = ['say hello', 'say how are you','ask for money', 'say thank you', 'say bye']
instructionApproved = []

for instr in instruction:
    print('Adding instruction:', instr)
    instructionApproved.append(instr)

    if instr == 'abort':
        print("Aborting!")
        instructionApproved.clear()
        break

else:
    print(instructionApproved)

import os
import urllib.request
data_output_catalog = 'C:\\Users\marci\PycharmProjects\Python_sredniozaawansowany\data'
pages = [{'name': 'kluczedoraju', 'url': 'https://www.youtube.com/watch?v=auLWjs0Xu28&list=RDauLWjs0Xu28&start_radio=1&ab_channel=Justyna/'},
         {'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'},
         {'name': 'udemy', 'url': 'https://www.udemy.com/course/'}]

for page in pages:
    try:
        file_name = "{}.html".format(page["name"])
        path = os.path.join(data_output_catalog, file_name)
        urllib.request.urlretrieve(page["url"], path)
    except:
        print('FAILURE processing web page: {}'.format(page["name"]))
        print('Stopping the process!')
        break
else:
    print('Task done succesfully')

