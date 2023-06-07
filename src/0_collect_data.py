import requests

url = 'https://zenodo.org/record/7879430/files/arguments-test.tsv?download=1'
r = requests.get(url, allow_redirects=True)
open('../data/raw/initial/arguments-test.tsv', 'wb').write(r.content)

url = 'https://zenodo.org/record/7879430/files/arguments-training.tsv?download=1'
r = requests.get(url, allow_redirects=True)
open('../data/raw/initial/arguments-training.tsv', 'wb').write(r.content)

url = 'https://zenodo.org/record/7879430/files/arguments-validation.tsv?download=1'
r = requests.get(url, allow_redirects=True)
open('../data/raw/initial/arguments-validation.tsv', 'wb').write(r.content)

url = 'https://zenodo.org/record/7879430/files/labels-test.tsv?download=1'
r = requests.get(url, allow_redirects=True)
open('../data/raw/initial/labels-test.tsv', 'wb').write(r.content)

url = 'https://zenodo.org/record/7879430/files/labels-training.tsv?download=1'
r = requests.get(url, allow_redirects=True)
open('../data/raw/initial/labels-training.tsv', 'wb').write(r.content)

url = 'https://zenodo.org/record/7879430/files/labels-validation.tsv?download=1'
r = requests.get(url, allow_redirects=True)
open('../data/raw/initial/labels-validation.tsv', 'wb').write(r.content)

url = 'https://zenodo.org/record/7879430/files/value-categories.json?download=1'
r = requests.get(url, allow_redirects=True)
open('../data/raw/initial/value-categories.json', 'wb').write(r.content)
