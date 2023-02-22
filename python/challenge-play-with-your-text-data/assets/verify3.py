from itertools import zip_longest
import os

words = []
for f in os.listdir('/home/labex/project/files'):
    texts = open(os.path.join('/home/labex/project/files', f), 'r').read().split()
    words.append([text.strip(',.') for text in texts])

words = list(zip_longest(*words, fillvalue=''))

for i, word in enumerate(words):
    ws = open(f'/home/labex/project/output/{i+1}', 'r').read().strip().split()
    assert set(filter(None, word)) == set(ws)