import os

from contextlib import suppress
with suppress(FileNotFoundError):
    os.remove(r'c:\temp\file.txt')


from contextlib import redirect_stdout
f = open(r'c:\temp\log.txt')


class Door:
    pass


with redirect_stdout(f):
    print('Hello')
    d = Door('EXIT')