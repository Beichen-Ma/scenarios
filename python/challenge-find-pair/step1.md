# Find Pair

You are given a list of integers and a target value. Your task is to implement a function 'find_pair()' that takes in the list of integers and the target value as parameters, and returns a tuple containing the indices of two elements in the list that add up to the target value. If there are multiple valid pairs, the function should return the indices of the first valid pair encountered.

## Input

- `nums` - A list of integers `n (2 <= n <= 10^3)` where each integer is within the range `[-10^3, 10^3]`.
- `target` - An integer `t (-10^3 <= t <= 10^3)`.

## Output

- A tuple containing two integers `i` and `j` where `0 <= i, j <= n-1` and `i != j`.
- If there are no valid pairs, the function should return an empty tuple `()`.
- If there are multiple valid pairs, the function should return the indices of the first valid pair encountered.

## Example

```python
nums = [2, 7, 11, 15]
target = 9
assert find_pair(nums, target) == (0, 1)
```

In this example, the pair of elements at indices `0` and `1` add up to the target value of `9`.

```python
nums = [3, 2, 4]
target = 6
assert find_pair(nums, target) == (1, 2)
```

In this example, the pair of elements at indices `1` and `2` add up to the target value of `6`.

```python
nums = [3, 3]
target = 6
assert find_pair(nums, target) == (0, 1)
```

In this example, the pair of elements at indices `0` and `1` add up to the target value of `6`. Note that there are no other valid pairs.

```python
nums = [1, 2, 3, 4, 5]
target = 10
assert find_pair(nums, target) == ()
```

In this example, there are no valid pairs that add up to the target value of `10`. The function should return an empty tuple.