from SDA_studies.Autoestudio import solved_internet_exercises
import unittest


class TestNotString(unittest.TestCase):

    def test_divisor(self):
        self.assertEqual(solved_internet_exercises.SomeOtherExcersices.divisors(12), [1, 2, 3, 4, 6, 12])


if __name__ == '__main__':
    unittest.main

