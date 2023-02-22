import os
import random
import json

random.seed(1116)

folder = '/home/labex/json_files'
if not os.path.isdir(folder):
    os.mkdir(folder)

for i in range(50):
    file = f'/home/labex/json_files/{i}.json'
    if os.path.isfile(file):
        continue
    json_file = {}
    for _ in range(15):
        if random.random() < 0.5:
            json_file[str(random.randint(0, 50))] = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', random.randint(5, 10)))
        else:
            json_file[str(random.randint(0, 50))] = {random.randint(0, 10): random.randint(0, 10) for _ in range(random.randint(3, 10))}
    json_file[str(random.randint(0, 50))] = [i%(j+1) for j in range(10)]
    json_file[str(i)] = f'{i}{i}'
    with open(file, 'w') as f:
        json.dump(json_file, f)
        