import random
import sys

def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    len_of_word = len(word)
    random_letter_index = random.randint(0, len_of_word - 1)
    current_answer = ""
    x = 0
    while x < len_of_word:
        if x == random_letter_index:
            current_answer += word[random_letter_index]
        else:
            current_answer += "_"
        x += 1
    return current_answer



# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    result = False
    for i in range(0, len(original_word)):
        if (original_word.find(char,i) != -1 and original_word.find(char, i) != answer_word.find(char,i)):
            result = True
    return result


# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    c = 0
    new_word = ""
    flag = False
    while c < len(answer_word):
        if (answer_word[c] == "_") and (original_word[c] == char and flag == False):
            new_word += char[0]
            flag = True
        else:
            new_word += answer_word[c]
        c += 1
    return new_word



def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)
    return answer


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    print("/----")  
    if number_guesses <= 3:
        print("|   0")
    else:
        print("|")
    if number_guesses <= 2:
        print("|  /|\\")
    else:
        print("|")
    if number_guesses <= 1:
        print("|   |")
    else:
        print("|")
    if number_guesses <= 0:
        print("|  / \\")
    else:
        print("|")
    print("_______")


# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):
    print("Guess the word: "+answer)
    guess_count = 5
    while word != answer:
        guess = get_user_input()
        if (guess == "exit"):
            print("Bye!")
            break
        if is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
        else:
            guess_count -= 1
            answer = do_wrong_answer(answer, guess_count)
            if (guess_count == 0):
                print("Sorry, you are out of guesses. The word was: "+word)
                break
            continue


# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    if (len(sys.argv) > 1):
        words_file = sys.argv[1]
    else:
        words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)

