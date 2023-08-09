# Write a Python function that takes an arbitrary number of positional
# arguments and returns the sum of all the numbers. Test your function with various
# input cases.

def sum_of_numbers(*args):
    """
        Calculate the sum of all the numbers passed as arguments.

        Parameters:
        *args: tuple of numbers
            Arbitrary number of positional arguments.

    Returns:
        int or float
            The sum of all the numbers passed as arguments.
    """
    return sum(args)

def main():
    # Test cases
    print(sum_of_numbers(1, 2, 3, 4))                 
    print(sum_of_numbers(10, 20, 30, 40, 50))        
    print(sum_of_numbers(1.5, 2.5, 3.5, 4.5))        
    print(sum_of_numbers(1, -2, 3, -4, 5))           
    print(sum_of_numbers(0, 0, 0, 0, 0, 0, 0))       
    print(sum_of_numbers())                          

if __name__ == "__main__":
    main()

