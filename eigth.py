def cubes_of_even_integers(input_list):
    """
    Create a list of cubes of even integers from the input list.
    
    Args:
        input_list (list): List containing elements of various types.
    
    Returns:
        list: List containing cubes of even integers.
    """
    result = []
    for item in input_list:
        # Check if the element is an integer and even
        if isinstance(item, int) and item % 2 == 0:
            cube = item ** 3
            result.append(cube)
    return result


# Example usage
input_list = [1, 2, 3.5, 4, 'hello', 6, 7, 8.0, 10, None]
output = cubes_of_even_integers(input_list)
print("Input list:", input_list)
print("Cubes of even integers:", output)
