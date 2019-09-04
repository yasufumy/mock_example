import os
import requests


def download(url):
    r = requests.get(url)
    filename = os.path.basename(url)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(r.text)
