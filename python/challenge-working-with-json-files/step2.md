# Write Together

Now you are counting them successfully, then you should find out all `list` values, merge and write them in one JSON file `list.json`.

For example, there are two jsons:

```json
{
  "1": [1, 2, 3],
  "2": { "a": "b" }
}
```

```json
{
  "2": [3, 4, 5],
  "3": { "a": "b" }
}
```

The two lists should be merged to `list.json` as follows:

```json
[
  [1, 2, 3],
  [3, 4, 5]
]
```

## Requirements

- The path of `list.json` is `/home/labex/project`.
