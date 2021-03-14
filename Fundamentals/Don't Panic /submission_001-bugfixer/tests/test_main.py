import unittest
import troll_hunter
from troll_hunter import TheyreEatingHer
from troll_hunter import ThenTheyreGoingToEatMe


class TestNaughtyPup(unittest.TestCase):

    def test_troll_check_replace(self):
        text = """Returns a copy of the string `text` with the substring 'goblin' replaced
            with 'elf' and the substring 'hobgoblin' replaced with 'orc'."""
        response = troll_hunter.troll_check(text)
        shouldbe = """Returns a copy of the string `text` with the substring 'elf' replaced
            with 'elf' and the substring 'orc' replaced with 'orc'."""
        self.assertEqual(shouldbe,response,'goblin and hobgoblin should have been replaced')

    def test_troll_check_raise_troll(self):
        text = """Returns a copy of the string `text` with the substring 'goblin' replaced
            with 'elf' and the substring 'hobgoblin' replaced with 'orc'.

            Raises `TheyreEatingHer` if the substring 'troll' is found in `text`.
            Raises `ThenTheyreGoingToEatMe` if the substring 'Nilbog' is found in
            `text`, and the substring 'troll' is not found in `text`."""
        try:
            response = troll_hunter.troll_check(text)
            self.fail('should have raised TheyreEatingHer')
        except Exception as ex:
            #all good! test class
            self.assertIsInstance(ex,TheyreEatingHer,'should have raised TheyreEatingHer')

    def test_troll_check_raise_nilbog(self):
        text = """Returns a copy of the string `text` with the substring 'goblin' replaced
            with 'elf' and the substring 'hobgoblin' replaced with 'orc'.

            Raises `ThenTheyreGoingToEatMe` if the substring 'Nilbog' is found """
        try:
            response = troll_hunter.troll_check(text)
            self.fail('should have raised ThenTheyreGoingToEatMe')
        except Exception as ex:
            #all good! test class
            self.assertIsInstance(ex,ThenTheyreGoingToEatMe,'should have raised ThenTheyreGoingToEatMe')

    def test_print_troll_checked(self):
        filename="tests/test0.txt"
        self.assertEqual(troll_hunter.print_troll_checked(filename),0,'Should have returned 0')
        filename="tests/test1.txt"
        self.assertEqual(troll_hunter.print_troll_checked(filename),1,'Should have returned 1')
        filename="tests/test1b.txt"
        self.assertEqual(troll_hunter.print_troll_checked(filename),1,'Should have returned 1')
        filename="tests/test2.txt"
        self.assertEqual(troll_hunter.print_troll_checked(filename),-1,'Should have returned -1')

    def test_scan_directory(self):
        nr_trolls = troll_hunter.scan_directory("tests/test", [".tst"], True)
        self.assertEqual(nr_trolls, 1, "total troll files must be 1 with .tst")

        nr_trolls = troll_hunter.scan_directory("tests/test", [], True)
        self.assertEqual(nr_trolls, 0, "total troll files must be 0 without .tst")

        nr_trolls = troll_hunter.scan_directory("tests/test", [".tst"], False)
        self.assertEqual(nr_trolls, 1, "total troll files must be 1 without defaults")


if __name__ == '__main__':
    unittest.main()
