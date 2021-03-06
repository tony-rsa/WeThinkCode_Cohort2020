import unittest
from unittest.mock import patch
from io import StringIO
import sys
import mastermind

class TestFunctions(unittest.TestCase):

    def test_code(self):
        for i in range(100):
            code = mastermind.create_code()
            count = 0
            for x in code:
                if (str(x).isdigit() == True) and (x != 9 and x != 0):
                    count += 1
            if count != 4:
                self.assertEqual(code, "Code is not 1 to 8 digits only")
            self.assertEqual(count, 4)


    def test_check_correctness(self):
        for i in range(5):
            if i == 4:
                self.assertEqual(mastermind.check_correctness(i), True)
            else:
                self.assertEqual(mastermind.check_correctness(i), False)


    @patch("sys.stdin", StringIO("12345\n1234\n"))
    def test_get_answer_input(self):
        old_output = sys.stdout
        sys.stdout = StringIO()
        mastermind.get_answer_input()
        result = sys.stdout.getvalue()
        sys.stdout = old_output
        self.assertEqual(result, "Input 4 digit code: Please enter exactly 4 digits.\nInput 4 digit code: ")


    @patch("sys.stdin", StringIO("12345\n1234\n"))
    def test_get_answer_input(self):
        code = [1, 2, 3, 4]
        old_output = sys.stdout
        sys.stdout = StringIO()
        mastermind.take_turn(code)
        value = sys.stdout.getvalue()
        self.assertEqual(value, "Input 4 digit code: Please enter exactly 4 digits.\nInput 4 digit code: Number of correct digits in correct place:     4\nNumber of correct digits not in correct place: 0\n")


if __name__ == "__main__":
        unittest.main()