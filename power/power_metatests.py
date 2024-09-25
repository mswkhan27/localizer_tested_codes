import unittest
from hypothesis import strategies as st
from hypothesis import given, settings
from power import power


class MyTestCase(unittest.TestCase):
    b = 100

    @given(x=st.integers(min_value=0, max_value=b),
           y=st.integers(min_value=0, max_value=b),
           z=st.integers(min_value=0, max_value=b))
    @settings(max_examples=1000)
    def test_something(self, x, y, z):
        seed = power(x, y) * power(x, z)
        morphed = power(x, y + z)
        print(x, y, z, seed, morphed)
        self.assertEqual(seed, morphed)  # add assertion here


if __name__ == '__main__':
    unittest.main()
