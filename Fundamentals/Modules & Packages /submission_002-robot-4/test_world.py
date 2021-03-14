import unittest
from world.text.world import *

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