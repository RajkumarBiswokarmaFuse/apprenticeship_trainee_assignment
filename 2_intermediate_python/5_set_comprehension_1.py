# Given a list of numbers, 
# create a set using set comprehension that contains only unique even numbers.

def unique_even(input_list):
    """
        Get a set of unique even numbers from the input list.

        Args:
            input_list (List[int]): The input list of integers.

        Returns:
            set: A set containing only the unique even numbers from the input list.
    """
    new_set = (i for i in input_list if i % 2 == 0)
    return set(new_set)

def main():
    print(unique_even([2,4,2,4,2,34,10]))
    print(unique_even([1,11,111,2,22,222,3,33,333]))

if __name__ == "__main__":
    main()