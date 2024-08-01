import unittest
from calculator import add

class TestCalcFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(add(""),0)

if __name__ == "__main__":
    unittest.main(verbosity=2)