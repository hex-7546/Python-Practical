text = input("Enter a sentence: ")
char = input("Enter a char to check frequency: ")

count = 0
 
for c in text:
    if c == char:
        count += 1

print(f"The char {char} in the sentence {text} appears {count} times")