# Solution

## Step 1 Solution

```python
def sum_n(n: int) -> int:
    """
    Get the sum of the first n integers.

    Args:
        n (int): The number of integers to sum.

    Returns:
        (int): The sum of the first n integers.
    """

    return sum(i for i in range(n))
```

## Step 2 Solution

```python
def concat_strings(strings: list) -> str:
    """
    Return a string containing all the strings concatenated together.

    Args:
        strings (list): List of strings.

    Return:
        str: String containing all the strings concatenated together.
    """

    return ''.join(strings)
```

## Step 3 Solution

```python
def get_grade(score: int) -> str:
    """
    Calculates the grade of a student based on their score.

    Args:
    score (int): The score of the student.

    Returns:
    str: The grade of the student ('A', 'B', 'C', 'D', or 'E').
    """
    grades = {90: 'A', 80: 'B', 70: 'C', 60: 'D'}
    return grades.get(next(key for key in grades if score >= key), 'E')
```

## Step 4 Solution

```python
def sum_two_lists(list1: list, list2: list) -> list:
    """
    Element-wise sum of two input lists.
    Args:
        list1 (list): The first list of numbers to be summed.
        list2 (list): The second list of numbers to be summed, of equal length to `list1`.

    Returns:
        list: A new list containing the element-wise sum of `list1` and `list2`.

    """
    sum_list = [x + y for x, y in zip(list1, list2)]
    return sum_list
```

## Step 5 Solution

```python
def flatten_list(nested_list: list) -> list:
    """
    Flatten a nested list and convert it to a one-dimensional list.

    Args:
        nested_list (list): A nested list containing elements of any type.

    Return:
        list: A one-dimensional list containing all the elements from the nested list.
    """
    return [item for sublist in nested_list for item in sublist]
```
