
def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """
    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def clean_word(word):
    """
        function removes all non alphabet chars
        :param word: string word
        :return temp: word with only alphabets
    """
    temp = ""
    for char in word:
        if char.isalpha():
            temp += char
    return temp


def convert_to_word_list(text):
    """Function that converts text to lower case list of words
        :param text: tring containing delimiters to use to split the string, e.g. `,;? `
        :return word_list: a list with lowercase words in it and no special chars
    """
    if text == "":
        return []

    words = split(" ", text.lower())
    converted_words = list(filter(lambda word: word != "", list(map(clean_word, words))))
    return converted_words


def words_longer_than(length, text):
    """Function that converts text with length thats more that length to lower case list of words
        :param text: tring containing delimiters to use to split the string, e.g. `,;? `
        :param length: the mininum int number/length the words to return must be
        :return word_list: a list with lowercase words in it and no special chars and have len grater than length
    """
    words = convert_to_word_list(text)
    word_list = list(filter(lambda x: len(x) > int(length),words))
    return word_list


def words_lengths_map(text):
    """Function that converts text to lower case list of words
        :param text: tring containing delimiters to use to split the string, e.g. `,;? `
        :return word_list: a list with lowercase words in it and no special chars
    """
    length_list = list(map(lambda  x: len(x), convert_to_word_list(text)))
    dict = {x:length_list.count(x) for x in length_list}
    return dict
        

def letters_count_map(text):
    """
        function that count and maps alphabets in given str
        :param text:
        :return dict: dict with alphabets and counts
    """
    alphabet = get_alphabet_characters()
    dict = {letter: text.lower().count(letter) for letter in alphabet}
    return dict


def most_used_character(text):
    """
        returns value(alphabet) of most used letter
    """
    if text == "":
        return None
    alpha = max(letters_count_map(text), key=letters_count_map(text).get)
    return alpha


def get_alphabet_characters():
    """
    :returns alpha_list: list with the alphabet
    """
    alpha_list = [chr(ord("a") + x) for x in range(0, 26)]
    return alpha_list
    