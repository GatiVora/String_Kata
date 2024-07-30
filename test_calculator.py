import unittest
from calculator import add

class TestAbsFunction(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_single_number(self):
        self.assertEqual(add("1"), 1)

    def test_zero(self):
        self.assertEqual(add("0,5"), 5)

    def test_two_numbers(self):
        self.assertEqual(add("1,5"), 6)

    def test_newline_between_numbers(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_newline_delimiter(self):
        self.assertEqual(add("1\n2\n3"), 6)
    
    def test_many_numbers(self):
        self.assertEqual(add("1,2,3\n4,5,6\n7,8,9,10"), 55)

    def test_multiple_diff_delimiters(self):
        self.assertRaises(ValueError, add, "1,\n2")

    def test_multiple_delimiter(self):
        self.assertRaises(ValueError, add, "1,2;3")
    
    def test_multiple_delimiter_in_row(self):
        self.assertRaises(ValueError, add, "1,2,,3")

    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)
    
    def test_multiple_newline(self):
        self.assertRaises(ValueError, add, "//\n\n1;2")
    
    def test_noninteger(self):
        self.assertRaises(ValueError, add, "a,b,c")

if __name__ == "__main__":
    unittest.main(verbosity=2)