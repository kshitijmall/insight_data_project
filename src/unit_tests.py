import unittest
from pharmacy_main import compare_name


class PharmacyTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def compare_name(self):
        """Is b > a on comparison?"""
        res = compare_name("a", "b")
        print(res)
        self.assertEqual(res, 1)


if __name__ == '__main__':
    unittest.main()
