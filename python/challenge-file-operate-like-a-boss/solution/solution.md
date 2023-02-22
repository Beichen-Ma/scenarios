# Solution

## Step 1 Solution

```python
import os

def folder_create(folder: str) -> None:
    """
    This function create folder
    :param folder: The name of the folder to be created.
    :return: None
    """

    if os.path.isdir(folder):
        return
    os.mkdir(folder)
```

## Step 2 Solution

```python
import os
import shutil

def file_move(file: str, folder: str) -> None:
    """
    This function move file to a new location
    :param file: The name of the file to be moved.
    :param folder: The name of the folder to move the file to.
    :return: None
    """

    if os.path.isfile(file):
        if not os.path.isdir(folder):
            os.mkdir(folder)
        shutil.move(file, folder)
```

## Step 3 Solution

```python
import os
import shutil

def folder_delete(folder: str) -> int:
    """
    This function delete folder
    :param folder: The name of the folder to be deleted.
    :return: The count of files in folder.
    """
    file_len = len(os.listdir(folder))
    shutil.rmtree(folder)
    return file_len
```
