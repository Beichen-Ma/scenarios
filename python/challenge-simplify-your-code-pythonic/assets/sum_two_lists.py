def sum_two_lists(list1: list, list2: list) -> list:
    """
    Element-wise sum of two input lists.
    Args:
        list1 (list): The first list of numbers to be summed.
        list2 (list): The second list of numbers to be summed, of equal length to `list1`.

    Returns:
        list: A new list containing the element-wise sum of `list1` and `list2`.

    """
    sum_list = []
    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])
    return sum_list