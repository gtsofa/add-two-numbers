
import unittest

from addTwoNumbers import Addition

class TestAddNumbers(unittest.TestCase):
    """Test adding two numbers functionality"""
    def setUp(self):
        """we need the Addition object to be avaible in each test case hence we initialize setUp method."""
        self.calc = Addition()
    def test_add_two_numbers_method_return_correct_results(self):
        # result = 2 + 2
        result = self.calc.addNumbers(2,'three')
        self.assertEqual(4, result)

    def test_addition_returns_error_message_if_inputs_are_not_numbers(self):
        self.assertRaises(ValueError, self.calc.addNumbers, 'two', 'three')

    def test_addition_returns_error_message_if_a_is_not_number(self):
        self.assertRaises(ValueError, self.calc.addNumbers, 'two', 3)

    def test_addition_returns_error_message_if_a_is_not_number(self):
        self.assertRaises(ValueError, self.calc.addNumbers, 2, 'three')
    # def test_is_an_integer(self):
    #     type(self) == int
    # def test_subtraction(self):
    #     self.assertEqual(addTwoNumbers(6, 2), 8)
    #     self.assertEqual(addTwoNumbers(-3, 1), -2)
    #     self.assertEqual(addTwoNumbers(7, -2), 5)
if __name__ == '__main__':
    unittest.main()
