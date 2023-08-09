# Design a function that takes a list of numerical data and performs calculations for mean,
# median and standard deviation. Write unit tests to verify the correctness of the statistical
# calculations for various inputs, including edge cases like an empty list or a list with one
# element (Use unittest module).

import unittest
import math

def calculate_statistics(data):
    """
    Calculate the mean, median, and standard deviation of a list of numerical data.

    Args:
        data (list): The list of numerical data.

    Returns:
        tuple: A tuple containing the mean, median, and standard deviation.
    """
    if not data:
        raise ValueError("The input list is empty.")

    n = len(data)
    mean = sum(data) / n

    sorted_data = sorted(data)
    if n % 2 == 0:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median = sorted_data[n // 2]

    variance = sum((x - mean) ** 2 for x in data) / n
    std_deviation = math.sqrt(variance)

    return mean, median, std_deviation

class TestStatisticsCalculations(unittest.TestCase):
    def test_mean_median_std_deviation(self):
        """
        Test the calculations of mean, median, and standard deviation.
        """
        test_data = [2, 4, 6, 8, 10]

        mean, median, std_deviation = calculate_statistics(test_data)
        self.assertEqual(mean, 6)
        self.assertEqual(median, 6)
        self.assertAlmostEqual(std_deviation, 2.8284271247461903, places=4)

    def test_empty_list(self):
        """
        Test with an empty list.
        """
        with self.assertRaises(ValueError):
            calculate_statistics([])

    def test_single_element_list(self):
        """
        Test with a list containing a single element.
        """
        test_data = [5]

        mean, median, std_deviation = calculate_statistics(test_data)
        self.assertEqual(mean, 5)
        self.assertEqual(median, 15)
        self.assertAlmostEqual(std_deviation, 0, places=4)

if __name__ == "__main__":
    unittest.main()
