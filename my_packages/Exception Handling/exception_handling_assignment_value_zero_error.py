"""
Write a Python program that takes two integers as input and performs division (num1
/ num2). Handle both ValueError (if non-integer input) and ZeroDivisionError and
display appropriate error messages.
"""

def perform_division(num1, num2):
    """
    Perform division (num1 / num2) and handle ZeroDivisionError.

    Args:
        num1 (int): The numerator.
        num2 (int): The denominator.

    Returns:
        float: The result of the division.

    Raises:
        ValueError: If num2 is not an integer.
        ZeroDivisionError: If num2 is zero.
    """
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError as exc:
        raise ZeroDivisionError('Cannot divide by zero') from exc
    except ValueError as exc:
        raise ValueError('Both numbers must be integers') from exc

def main():
    """
    This is the main function.
    """
    while True:
        try:
            num1 = input("Enter the numerator (or 'q' to quit): ")
            if num1 == 'q':
                break
            num1 = int(num1)

            num2 = int(input("Enter the denominator: "))

            result = perform_division(num1, num2)
            print("Result of the division:", result)
        except ValueError as value_error:
            print("Value Error:", value_error)
        except ZeroDivisionError as zde:
            print("Zero Division Error:", zde)
if __name__ == "__main__":
    main()
