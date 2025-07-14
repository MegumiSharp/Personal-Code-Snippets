def flatten(iterable):
    """
    Recursively flattens a nested iterable structure into a single flat list.
    
    This function takes an iterable containing nested lists, and returns a new list with all elements at the same level. It handles arbitrary  nesting depth and filters out None values.
    
    Examples:
        >>> flatten([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        
        >>> flatten([1, None, [2, [3, None, 4]]])
        [1, 2, 3, 4] 
    """

    # Initialize empty list to store flattened results
    result = []
    
    # Iterate through each item in the input iterable
    for item in iterable:
        # Skip None values - they are filtered out from the final result
        if item is None:
            continue
        
        if type(item) is not list:
            result.append(item)
        else:
            result += flatten(item)
    
    # Return the completely flattened list
    return result