"""
    Create a function add_to_json that takes a filename and a dictionary as input. The
    should read the JSON data from the file, add the new dictionary to it, and
    write the updated data back to the same file
"""

import json

def add_to_json(filename, new_data):
    """
    Read JSON data from the file, add the new dictionary, and write back to the same file.

    Args:
        filename (str): The name of the JSON file.
        new_data (dict): The dictionary to be added to the JSON data.

    
    """
    # pylint: disable=unspecified-encoding
    try:
        # Read the existing JSON data from the file
        with open(filename, 'r') as file:
            json_data = json.load(file)

        # Add the new data to the existing JSON data
        json_data.append(new_data)

        # Write the updated JSON data back to the file
        with open(filename, 'w') as file:
            json.dump(json_data, file, indent=4)

        print("JSON data updated successfully in the file:", filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in the file '{filename}'.")

def main():
    """
        This is a main function
    """
    add_to_json("./data/data.json", {"name": "raj", "age": 24})
    add_to_json("./data/data.json", {"name": "kumar", "age": 25})


if __name__ == "__main__":
    main()
