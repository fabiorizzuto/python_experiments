import unittest
from major_scales import *


class TestMajorScales(unittest.TestCase):
    def test_c(self):
        self.assertEqual('C', note("C", "Do"))

    def test_d(self):
        self.assertEqual('D', note("C", "Re"))

    def test_d_major_scale(self):
        self.assertEqual(['D', 'E', 'F#', 'G', 'A', 'B', 'C#'], build_major_scale('D'))

    def test_e(self):
        self.assertEqual('E', note("C", "Mi"))

    def test_fsharp(self):
        self.assertEqual('F#', note("D", "Mi"))

    def test_dsharp(self):
        self.assertEqual('D#', note("A#", "Fa"))


if __name__ == '__main__':
    unittest.main()
