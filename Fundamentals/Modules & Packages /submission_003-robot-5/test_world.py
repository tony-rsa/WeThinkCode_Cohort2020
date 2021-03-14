import unittest
from io import StringIO
from unittest.mock import patch
from world.text.world import *
import robot

class Mytest(unittest.TestCase):

    def test_is_position_allowed(self):
        new_x = 254125
        new_y = 52
        result = is_position_allowed(new_x, new_y, 5000, 52)
        self.assertEqual(result, (False, False))

        new_x = 25
        new_y = 52
        result = is_position_allowed(new_x, new_y, 55, 52)
        self.assertEqual(result, (True, False))

    def test_update_position(self):
        steps = 50
        position_x = 0
        position_y = 0
        current_direction_index = 2
        result = update_position(steps, position_x, position_y, current_direction_index)
        self.assertEqual(result, (True, False, 0, -50))

    @patch("sys.stdin", StringIO("Hal\nForward 10\nforward 5\nreplay\noff"))
    def test_print_obstacles(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        obstacles.random.randint = lambda a, b: 1
        robot.robot_start()
        output = sys.stdout.getvalue()
        self.assertEqual(output,"What do you want to name your robot? Hal: Hello kiddo!\nHal: Loaded obstacles.\nThere are some obstacles:\n- At position 1,1 (to 5,5)\nHal: What must I do next?  > Hal moved forward by 10 steps.\n > Hal now at position (0,10).\nHal: What must I do next?  > Hal moved forward by 5 steps.\n > Hal now at position (0,15).\nHal: What must I do next?  > Hal moved forward by 10 steps.\n > Hal now at position (0,25).\n > Hal moved forward by 5 steps.\n > Hal now at position (0,30).\n > Hal replayed 2 commands.\n > Hal now at position (0,30).\nHal: What must I do next? Hal: Shutting down..\n")

    @patch("sys.stdin", StringIO("Hal\nForward 10\noff"))
    def test_show_position(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        obstacles.random.randint = lambda a, b: 1
        robot.robot_start()
        output = sys.stdout.getvalue()
        self.assertEqual(output,"What do you want to name your robot? Hal: Hello kiddo!\nHal: Loaded obstacles.\nThere are some obstacles:\n- At position 1,1 (to 5,5)\nHal: What must I do next?  > Hal moved forward by 10 steps.\n > Hal now at position (0,10).\nHal: What must I do next? Hal: Shutting down..\n")

    def test_return_obst_import(self):
        result = return_obst_import()
        self.assertEqual(result != None, True)