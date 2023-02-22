# Solution

## Step 1 Solution

```python
import os
import json

count = 0
for filename in os.listdir('/home/labex/project/json_files'):
    data = json.load(open(os.path.join('/home/labex/project/json_files', filename), 'r'))
    count += len(data)
print(count)
```

## Step 2 Solution

```python
import os
import json

merged = []
for filename in os.listdir('/home/labex/project/json_files'):
    data = json.load(open(os.path.join('/home/labex/project/json_files', filename), 'r'))
    for value in data.values():
        if isinstance(value, list):
            merged.append(value)
with open('/home/labex/project/list.json', 'w') as f:
    json.dump(merged, f)
```

## Step 3 Solution

```python
import sys
import json

filename, key = sys.argv[1:]
if os.path.isfile(filename):
    data = json.load(filename, 'r')
    if key in data:
        print(f'The value for the key {key} in {filename} is {data[key]}.')
```
