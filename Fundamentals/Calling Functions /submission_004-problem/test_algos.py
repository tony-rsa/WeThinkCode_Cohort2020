import unittest
import super_algos

class TestFunctions(unittest.TestCase):

    def test_find_min(self):
        my_list = [1,2,3,4,5]
        result = super_algos.find_min(my_list)
        self.assertEqual(result, 1)

        my_list = [1,"2","3",4,5]
        result = super_algos.find_min(my_list)
        self.assertEqual(result, -1)

        my_list = []
        result = super_algos.find_min(my_list)
        self.assertEqual(result, -1)

    
    def test_sum_all(self):
        my_list = [1,2,3,4,5]
        result = super_algos.sum_all(my_list)
        self.assertEqual(result, 15)

        my_list = [1,"2","3",4,5]
        result = super_algos.sum_all(my_list)
        self.assertEqual(result, -1)

        my_list = []
        result = super_algos.sum_all(my_list)
        self.assertEqual(result, -1)


    def test_find_possible_strings(self):
        result = super_algos.find_possible_strings(['a','b','c','d'], 1)
        self.assertEqual(['a','b','c','d'], result)

        result = super_algos.find_possible_strings(['a','b'], 3)
        self.assertEqual(['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb'], result)

        result = super_algos.find_possible_strings([], 3)
        self.assertEqual([], result)

        result = super_algos.find_possible_strings([1,2,3,4], 3)
        self.assertEqual([], result)

    # def test_check_elements(self):
    #     my_list = ["3", 4, 5 ,6]
    #     result = super_algos.check_elements(my_list, int)
    #     self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()