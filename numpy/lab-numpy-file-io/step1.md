# Writing Arrays to Files

NumPy provides several functions for writing arrays to files. The most common are `savetxt` and `save`.

## Open the Python Shell

Open the Python shell by typing the following command in the terminal.

```bash
python3
```

## Import Numpy

NumPy is already installed，you can import it in your Python code:

```python
import numpy as np
```

## Using Savetxt

The `savetxt` function is used to write arrays to text files. Here is an example:

```python
data = np.random.rand(10, 5)
np.savetxt('data.txt', data, delimiter=',')
```

- This will write the contents of `data` to a text file called `data.txt`, separating the values by `commas`.

## Using save

The `save` function is used to write arrays to binary files. Here is an example:

```python
np.save('data.npy', data)
```

- This will write the contents of `data` to a binary file called `data.npy`.
