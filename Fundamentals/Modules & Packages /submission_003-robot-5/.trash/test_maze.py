import unittest
import random
from io import StringIO
from unittest.mock import patch
import sys
from maze import the_worlds_most_crazy_maze as maze

class MyTest(unittest.TestCase):

    def _make_walls(self):
        result = maze.make_walls()
        self.assertEqual(len(result) == 10, True)
        self.assertEqual(len(result[0]) == 10, True)

    def _make_maze(self):
        result = maze.make_maze()
        self.assertEqual(result, "")

    def _y_obstacles(self):
        maze.random.randint = lambda a,b: 1
        result = maze.y_obstacles(maze.make_walls())
        print(result)
        self.assertEqual(result, )

    def _make_door(self):
        maze.random.randint = lambda a, b: 4
        result = maze.make_door()
        self.assertEqual(result, ([0,0,0,0,1,0,0,0,0,0],4))

    def test_do_x(self):
        maze.random.randint = lambda a, b: 1
        result = maze.do_x(7)
        self.assertEqual(result, ([0,1,1,1,1,1,1,1,0,0],1))

        maze.random.randint = lambda a, b: 9
        result = maze.do_x(7)
        self.assertEqual(result, ([0,0,0,0,0,0,0,1,1,1],9))

    def test_do_y(self):
        result = maze.do_y(5)
        self.assertEqual(result, ([0,0,0,0,0,1,0,0,0,0],5))
        

    def test_make_plane(self):
        result = maze.make_plane(5)
        self.assertEqual(len(result) == 16, True)