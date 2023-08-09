# Given a list of strings, create a new list that contains only the
# strings with more than 5 characters using list comprehension.

def create_new_list(input_list):
    """
        Create a new list containing elements with a length greater than 5.

        Args:
            input_list (List[str]): The input list of strings.

        Returns:
            List[str]: A new list containing elements from the input list that have a length greater than 5.
    """
    new_list = [i for i in input_list if len(i)>5]
    return new_list

def main():
    print(create_new_list(["apple", "banana", "grape", "watermelon", "kiwi", "orange"]))
    print(create_new_list(['Apple','ball','cat','dog','Elephant',"Fisher"]))

if __name__ == "__main__":
    main()