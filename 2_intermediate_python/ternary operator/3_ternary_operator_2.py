# Create a Python function check_leap_year that takes a year as input 
# and uses a ternary operator to determine if it's a leap year. 
# Return "Leap Year" if it is, otherwise "Not a Leap Year." 
# (A leap year is divisible by 4, except for years divisible by 100 but not 
# divisible by 400).

def check_leap_year(year):
    """
    Check if a given year is a leap year or not.

    A leap year is a year that is divisible by 4, except for years that are exactly
    divisible by 100. However, years divisible by 400 are still considered leap years.

    Args:
        year (int): The year to be checked.

    Returns:
        str: "Leap Year" if the input year is a leap year, "Not a Leap Year" otherwise.

    """
    return "Leap Year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "Not a Leap Year"

def main():
    print(check_leap_year(1000))
    print(check_leap_year(2024))
    print(check_leap_year(1600))
    print(check_leap_year(1700))

if __name__ == "__main__":
    main()