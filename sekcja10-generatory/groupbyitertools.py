import itertools
import os


def scantree(path):
    for entry in  os.scandir(path):
        if os.DirEntry.is_dir(entry) == True:
            yield entry
            yield from scantree(entry.path)
        if os.DirEntry.is_dir(entry) == False:
            yield entry

listing = scantree(r'C:\Users\marci\PycharmProjects\Python_sredniozaawansowany\data')
for l in listing:
    print('DIR ' if l.is_dir() else 'FILE', l.path)

listing = scantree(r'C:\Users\marci\PycharmProjects\Python_sredniozaawansowany\data')
listing = sorted(listing, key=lambda e: e.is_dir())
for is_dir, elements in itertools.groupby(listing, key=lambda e: e.is_dir()):
    print('DIR ' if is_dir else 'FILE', len(list(elements)))
