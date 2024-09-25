import unittest
from trityp import trityp

class MyTestCase(unittest.TestCase):
    def test_scalene(self):
        self.assertEqual(1, trityp(2, 4, 3))

    def test_isoscele(self):
        self.assertEqual(2, trityp(2, 2, 3))

    def test_equilateral(self):
        self.assertEqual(3, trityp(3, 3, 3))

    def test_invalid(self):
        self.assertEqual(4, trityp(-1, 2, 3))

if __name__ == '__main__':
    unittest.main()
