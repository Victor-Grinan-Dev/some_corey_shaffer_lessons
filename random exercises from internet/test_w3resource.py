from SDA_studies.Autoestudio import solved_w3resourse as sw3
import unittest

class TestW3resourse(unittest.TestCase):

    def test_diferent_numbers(self):
        self.assertFalse(sw3.w3resourse.different_numbers([3,4,5,5,6,7]))
        self.assertTrue(sw3.w3resourse.different_numbers([3, 4, 2, 5, 6, 7]))

    def test_possible_strings(self):
        pass

if __name__ == '__main__':
    unittest.main