def flatten_list(nested_list: list) -> list:
    """
    Flatten a nested list and convert it to a one-dimensional list.

    Args:
        nested_list (list): A nested list containing elements of any type.

    Return:
        list: A one-dimensional list containing all the elements from the nested list.
    """
    flattened_list = []
    for list_ in nested_list:
        for item in list_:
            flatten_list.append(item)
    return flattened_list
