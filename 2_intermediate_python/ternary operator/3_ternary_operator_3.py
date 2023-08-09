# Write a function find_bigger_number that takes three integers as input and uses a
# ternary operator to return the larger number. If all numbers are equal, return Equal

def find_bigger_number(number1, number2, number3):
    """
    Find the biggest number among three given numbers.

    Args:
        number1 (int): The first number.
        number2 (int): The second number.
        number3 (int): The third number.

    Returns:
        int or str: The biggest number among the three. If all three numbers are equal,
                   it returns "Equal".

    """
    if number1 == number2 == number3:
        return 'Equal'
    else:
        return max(number1, number2, number3)
    
def main():
    print(find_bigger_number(8,7,6))
    print(find_bigger_number(7,7,7))
    print(find_bigger_number(8,9,87))

if __name__ == "__main__":
    main()