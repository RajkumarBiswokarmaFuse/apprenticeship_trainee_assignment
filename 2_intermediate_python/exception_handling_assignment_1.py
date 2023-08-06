def perform_division(num1, num2):
    """
    Perform division (num1 / num2) and handle ZeroDivisionError.

    Args:
        num1 (int): The numerator.
        num2 (int): The denominator.

    Returns:
        float: The result of the division.

    Raises:
        ZeroDivisionError: If num2 is zero.
    """
    try:
        result = num1 / num2
    except ZeroDivisionError as exc:
        # Capture the exception and add custom handling if needed
        raise ZeroDivisionError(
            'Error: Division by zero is not allowed.') from exc
    return result


def main():
    while True:
        try:
            num1 = input("Enter the numerator (or 'q' to quit): ")
            if num1 == 'q':
                break

            num2 = int(input("Enter the denominator: "))

            # Call the function and perform division
            result = perform_division(int(num1), num2)
            print("Result of the division:", result)
        except ZeroDivisionError as zde:
            print(zde)


if __name__ == "__main__":
    main()
