# Given two lists - one containing keys and another
# containing values, create a dictionary using dictionary comprehension

def new_dict(keys, values):
    """
    Create a new dictionary by pairing corresponding elements from the key and value lists.

    Args:
        keys (List[str]): The list of keys.
        values (List[Any]): The list of corresponding values.

    Returns:
        dict: A new dictionary with keys and values paired from the input lists.

    
    """
    new_dict = dict(zip(keys, values))
    return new_dict

def main():
    print(new_dict(["Item1","Item2","Item3"],[100,200,300]))
    print(new_dict(['name', 'age', 'city'], ['Raj', 24, 'Rupandehi']))

if __name__ == "__main__":
    main()
