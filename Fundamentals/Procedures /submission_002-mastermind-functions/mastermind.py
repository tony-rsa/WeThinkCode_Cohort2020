import random


def make_code():
    """
    Makes a new code everytime game starts

    Returns:
        code: returns 4-digit code(each between 1 to 8)and has no duplicates
    """
    code = [random.randint(1,8) for x in range(0,4)]

    print("4-digit Code has been set. Digits in range 1 to 8. ", end="")
    print("You have 12 turns to break it.")

    return code


def get_user_input():
    """
    Gets user input

    Returns:
        user_input: user input as an int
        boolean: Flag which is true when answer useable
    """
    while True:
        try:
            answer = int(input("Input 4 digit code: "))
            if len(str(answer)) != 4:
                print("Please enter exactly 4 digits.")
                continue
        except ValueError:
            print("Please enter exactly 4 digits.")
            continue
        else:
            return answer


def handle_outcomes(correct_digits_only, correct_digits_and_position, turns):
    """
    Return game outcomes

    Parameters:
        correct_digits_only: Number of correct digits not in correct place
        correct_digits_and_position: Number of correct digits in correct place

    Returns:
        True: user answer is correct
        False: user annswer is wrong
        truns: number of turns the user has left
    """
    print("Number of correct digits in correct place:     {}"
        .format(correct_digits_and_position))
    print("Number of correct digits not in correct place: {}"
        .format(correct_digits_only))
    #Did you win?   
    if correct_digits_and_position == 4:
        print("Congratulations! You are a codebreaker!")
        return True , turns
    else:
        turns -= 1
        print("Turns left: {}".format(turns))
        return False, turns


def code_master(code, answer, turns):
    """
    Makes a new code everytime game starts

    Parameters:
        code: code made in the start of game
        answer: users answer to game
        turns: how many turns the user has

    Returns:
        hande_outcomes(): called function to handle game outcomes
    """
    correct_digits_and_position = 0
    correct_digits_only = 0
    v = 0
    for x in str(answer):
        for index, value in enumerate(code):
            if str(value) == x:
                if v == index:
                    correct_digits_and_position += 1
                else:
                    correct_digits_only += 1
        v += 1
    return handle_outcomes(correct_digits_only, correct_digits_and_position, turns)


def run_game():
    """
    TODO: implement Mastermind code here
    """
    code = make_code()
    turns = 12
    while True and turns > 0:
        answer = get_user_input()
        result, turns = code_master(code, answer, turns)
        if (result == True) or (turns == 0):
            print("The code was: "+str(code))
            break


if __name__ == "__main__":
    run_game()
