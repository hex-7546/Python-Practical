def print_cubes_dict():
    """
    Creates and prints a dictionary with keys 1 to 5 and values as cubes of the keys.
    """
    cubes_dict = {}
    for num in range(1, 6):
        cubes_dict[num] = num ** 3
    
    print(cubes_dict)

# Example usage
print_cubes_dict()
