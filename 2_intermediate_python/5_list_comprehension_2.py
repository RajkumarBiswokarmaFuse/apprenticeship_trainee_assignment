# Given two lists of integers, create a list that contains the
# product of each element of the first list with the corresponding element in the
# second list using list comprehension.

def product(input_list_1, input_list_2):
    """
    Calculate the element-wise product of two input lists.

    Args:
        input_list_1 (List[int]): The first input list of integers.
        input_list_2 (List[int]): The second input list of integers.

    Returns:
        List[int]: A new list containing the element-wise products of corresponding elements
                   from the two input lists.

    """
    product_of_list = [x * y for x, y in zip(input_list_1, input_list_2)]
    return product_of_list

def main():
    print( product([1,2,3],[4,5,6]))
    print( product([1,2,3,6],[4,5,6,8]))

if __name__ == "__main__":
    main()
