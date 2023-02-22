def concat_strings(strings: list) -> str:
    """
    Return a string containing all the strings concatenated together.

    Args:
        strings (list): List of strings.

    Return:
        str: String containing all the strings concatenated together.
    """

    string = ''
    for s in strings:
        string += s
    return string