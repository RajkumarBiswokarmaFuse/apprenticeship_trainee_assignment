# Implement a function called filter_prime_numbers that takes a list of integers as input 
# and uses the filter function to return a new list containing only the prime number

def is_prime(num):
    """
        Check whether given number is Prime or Not.

        Args:
            num (int) :  The number which need to be checked for primality.

        Returns: 
            bool : Return true/false based on whether it's prime ot not
    """
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def filter_prime_numbers(*number_list):
    """
        This function takes a variable number of integer arguments and filters out
        the prime numbers from the list of numbers.

        Args:
            *number_list (int): One or more integer arguments representing a list of numbers.

        Returns:
            list: A list containing only the prime numbers from the input number_list.
    """
    return list(filter(is_prime,number_list))

def main():
    print(filter_prime_numbers(1,2,3,4,5))
    print(filter_prime_numbers(5,56,43,78))

if __name__ == "__main__":
    main()