def list_operations(input_list: list) -> list:
    """
    This function performs the following operations on the input list:
    1. Sort the list in ascending order.
    2. Remove duplicates from the list.
    3. Return the final list.
    
    Args:
    input_list: a list of integers to be manipulated
    
    Returns:
    The final manipulated list.
    """
    input_list = list(set(input_list))
    input_list.sort()
    return input_list