# Write a Python function calculate_factorial that takes an integer as input
# and uses the reduce function to return the factorial of that number

from functools import reduce

def calulate_factorial(number):
    """
        Calculate the factorial of a given number.

        Args:
            number (int) : non - negative number for which factorial is to be calculated.

        Returns:
            int : The factorial of the given input number 
    """
    return reduce(lambda x, y: x * y, range(1,number+1,1), 1)

def main():
    print(calulate_factorial(12))
    print(calulate_factorial(5))
    print(calulate_factorial(10))

if __name__ == "__main__":
    main()