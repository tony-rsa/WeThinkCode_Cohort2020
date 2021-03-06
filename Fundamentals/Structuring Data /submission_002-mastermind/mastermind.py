import random

def set_code():
    code = [random.randint(1,8) for x in range(0,4)]

    print("4-digit Code has been set. Digits in range 1 to 8. ", end="")
    print("You have 12 turns to break it.")

    return code


def check_duplicates(user_input):
    #checks if input has duplicates
    if len(user_input) == len(set(user_input)):
        return False
    else:
        return True


def get_answer():
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
            return str(answer)


def handle_outcomes(incorrect_place, correct_place, try_count):
    print("Number of correct digits in correct place:     {}"
        .format(correct_place))
    print("Number of correct digits not in correct place: {}"
        .format(incorrect_place))
           
    if correct_place == 4:
        print("Congratulations! You are a codebreaker!")
        return True , try_count
    else:
        try_count -= 1
        print("Turns left: {}".format(try_count))
        return False, try_count


def code_master(code, answer, try_count):
    correct_place = 0
    incorrect_place = 0
    v = 0
    for x in answer:
        for index, value in enumerate(code):
            if str(value) == x:
                if v == index:
                    correct_place += 1
                else:
                    incorrect_place += 1
        v += 1
    return handle_outcomes(incorrect_place, correct_place, try_count)


def run_game():
    """
    TODO: implement Mastermind code here
    """
    code = set_code()
    try_count = 12
    while True:
        answer = get_answer()
        result, try_count = code_master(code, answer, try_count)
        if (result == True) or (try_count == 0):
            print("The code was:", end=" ")
            for x in code:
                print(x, end="")
            print()
            break


if __name__ == "__main__":
    run_game()
