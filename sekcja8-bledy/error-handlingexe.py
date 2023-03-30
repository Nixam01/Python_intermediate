import requests
import os
import shutil


def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spisessa/'
dir = 'c:/temp/'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)
try:
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)
    print('Downloading url {}'.format(url))
    save_url_to_file(url, tmpfile_path)

    print('Copying file {} {}'.format(tmpfile_path, file_path))
    shutil.copy(tmpfile_path, file_path)
except Exception as e:
    print("Sorry we have an error....")
    print("Error details: {}".format(e))
else:
    print("Everything was done in success")
finally:
    print("Removing tmp_file")
    os.remove(tmpfile_path)
    print("{} file removed".format(tmpfile_path))