import unittest
from io import StringIO
from unittest.mock import patch
import sys
import robot
from world import obstacles

class Mytest(unittest.TestCase):

   
    def test_keep_history(self):
        command = "forward 10"
        command_history = []
        result = robot.add_command_history(command, command_history)
        self.assertEqual(result, ['forward 10'])

    @patch("sys.stdin", StringIO("Hal\nForward 10\nforward 5\nreplay\noff"))
    def test_do_replay(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        obstacles.random.randint = lambda a, b: 0
        robot.robot_start()
        output = sys.stdout.getvalue()
        self.assertEqual(output,"What do you want to name your robot? Hal: Hello kiddo!\nHal: What must I do next?  > Hal moved forward by 10 steps.\n > Hal now at position (0,10).\nHal: What must I do next?  > Hal moved forward by 5 steps.\n > Hal now at position (0,15).\nHal: What must I do next?  > Hal moved forward by 10 steps.\n > Hal now at position (0,25).\n > Hal moved forward by 5 steps.\n > Hal now at position (0,30).\n > Hal replayed 2 commands.\n > Hal now at position (0,30).\nHal: What must I do next? Hal: Shutting down..\n")

    @patch("sys.stdin", StringIO("Hal\nForward 10\nforward 5\nreplay silent\noff"))
    def test_do_replay_silent(self):
        sys.stdout = StringIO()
        self.maxDiff = None
        obstacles.random.randint = lambda a, b: 0
        robot.robot_start()
        output = sys.stdout.getvalue()
        self.assertEqual(output, "What do you want to name your robot? Hal: Hello kiddo!\nHal: What must I do next?  > Hal moved forward by 10 steps.\n > Hal now at position (0,10).\nHal: What must I do next?  > Hal moved forward by 5 steps.\n > Hal now at position (0,15).\nHal: What must I do next?  > Hal replayed 2 commands silently.\n > Hal now at position (0,30).\nHal: What must I do next? Hal: Shutting down..\n")

    @patch("sys.stdin", StringIO("Hal\nForward 10\nforward 5\nreplay reversed\noff"))
    def test_do_replay_reversed(self):
        sys.stdout = StringIO()
        self.maxDiff = None
        obstacles.random.randint = lambda a, b: 0
        robot.robot_start()
        output = sys.stdout.getvalue()
        self.assertEqual(output, "What do you want to name your robot? Hal: Hello kiddo!\nHal: What must I do next?  > Hal moved forward by 10 steps.\n > Hal now at position (0,10).\nHal: What must I do next?  > Hal moved forward by 5 steps.\n > Hal now at position (0,15).\nHal: What must I do next?  > Hal moved forward by 5 steps.\n > Hal now at position (0,20).\n > Hal moved forward by 10 steps.\n > Hal now at position (0,30).\n > Hal replayed 2 commands in reverse.\n > Hal now at position (0,30).\nHal: What must I do next? Hal: Shutting down..\n")

    @patch("sys.stdin", StringIO("Hal\nForward 10\nforward 5\nreplay reversed silent\noff"))
    def test_do_replay_reversed_silent(self):
        sys.stdout = StringIO()
        obstacles.random.randint = lambda a, b: 0
        robot.robot_start()
        output = sys.stdout.getvalue()
        self.assertEqual(output, "What do you want to name your robot? Hal: Hello kiddo!\nHal: What must I do next?  > Hal moved forward by 10 steps.\n > Hal now at position (0,10).\nHal: What must I do next?  > Hal moved forward by 5 steps.\n > Hal now at position (0,15).\nHal: What must I do next?  > Hal replayed 2 commands in reverse silently.\n > Hal now at position (0,30).\nHal: What must I do next? Hal: Shutting down..\n")

    def test_split_command_range(self):
        each = "2-5"
        n, m = robot.split_command_range(each)
        self.assertEqual(n, 2)
        self.assertEqual(m, 5)

    @patch("sys.stdin", StringIO('HAL\nforward 3\nforward 2\nforward 1\nreplay 3-1\noff\n'))
    def test_do_replay_range(self):
        sys.stdout = StringIO()
        obstacles.random.randint = lambda a, b: 0
        robot.robot_start()
        output = sys.stdout.getvalue()
        self.assertEqual(output, """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,3).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 1 steps.
 > HAL now at position (0,6).
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,9).
 > HAL moved forward by 2 steps.
 > HAL now at position (0,11).
 > HAL replayed 2 commands.
 > HAL now at position (0,11).
HAL: What must I do next? HAL: Shutting down..\n""")