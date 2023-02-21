def dictionary_operations(input_dict: dict) -> dict:
    """
    This function performs the following operations on the input dictionary:
    1. Add a key-value pair {"new_key": "new_value"} to the dictionary.
    2. Remove the key "remove_key" and its corresponding value from the dictionary.
    3. Return the final dictionary.
    
    Args:
    input_dict: a dictionary to be manipulated
    
    Returns:
    The final manipulated dictionary.
    """
    input_dict["new_key"] = "new_value"
    input_dict.pop("remove_key", None)
    return input_dict