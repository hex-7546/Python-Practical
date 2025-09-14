t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
t2 = (11, 13, 15)

# a. Print half the values of the tuple in one line, other half in the next line
half = len(t1) // 2
print("First half:", t1[:half])
print("Second half:", t1[half:])

# b. Print another tuple of only even numbers from t1
even_numbers = tuple(x for x in t1 if x % 2 == 0)
print("Even numbers tuple:", even_numbers)

# c. Concatenate tuple t2 with t1
concatenated_tuple = t1 + t2
print("Concatenated tuple:", concatenated_tuple)

# d. Return maximum and minimum values from t1
max_value = max(t1)
min_value = min(t1)
print("Maximum value in t1:", max_value)
print("Minimum value in t1:", min_value)
