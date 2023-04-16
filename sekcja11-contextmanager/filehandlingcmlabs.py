import os
import zipfile
import requests

class FileFromWeb:

    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def __enter__(self):
        response = requests.get(self.url)
        with open(self.tmp_file, "wb") as file:
            file.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'C:/Users/marci/PycharmProjects/Python_sredniozaawansowany/data/eurofxref.zip') as f:

    with zipfile.ZipFile(f.tmp_file, "r") as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir('c:/temp ')
        z.extract(a_file, '.', None)