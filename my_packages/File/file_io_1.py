"""
Implement a program that reads a CSV file named "data.csv," containing columns
"Name" and "Age." Create a new CSV file called "adults.csv" with only the rows of
individuals who are 18 years or older.

"""

import csv

def filter_adults(input_file, output_file):
    """
    Read data from the input CSV file and filter adults to create a new CSV file.

    Args:
        input_file (str): The name of the input CSV file.
        output_file (str): The name of the output CSV file.

    Example:
        >>> filter_adults("data.csv", "adults.csv")
        Adults filtered successfully. New file created: adults.csv
    """
    # pylint: disable=unspecified-encoding
    try:
        with open(input_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            adults = [row for row in reader if int(row['Age']) >= 18]

        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = ['Name', 'Age']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(adults)

        print("Adults filtered successfully. New file created:", output_file)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except ValueError:
        print("Error: Invalid 'Age' value found in the CSV file.")

def main():
    """
        This is a main function
    """
    input_file = "./data/data.csv"
    output_file = "./data/adults.csv"
    filter_adults(input_file, output_file)

if __name__ == "__main__":
    main()
