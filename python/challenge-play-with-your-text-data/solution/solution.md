# Solution

## Step 1 Solution

```python
import os

total_len = 0
for f in os.listdir('/home/labex/files'):
    total_len += len(open(os.path.join('/home/labex/files', f), 'r').read().split())

print(total_len)
```

## Step 2 Solution

```python
import os

words_counter = {}
for f in os.listdir('/home/labex/files'):
    words = open(os.path.join('/home/labex/files', f), 'r').read().split()
    for word in words:
        word = word.strip('.,')
        if word not in words_counter:
            words_counter[word] = 0
        words_counter[word] += 1

for words, count in sorted(words_counter.items(), key=lambda x: x[1], reverse=True)[:3]:
    print(words, count)
```

## Step 3 Solution

```python
import os

words_list = []

for f in os.listdir('/home/labex/files'):
    texts = open(os.path.join('/home/labex/files', f), 'r').read().split()
    words_list.append([text.strip(',.') for text in texts])


for i in range(max(words_count)):
    words = []
    for word_list in words_list:
        if i <= len(word_list):
            words.append(word_list[i])
    open(f'/home/labex/output/{i+1}', 'w').write(' '.join(words))
```
