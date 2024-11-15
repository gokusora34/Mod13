import unittest
import re
from datetime import datetime

# Validation functions
def is_valid_symbol(symbol):
    return bool(re.fullmatch(r'[A-Z]{1,7}', symbol))

def is_valid_chart_type(chart_type):
    return chart_type in {'1', '2'}

def is_valid_time_series(time_series):
    return time_series in {'1', '2', '3', '4'}

def is_valid_date(date_string):
    if len(date_string) != 10:  # Strictly enforce YYYY-MM-DD format length
        return False
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False


# Unit test class
class TestInputValidation(unittest.TestCase):

    def test_symbol(self):
        # Valid symbols
        self.assertTrue(is_valid_symbol("AAPL"))
        self.assertTrue(is_valid_symbol("GOOGL"))
        self.assertTrue(is_valid_symbol("AMZN"))
        self.assertTrue(is_valid_symbol("XYZ"))
        self.assertTrue(is_valid_symbol("TESTER"))

        # Invalid symbols
        self.assertFalse(is_valid_symbol("appl"))  # lowercase
        self.assertFalse(is_valid_symbol("AAPL123"))  # more than 7 characters
        self.assertFalse(is_valid_symbol("1234567"))  # numeric
        self.assertFalse(is_valid_symbol("AA@#$%"))  # special characters
        self.assertFalse(is_valid_symbol(""))  # empty string

    def test_chart_type(self):
        # Valid chart types
        self.assertTrue(is_valid_chart_type("1"))
        self.assertTrue(is_valid_chart_type("2"))

        # Invalid chart types
        self.assertFalse(is_valid_chart_type("3"))  # out of range
        self.assertFalse(is_valid_chart_type("0"))  # out of range
        self.assertFalse(is_valid_chart_type(""))  # empty string
        self.assertFalse(is_valid_chart_type("12"))  # multiple characters

    def test_time_series(self):
        # Valid time series
        self.assertTrue(is_valid_time_series("1"))
        self.assertTrue(is_valid_time_series("2"))
        self.assertTrue(is_valid_time_series("3"))
        self.assertTrue(is_valid_time_series("4"))

        # Invalid time series
        self.assertFalse(is_valid_time_series("5"))  # out of range
        self.assertFalse(is_valid_time_series("0"))  # out of range
        self.assertFalse(is_valid_time_series("12"))  # multiple characters
        self.assertFalse(is_valid_time_series(""))  # empty string

    def test_start_date(self):
        # Valid dates
        self.assertTrue(is_valid_date("2024-11-08"))
        self.assertTrue(is_valid_date("2000-01-01"))
        self.assertTrue(is_valid_date("1999-12-31"))

        # Invalid dates
        self.assertFalse(is_valid_date("2024/11/08"))  # wrong separator
        self.assertFalse(is_valid_date("2024-13-01"))  # invalid month
        self.assertFalse(is_valid_date("2024-00-01"))  # invalid month
        self.assertFalse(is_valid_date("2024-02-30"))  # invalid day
        self.assertFalse(is_valid_date("08-11-2024"))  # wrong format
        self.assertFalse(is_valid_date("2024-11-8"))  # missing zero-padding
        self.assertFalse(is_valid_date(""))  # empty string

    def test_end_date(self):
        # Valid dates
        self.assertTrue(is_valid_date("2024-11-08"))
        self.assertTrue(is_valid_date("2000-01-01"))
        self.assertTrue(is_valid_date("1999-12-31"))

        # Invalid dates
        self.assertFalse(is_valid_date("2024/11/08"))  # wrong separator
        self.assertFalse(is_valid_date("2024-13-01"))  # invalid month
        self.assertFalse(is_valid_date("2024-00-01"))  # invalid month
        self.assertFalse(is_valid_date("2024-02-30"))  # invalid day
        self.assertFalse(is_valid_date("08-11-2024"))  # wrong format
        self.assertFalse(is_valid_date("2024-11-8"))  # missing zero-padding
        self.assertFalse(is_valid_date(""))  # empty string

# Run the tests
if __name__ == '__main__':
    unittest.main()
