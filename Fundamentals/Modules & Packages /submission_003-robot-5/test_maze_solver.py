import unittest
from io import StringIO
from unittest.mock import patch
import sys
import import_helper
import maze_solver
from maze import crazy_maze as obstacles
import robot

class MyTests(unittest.TestCase):

    @patch("sys.stdin", StringIO('HAL\nmazerun\noff\n'))
    def test_find_edge(self):
        sys.stdout = StringIO()
        obstacles.random.randint = lambda a, b: 1
        robot.robot_start()

        output = sys.stdout.getvalue()
        self.assertTrue(output.find('starting maze run..') > -1)
        self.assertTrue(output.find('I am at the top edge') > -1)

    def test_compress_instrc(self):
        instruct = ["L","L","R","L", "D", "D", "R"]
        result = maze_solver.compress_instrc(instruct, [])
        self.assertEqual(result,[('L', 10), ('R', 5), ('L', 5), ('D', 10)])

    def test_append_handler(self):
        result = maze_solver.append_handler(10, 3, "U", "D")
        self.assertEqual(result,"D")
        result = maze_solver.append_handler(0, 3, "R", "L")
        self.assertEqual(result,"R")

    def test_make_instr(self):
        wayout = [(0,0),(0,5),(5,0)]
        result = maze_solver.make_instr(wayout, [])
        self.assertEqual(result, [('U', 5), ('R', 5)])

    def test_backRoute(self):
        solution = {(0,10): (0,10), (0,5): (0,10), (0,0): (0,5)}
        result = maze_solver.backRoute(solution, 0, 10, 0, 0)
        self.assertEqual(result, [('U', 10)])
    
    def test_do_x_y(self):
        result = maze_solver.do_x_y(0, 0, "U", 20)
        self.assertEqual(result, (0,20))

    @patch("sys.stdin", StringIO('HAL\nmazerun\nmazerun bottom\noff\n'))
    def test_search(self):
        sys.stdout = StringIO()
        obstacles.random.randint = lambda a, b: 1
        robot.robot_start()

        output = sys.stdout.getvalue()
        self.assertTrue(output.find('starting maze run..') > -1)
        self.assertTrue(output.find('I am at the top edge') > -1)
        self.assertTrue(output.find('I am at the bottom edge') > -1)