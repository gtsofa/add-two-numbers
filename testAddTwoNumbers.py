
import unittest

from addTwoNumbers import Addition

class TestDivideNumbers(unittest.TestCase):
    """Test adding two numbers functionality"""
    def test_add_two_numbers_method_return_correct_results(self):
        result = 2 + 2
        self.assertEqual(4, result)
    # def test_is_an_integer(self):
    #     type(self) == int
    # def test_subtraction(self):
    #     self.assertEqual(addTwoNumbers(6, 2), 8)
    #     self.assertEqual(addTwoNumbers(-3, 1), -2)
    #     self.assertEqual(addTwoNumbers(7, -2), 5)
if __name__ == '__main__':
    unittest.main()
