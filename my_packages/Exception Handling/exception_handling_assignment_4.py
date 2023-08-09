# Implement a program that reads user input for a password. Create a custom
# exception WeakPasswordError to handle cases where the password is shorter
# than 8 characters

class WeakPasswordError(Exception):
    pass


def check_password_strength(password):
    """
    Check the strength of the password.

    Args:
        password (str): The password provided by the user.

    Raises:
        WeakPasswordError: If the password is shorter than 8 characters.

    """
    if len(password) < 8:
        raise WeakPasswordError(
            "Error: Password must be at least 8 characters long.")


def main():
    try:
        password = input("Enter your password: ")
        check_password_strength(password)
        print("Password is strong and accepted.")
    except WeakPasswordError as wpe:
        print(wpe)


if __name__ == "__main__":
    main()
