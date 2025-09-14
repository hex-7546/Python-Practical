import re

class InvalidNameError(Exception):
    """Custom exception for invalid names."""
    pass

def validate_name(name):
    """
    Validate that the name contains only alphabets and spaces.
    Raises InvalidNameError if validation fails.
    """
    if not name:
        raise InvalidNameError("Name cannot be empty.")
    
    # Regular expression to allow only letters and spaces
    if not re.fullmatch(r"[A-Za-z ]+", name):
        raise InvalidNameError("Name must contain only alphabets and spaces.")
    
def get_name():
    """
    Prompt user to enter a name and validate it.
    Handle exceptions if invalid characters are present.
    """
    try:
        name = input("Enter your name: ")
        validate_name(name)
        print(f"Hello, {name}!")
    except InvalidNameError as e:
        print(f"Invalid name entered: {e}")

# Run the function
get_name()
