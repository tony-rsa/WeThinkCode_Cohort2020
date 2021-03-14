import unittest
import word_processor

class Mytest(unittest.TestCase):
    
    def test_convert_to_word_list(self):
        text = 'These are indeed interesting, an obvious understatement, times. What say you?'
        expected = ['these','are','indeed','interesting','an','obvious','understatement','times','what','say','you']
        result = word_processor.convert_to_word_list(text)
        self.assertEqual(result, expected)

    def test_words_longer_than(self):
        text = 'These are indeed interesting, an obvious understatement, times. What say you?'
        expected = ['interesting','understatement']
        length = 10
        result = word_processor.words_longer_than(length,text)
        self.assertEqual(result, expected)

    def test_words_lengths_map(self):
        text = 'These are indeed interesting, an obvious understatement, times. What say you?'
        expected = {2: 1, 3: 3, 4: 1, 5: 2, 6: 1, 7: 1, 11: 1, 14: 1}
        result = word_processor.words_lengths_map(text)
        self.assertEqual(result, expected)

    def test_letters_count_map(self):
        text = 'These are indeed interesting, an obvious understatement, times. What say you?'
        expected = {'a':5, 'b': 1, 'c':0, 'd': 3, 'e': 11, 'f': 0, 'g': 1, 'h': 2, 'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2, 'n': 6, 'o': 3, 'p': 0, 'q': 0, 'r': 3, 's': 6, 't': 8, 'u': 3, 'v': 1, 'w': 1, 'x': 0, 'y': 2, 'z': 0}
        result = word_processor.letters_count_map(text)
        self.assertEqual(result, expected)

    def test_most_used_char(self):
        text = 'These are indeed interesting, an obvious understatement, times. What say you?'
        expected = "e"
        result = word_processor.most_used_character(text)
        self.assertEqual(result, expected)