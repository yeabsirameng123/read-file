import sys

# Function to read from command line arguments
def read_from_command_line():
    if len(sys.argv) < 2:
        return None  # No command line arguments
    return ' '.join(sys.argv[1:])

# Function to read from a text file
def read_from_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None  # File not found

if __name__ == "__main":
    input_from_command_line = read_from_command_line()
    if input_from_command_line:
        print("Input from command line:", input_from_command_line)
    else:
        print("No command line arguments provided.")

    file_path = "sample.txt"  # Replace with the path to your text file
    input_from_file = read_from_text_file(file_path)
    if input_from_file:
        print("Input from text file:")
        print(input_from_file)
    else:
        print(f"File '{file_path}' not found.")
