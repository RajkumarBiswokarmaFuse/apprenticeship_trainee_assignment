"""
This program demonstates a exception handling.
"""

import argparse


def display_file_contents(filename):
    """
    Display the contents of the file with the given filename.

    Args:
        filename (str): The name of the file to be opened and read.

    Raises:
        FileNotFoundError: If the file is not found.
    """
    # pylint: disable=unspecified-encoding
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError as fnfe:
        raise FileNotFoundError(
            f"Error: File '{filename}' not found.") from fnfe


def main():

    """
    This is the main function.
    """
    parser = argparse.ArgumentParser(
        description='Display the contents of a file.')
    parser.add_argument('filename', type=str,
                        help='The name of the file to be displayed.')
    args = parser.parse_args()

    try:
        display_file_contents(args.filename)
    except FileNotFoundError as fnfe:
        print(fnfe)
    except ValueError as value:
        print("Value Error:", value)


if __name__ == "__main__":
    main()
