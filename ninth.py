def file_stats(filename):
    """
    Reads a file and prints the total number of characters, words, and lines.
    
    Args:
        filename (str): Path to the file to read.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            
            # Count characters (including whitespace and newline)
            char_count = len(text)
            
            # Count words (split by whitespace)
            word_count = len(text.split())
            
            # Count lines
            file.seek(0)  # Reset file cursor to start
            line_count = sum(1 for line in file)
            
        print(f"Total characters: {char_count}")
        print(f"Total words: {word_count}")
        print(f"Total lines: {line_count}")
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# Replace 'example.txt' with your file path
# file_stats('example.txt')
