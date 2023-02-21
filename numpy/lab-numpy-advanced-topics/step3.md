# Masked Arrays

Masked arrays are arrays that have a mask attached to them. The mask is an array of boolean values that indicate which elements of the array should be masked (hidden). NumPy provides the `np.ma` module for working with masked arrays.

## Creating a Masked Array

A masked array can be created using the `np.ma.masked_array()` function.

```python
# create an array with some values masked
a = np.ma.masked_array([1, 2, 3, 4], mask=[True, False, False, True])

print(a) # Output: [-- 2 3 --]
```

## Applying a Mask

A mask can be applied to an array using the `np.ma.masked_where()` function.

```python
# create an array
a = np.array([1, 2, 3, 4])

# create a mask
mask = a > 2

# apply the mask
b = np.ma.masked_where(mask, a)

print(b) # Output: [1 2 -- --]
```

## Masking Invalid Values

Masked arrays can be used to handle invalid values such as NaNs (not a number) or infinities.

```python
# create an array with some invalid values
a = np.array([1, np.nan, np.inf, 4])

# create a masked array
b = np.ma.masked_invalid(a)

print(b) # Output: [1.0 -- -- s4.0]
```

## Exercise

Now, please use the`np.ma`module provided by numoy to complete the creation of mask array. At the same time, use the `np.ma.masked_where()` function to apply the mask to the array, and finally use the `np.ma.masked_invalid()`to handle invalid values. Please complete this exercise.
