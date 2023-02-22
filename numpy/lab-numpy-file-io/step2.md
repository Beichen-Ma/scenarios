# Reading Arrays from Files

NumPy provides several functions for reading arrays from files. The most common are `loadtxt`, `genfromtxt` and `load`.

## Using loadtxt

The `loadtxt` function is used to read arrays from text files.Here is an example:

```python
data = np.loadtxt('data.txt',delimiter=',')
print(data)
```

- This will read the contents of `data.txt` into a NumPy array, from step 1 we know that the values in `data.txt` are separated by `commas`.
- The code `print(data)` will print the content read from `data.txt`.

## Using Genfromtxt

The `genfromtxt` function is similar to loadtxt, but it can handle missing values and other special cases. Here is an example:

```python
data = np.genfromtxt('data.txt', delimiter=',')
print(data)
```

- This will read the contents of `data.txt` into a NumPy array.

## Using Load

The `load` function is used to read the arrays from binary files. Here is an example:

```python
data = np.load('data.npy')
print(data)
```

- This will read the contents of `data.npy` into a NumPy array.
