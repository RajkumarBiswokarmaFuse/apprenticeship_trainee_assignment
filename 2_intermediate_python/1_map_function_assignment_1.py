# Write a Python function square_numbers that takes a list of integers as
# input and uses the map function to return a new list containing the square of each
# element

def square_number(input_list):
    """
        Calculate the squares of the numbers in the input list.

        Parameters:
            input_list : a list of integer
                A list of numbers.

        Returns:
            list
                A list containing the squares of the numbers in the input list.
    """
    return list(map(lambda x:x**2, input_list))


def main():
    print(square_number([1,2,3,4,5]))
    print(square_number([12,11,23]))

if __name__ =="__main__":
    main()