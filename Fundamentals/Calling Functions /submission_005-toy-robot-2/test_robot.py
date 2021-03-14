import unittest
from io import StringIO
from unittest.mock import patch
import sys
import robot

class TestFunctions(unittest.TestCase):

    @patch("sys.stdin", StringIO("hello\nOFf"))
    def test_get_command_input(self):
        robo_info = ["HAL", [0,0], 0]
        valid_command_list = ["OFF", "HELP"]
        sys.stdout = StringIO()
        robot.get_command_input(robo_info, valid_command_list)
        output = sys.stdout.getvalue()
        self.assertEqual(output, "HAL: What must I do next? HAL: Sorry, I did not understand 'hello'.\nHAL: What must I do next? ")
        

    def test_handle_help_command(self):
        result = robot.handle_help_command()
        expected = "I can understand these commands:\nOFF  - Shut down robot\nHELP - provide information about commands\nFORWARD [count]- Moves the bot forward count times\nBACK [count]- Moves the bot back count times\n"
        expected += "RIGHT - Turns robot right\n"
        expected += "LEFT - Turns robot left\n"
        expected += "SPRINT - sprints robot count times\n"
        self.assertEqual(result, expected)


    @patch("sys.stdin", StringIO("Forward 3\n ForWarD 10\noff"))
    def test_run_commands_forward(self):
        robo_info = ["HAL", [0,0], 0]
        sys.stdout = StringIO()
        robot.run_commands(robo_info)
        output = sys.stdout.getvalue()
        self.assertEqual(output, "HAL: What must I do next?  > HAL moved forward by 3 steps.\n > HAL now at position (0,3).\nHAL: What must I do next?  > HAL moved forward by 10 steps.\n > HAL now at position (0,13).\nHAL: What must I do next? HAL: Shutting down..\n")

    
    @patch("sys.stdin", StringIO("BAck 3\nBACk 10\noff"))
    def test_run_commands_back(self):
        robo_info = ["HAL", [0,0], 0]
        sys.stdout = StringIO()
        robot.run_commands(robo_info)
        output = sys.stdout.getvalue()
        self.assertEqual(output, "HAL: What must I do next?  > HAL moved back by 3 steps.\n > HAL now at position (0,-3).\nHAL: What must I do next?  > HAL moved back by 10 steps.\n > HAL now at position (0,-13).\nHAL: What must I do next? HAL: Shutting down..\n")


    @patch("sys.stdin", StringIO("forward 10\nright\nforward 5\noff"))
    def test_run_commands_right(self):
        robo_info = ["HAL", [0,0], 0]
        sys.stdout = StringIO()
        robot.run_commands(robo_info)
        output = sys.stdout.getvalue()
        self.assertEqual(output, "HAL: What must I do next?  > HAL moved forward by 10 steps.\n > HAL now at position (0,10).\nHAL: What must I do next?  > HAL turned right.\n > HAL now at position (0,10).\nHAL: What must I do next?  > HAL moved forward by 5 steps.\n > HAL now at position (5,10).\nHAL: What must I do next? HAL: Shutting down..\n")


    @patch("sys.stdin", StringIO("forward 10\nleft\nforward 5\noff"))
    def test_run_commands_left(self):
        robo_info = ["HAL", [0,0], 0]
        sys.stdout = StringIO()
        robot.run_commands(robo_info)
        output = sys.stdout.getvalue()
        self.assertEqual(output, "HAL: What must I do next?  > HAL moved forward by 10 steps.\n > HAL now at position (0,10).\nHAL: What must I do next?  > HAL turned left.\n > HAL now at position (0,10).\nHAL: What must I do next?  > HAL moved forward by 5 steps.\n > HAL now at position (-5,10).\nHAL: What must I do next? HAL: Shutting down..\n")


    @patch("sys.stdin", StringIO("sprint 5\noff"))
    def test_run_commands_sprint(self):
        robo_info = ["HAL", [0,0], 0]
        sys.stdout = StringIO()
        robot.run_commands(robo_info)
        output = sys.stdout.getvalue()
        self.assertEqual(output, "HAL: What must I do next?  > HAL moved forward by 5 steps.\n > HAL moved forward by 4 steps.\n > HAL moved forward by 3 steps.\n > HAL moved forward by 2 steps.\n > HAL moved forward by 1 steps.\n > HAL now at position (0,15).\nHAL: What must I do next? HAL: Shutting down..\n")

        