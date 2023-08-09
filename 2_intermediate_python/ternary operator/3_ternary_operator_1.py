# Write a Python function called check_odd_even that takes an integer as input and
# uses a ternary operator to return "Even" if the number is even, and "Odd" if the
# number is odd

def check_odd_even(number):
    """
    Check if a given number is odd or even.

    Args:
        number (int): The integer to be checked.

    Returns:
        str: "Even" if the input number is even, "Odd" if the input number is odd.

    """
    return "Even" if number % 2 == 0 else "Odd"

def main():
    print(check_odd_even(12))
    print(check_odd_even(111))
    print(check_odd_even(1010))

if __name__ == "__main__":
    main()

