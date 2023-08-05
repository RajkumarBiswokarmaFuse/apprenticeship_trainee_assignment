# Implement a program that takes user input for a filename, opens the file in read
# mode, and displays its contents. Handle the FileNotFoundError and display an error
# message if the file is not found.

import argparse

def display_file_contents(filename):
    """
    Display the contents of the file with the given filename.

    Args:
        filename (str): The name of the file to be opened and read.

    Raises:
        FileNotFoundError: If the file is not found.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{filename}' not found.")

def main():
    parser = argparse.ArgumentParser(description='Display the contents of a file.')
    parser.add_argument('filename', type=str, help='The name of the file to be displayed.')
    args = parser.parse_args()

    try:
        display_file_contents(args.filename)
    except FileNotFoundError as fnfe:
        print(fnfe)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
