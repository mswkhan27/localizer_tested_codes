import unittest
from power import power

class MyTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(8, power(2, 3))

if __name__ == '__main__':
    unittest.main()



