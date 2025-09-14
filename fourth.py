def swap_first_n_chars_compact(str1, str2, n):
    """Compact version using tuple unpacking"""
    if n <= 0:
        return str1, str2
    return str2[:n] + str1[n:], str1[:n] + str2[n:]


# Example usage
result1, result2 = swap_first_n_chars_compact("python", "java", 1)
print(f"result: '{result1}', '{result2}'")

