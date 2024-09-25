import unittest
from multiply2 import multiply2

class Multiply2Tests(unittest.TestCase):
    def test_something(self):
        assert multiply2(1, 1, 1) == 1

    def test_something1(self):
        assert multiply2(1, -1, 1) == -1

    def test_something2(self):
        assert multiply2(1, 1, -1) == -1

    def test_something3(self):
        assert multiply2(1, 2, 3) == 6

    def test_something4(self):
        assert multiply2(-1, 2, 3) == -6

    def test_something5(self):
        assert multiply2(1, 2, -3) == -6

    def test_something6(self):
        assert multiply2(-1, -2, 3) == 6

    def test_something7(self):
        assert multiply2(-1, 2, -3) == 6

    def test_something8(self):
        assert multiply2(1, -2, -3) == 6

    def test_something9(self):
        assert multiply2(-1, -2, -3) == -6

if __name__ == '__main__':
    unittest.main()
