def sum_n(n: int) -> int:
    """
    Get the sum of the first n integers.

    Args:
        n (int): The number of integers to sum.

    Returns:
        (int): The sum of the first n integers.
    """

    s = 0
    for i in range(n):
        s += i
    return s