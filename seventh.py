def find_all_occurrences(main_string, substring):
    """
    Find all occurrences of substring in main_string and return their indices.
    
    Args:
        main_string (str): The string to search in
        substring (str): The string to search for
    
    Returns:
        list or int: List of indices where substring occurs, or -1 if not found
    """
    if not substring:  # Handle empty substring
        return -1
    
    indices = []
    start = 0
    
    while True:
        # Find the next occurrence starting from 'start'
        index = main_string.find(substring, start)
        
        if index == -1:  # No more occurrences found
            break
            
        indices.append(index)
        start = index + 1  # Move start position to search for overlapping occurrences
    
    # Return -1 if no occurrences found, otherwise return the list of indices
    return indices if indices else -1

# Example usage
result = find_all_occurrences("hello world hello universe hello", "hello")
print(result)

