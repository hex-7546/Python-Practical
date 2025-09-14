def char_frequency(s, char):
    """
    Find the frequency of a character in a string.
    
    Args:
        s (str): The input string.
        char (str): The character to find frequency of.
        
    Returns:
        int: Frequency of the character in the string.
    """
    return s.count(char)

def replace_char(s, old_char, new_char):
    """
    Replace all occurrences of old_char by new_char in the string.
    
    Args:
        s (str): The input string.
        old_char (str): The character to be replaced.
        new_char (str): The character to replace with.
        
    Returns:
        str: Modified string with characters replaced.
    """
    return s.replace(old_char, new_char)

def remove_first_occurrence(s, char):
    """
    Remove the first occurrence of a character from the string.
    
    Args:
        s (str): The input string.
        char (str): The character to remove.
        
    Returns:
        str: Modified string with the first occurrence removed.
    """
    index = s.find(char)
    if index == -1:
        return s  # Character not found, return original string
    return s[:index] + s[index+1:]

def remove_all_occurrences(s, char):
    """
    Remove all occurrences of a character from the string.
    
    Args:
        s (str): The input string.
        char (str): The character to remove.
        
    Returns:
        str: Modified string with all occurrences removed.
    """
    return s.replace(char, '')


# Example usage:
input_str = "abracadabra"
char_to_find = 'a'
char_to_replace_old = 'a'
char_to_replace_new = 'o'
char_to_remove = 'b'

print(f"Original string: {input_str}")
print(f"Frequency of '{char_to_find}': {char_frequency(input_str, char_to_find)}")
print(f"Replace '{char_to_replace_old}' by '{char_to_replace_new}': {replace_char(input_str, char_to_replace_old, char_to_replace_new)}")
print(f"Remove first occurrence of '{char_to_remove}': {remove_first_occurrence(input_str, char_to_remove)}")
print(f"Remove all occurrences of '{char_to_remove}': {remove_all_occurrences(input_str, char_to_remove)}")

