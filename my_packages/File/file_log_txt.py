"""
    Create a function search_log that takes a log file and
    a search keyword as input.
    The function should find and display all lines containing
    the search keyword.
"""


def search_log(log_file, search_keyword):
    """
    Find and display all lines containing the search keyword in the log file.

    Args:
        log_file (str): The name of the log file.
        search_keyword (str): The keyword to search for in the log file.


    """
    # pylint: disable=unspecified-encoding
    try:
        with open(log_file, 'r') as file:
            lines = file.readlines()

        found_lines = [f"[{i + 1}] {line.strip()}"
                       for i, line in enumerate(lines)
                       if search_keyword in line.lower()]

        if found_lines:
            print(f"Found {len(found_lines)} lines containing \
                '{search_keyword}' "
                  f"in the log file '{log_file}':")
            for line in found_lines:
                print(line)
        else:
            print(
                f"No lines containing '{search_keyword}' \
                    found in the log file '{log_file}'.")
    except FileNotFoundError:
        print(f"Error: File '{log_file}' not found.")


def main():
    """This is a main function."""
    search_log("./data/log.txt", "error")
    search_log("./data/log.txt", "assist")
    search_log("./data/log.txt", "fusemachines")


if __name__ == "__main__":
    main()
