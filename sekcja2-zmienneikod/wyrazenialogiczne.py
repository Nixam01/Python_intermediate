import os



#os.remove(path)
'''
if os.path.isfile(path):
    print('File %s exists' % path)
else:
    print('Creating a file %s' % path)
    open(path, 'x').close()
    print('File %s created' % path)
'''

#result = os.path.isfile(path) and open(path, 'x').close()
#print(result)

newpath = r'c:\temp\pogoda.txt'

def WordsInFile(path):
    with open(path,'r') as f:
        content = f.read()
        word_count = len(content.split())
    return word_count

if os.path.isfile(newpath):
    print("There are {} words in the file {}".format(WordsInFile(newpath), newpath))

