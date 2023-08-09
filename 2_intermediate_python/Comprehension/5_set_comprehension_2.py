# Given two strings, write a Python program to create a set using set comprehension 
# that contains all the characters that are common in both strings.

def common_characters(string1, string2):
    """
    Create a set containing all the common characters in both strings.

    Args:
        string1 (str): The first input string.
        string2 (str): The second input string.

    Returns:
        set: A set containing all the characters that are common in both strings.

    
    """
   
    common_chars = {char for char in string1 if char in string2}
    return common_chars

def main():
    print(common_characters("nepal","nepalese"))
    print(common_characters("Apple","Ant"))

if __name__ == "__main__":
    main()