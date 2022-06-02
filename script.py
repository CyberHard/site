import os
import time
import shutil
import wget

import requests

import zipfile
os.mkdir('www')
def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True, allow_redirects=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename

filename = download_file('https://github.com/CyberHard/http/archive/refs/heads/main.zip')
print(filename)

archive = 'main.zip'
with zipfile.ZipFile(archive, 'r') as zip_file:
    zip_file.extractall('www/')
src = 'www/http-main'
dst = 'www/http'
os.rename(src, dst)