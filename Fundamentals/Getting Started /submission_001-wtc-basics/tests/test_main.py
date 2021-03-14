import unittest
from test_base import captured_output
from io import StringIO
import hello


class MyTestCase(unittest.TestCase):
    def test_step1(self):
        with captured_output() as (out, err):
            hello.print_hello()
        # This can go inside or outside the `with` block
        output = out.getvalue().strip()
        self.assertEqual(output, "Hello World!")


if __name__ == '__main__':
    unittest.main()
