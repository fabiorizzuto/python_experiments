import unittest
from calc import calculate_b
from compose_string import compose_string


class TestSweetBaum(unittest.TestCase):
    def test_calculate_b_4(self):
        self.assertEqual(1, calculate_b(4))

    def test_calculate_b_5(self):
        self.assertEqual(0, calculate_b(5))

    def test_calculate_b_19611206(self):
        self.assertEqual(0, calculate_b(19611206))

    def test_compose_string(self):
        self.assertEqual('1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0', compose_string(20))
