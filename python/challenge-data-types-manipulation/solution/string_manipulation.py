def string_manipulation(input_string: str) -> str:
    """
    This function performs the following operations on the input string:
    1. Convert the string to lowercase.
    2. Remove all whitespaces from the string.
    3. Reverse the string.
    4. Return the final string.
    
    Args:
    input_string: a string to be manipulated
    
    Returns:
    The final manipulated string.
    """
    input_string = input_string.lower().replace(" ", "")
    return input_string[::-1]