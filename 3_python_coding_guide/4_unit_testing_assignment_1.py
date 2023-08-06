# Create a function that validates email addresses based on following set of rules:
# -Proper email format such as presence of “@”, no space in the address
# -Presence of valid email providers such as yahoo, gmail and outlook. Make sure
# there are no no disposable email providers such as yopmail.
# Write unit tests to validate different email addresses against the rules, including valid and
# invalid addresses (Use unittest module).

import re
import unittest

def validate_email(email):
    """
    Validate an email address based on the specified rules.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    # Regular expression pattern to match a valid email format
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # List of valid email providers
    valid_providers = ["yahoo", "gmail", "outlook"]

    # List of disposable email providers
    disposable_providers = ["yopmail", "example"]

    if not re.match(email_pattern, email):
        return False

    provider = email.split("@")[1].split(".")[0]
    if provider in disposable_providers:
        return False

    return provider in valid_providers

class TestEmailValidation(unittest.TestCase):
    def test_valid_emails(self):
        """
        Test for valid email addresses.
        """
        valid_emails = [
            "rajkumar@example.com",
            "mynameiskhan@gmail.com",
            "wearefusemachines.123@yahoo.com",
            "jamesbond007@outlook.com",
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(validate_email(email))

    def test_invalid_emails(self):
        """
        Test for invalid email addresses.
        """
        invalid_emails = [
            "raj.email@",
            "invalid@example",
            "janeman@yopmail.com",
            "msdhoni@.com",
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(validate_email(email))

if __name__ == "__main__":
    unittest.main()
