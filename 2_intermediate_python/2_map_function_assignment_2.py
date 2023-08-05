# Create a function convert_to_uppercase that takes a list of strings as input 
# and uses the map function to return a new list with all the strings converted 
# to uppercase.

def convert_to_uppercase(input_list):
    """
        Convert the given list of strings to upper_case.

        Parameter:
            input_list : List of integers to convert into uppercase

        Returns:
            list    : List containing the input strings converted to uppercase
    """
    return list(map(lambda x: x.upper(),input_list))

def main():
    print(convert_to_uppercase(['Apple','Ball','Cat']))
    print(convert_to_uppercase(['a','b','c','d']))


if __name__ =="__main__":
    main()