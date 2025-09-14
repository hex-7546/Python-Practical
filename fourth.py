def get_digit_name(digit_char):
    """
    Returns the name of the digit character as text.
    """
    digit_names = {
        '0': 'ZERO',
        '1': 'ONE',
        '2': 'TWO',
        '3': 'THREE',
        '4': 'FOUR',
        '5': 'FIVE',
        '6': 'SIX',
        '7': 'SEVEN',
        '8': 'EIGHT',
        '9': 'NINE'
    }
    return digit_names.get(digit_char, "UNKNOWN")

def analyze_character(ch):
    """
    Analyzes the character and prints class and details.
    """
    if ch.isalpha():
        print(f"'{ch}' is a letter.")
        if ch.isupper():
            print("It is uppercase.")
        else:
            print("It is lowercase.")
    elif ch.isdigit():
        print(f"'{ch}' is a numeric digit.")
        print(f"Its name is {get_digit_name(ch)}.")
    else:
        print(f"'{ch}' is a special character.")

# Main program
char = input("Enter a single character: ")

if len(char) != 1:
    print("Error: Please enter exactly one character.")
else:
    analyze_character(char)
