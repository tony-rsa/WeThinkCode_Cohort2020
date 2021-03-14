import unittest
from io import StringIO
from unittest.mock import patch
import sys
from maze import hardcoded_maze as obstacles

class MyTest(unittest.TestCase):

    def test_get_obstacles(self):
        result = obstacles.get_obstacles()
        self.assertEqual(len(result) > 0, True)

    def test_is_position_blocked(self):
        obstacles.random.randint = lambda a,b : 1
        obstacles.get_obstacles()
        result = obstacles.is_position_blocked(1,1)
        self.assertEqual(result, False)
        result = obstacles.is_position_blocked(1,10)
        self.assertEqual(result, False)

    def check_greater(self):
        value1 = 1
        value2 = 5
        result = obstacles.check_greater(value1, value2)
        self.assertEqual(result, (value1, value2))
        result = obstacles.check_greater(value2, value1)
        self.assertEqual(result, (value1, value2))

    def test_is_path_blocked(self):
        obstacles.random.randint = lambda a,b : 1
        obstacles.get_obstacles()
        result = obstacles.is_path_blocked(1, 0, 1, 5)
        self.assertEqual(result, False)
        result = obstacles.is_path_blocked(10,10, 10, 20)
        self.assertEqual(result, True)