import unittest
from math_quiz import get_random_integer_between, get_random_operator, solve


class TestMathGame(unittest.TestCase):

    def test_get_random_integer_between(self):
        """ 
        Test if random numbers generated are within the specified range
        :raises AssertionError: this function has code that raises a AssertionError when unit test fails
        """
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_integer_between(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operator(self):
        """ 
        Test if random operator generated are out of the valid operators
        :raises AssertionError: this function has code that raises a AssertionError when unit test fails
        """
        for _ in range(1000):
            rand_operator = get_random_operator()
            self.assertTrue(rand_operator in ["+", "-", "*"])

    def test_solve(self):
        """ 
        Test if the formulated problems and the answers are correct
        :raises AssertionError: this function has code that raises a AssertionError when unit test fails
        """
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (3, 2, '+', '3 + 2', 5),
            (2, 6, '+', '2 + 6', 8),
            (7, 2, '+', '7 + 2', 9),
            (5, 4, '+', '5 + 4', 9)]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = solve(num1, num2, operator)
            self.assertTrue(problem==expected_problem and answer==expected_answer)

if __name__ == "__main__":
    unittest.main()
