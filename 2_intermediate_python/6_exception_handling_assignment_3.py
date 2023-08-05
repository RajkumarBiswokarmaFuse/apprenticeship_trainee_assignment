# Write a Python program that takes two integers as input and performs division (num1
# / num2). Handle both ValueError (if non-integer input) and ZeroDivisionError and
# display appropriate error messages

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
    except ZeroDivisionError:
        raise ZeroDivisionError("Error: Division by zero is not allowed.")
    except TypeError:
        raise ValueError("Error: The second number should be an integer.")

def main():
    while True:
        try:
            num1 = int(input("Enter the numerator (or 'q' to quit): "))
            if num1 == 'q':
                break

            num2 = int(input("Enter the denominator: "))

            result = perform_division(num1, num2)
            print("Result of the division:", result)
        except ValueError as ve:
            print(ve)
        except ZeroDivisionError as zde:
            print(zde)
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
