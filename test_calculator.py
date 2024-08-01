import unittest
from calculator import add

class TestCalcFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(add(""),0)

    def test_single_number(self):
        self.assertEqual(add("1"),1)

    def test_two_numbers(self):
        self.assertEqual(add("1,5"), 6)

    def test_newline_between_numbers(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_newline_delimiter(self):
        self.assertEqual(add("1\n2\n3"), 6)

    def test_many_numbers(self):
        self.assertEqual(add("1,2,3\n4,5,6\n7,8,9,10"), 55)

    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)

if __name__ == "__main__":
    unittest.main(verbosity=2)