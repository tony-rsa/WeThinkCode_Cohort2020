import sys
from world import obstacles

turtle_flag = False
if "turtle" in sys.argv:
    from world.turtle.world import *
    turtle_flag = True
else:
    from world.text.world import *


# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint', 'replay', 'silent', 'reversed']

# variables tracking position and direction
position_x = 0
position_y = 0
current_direction_index = 0


def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """

    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)

    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def check_valid_range(command_range):
    """
        checks if the command  range id valid
        :param command_range: replay range as string
        :return flag: boolean flag true if range is valid
    """
    flag = False
    if command_range.find("-"):
        ranges = command_range.split("-")
    if len(ranges) == 2:
        if ranges[0].isdigit() and ranges[1].isdigit():
            flag = True
    if command_range.isdigit():
        flag = True
    return flag


def checker_(value):
    """
        function used with map() to check if each command valid
    """
    if value in valid_commands:
        return value
    if check_valid_range(value):
        return value
    return ""


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """
    check_commands = command.lower().split(" ")

    if check_commands[0] == "replay":
        my_valid_command = list(filter(lambda x: x != "", list(map(checker_ ,check_commands))))
        if check_commands == my_valid_command:
            return True

    (command_name, arg1) = split_command_input(command)

    return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1))


def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY {n-m}- replay history commands n is start index m is end index 
SILENT - DOES COMMANDS SILENTLY
REVERSED - DOES COMMANDS IN REVERSE
"""


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    global position_x, position_y, current_direction_index

    zone_flag, obst_flag, new_x, new_y = update_position(steps, position_x, position_y, current_direction_index)
    if zone_flag and not obst_flag:
        position_x = new_x
        position_y = new_y
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    if obst_flag:
        return True, ''+robot_name+': Sorry, there is an obstacle in the way.'
    if not zone_flag:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    global position_x, position_y, current_direction_index

    zone_flag, obst_flag, new_x, new_y = update_position(-steps, position_x, position_y, current_direction_index)
    if zone_flag and not obst_flag:
        position_x = new_x
        position_y = new_y
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    if obst_flag:
        return True, ''+robot_name+': Sorry, there is an obstacle in the way.'
    if not zone_flag:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    if turtle_flag:
        turtle_turn_right()

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    if turtle_flag:
        turtle_turn_left()

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def reversed_replay(command_history, reverse):
    """
        function that reverses command_history if reverse is set to true
        :param command_history: list of history commands
        :param reverse: boolean true/flase true if reverse needed
        :return command_history: list of history commands
        :return reverse_pre: prefix to add to output command
    """
    reverse_pre = ""
    if reverse:
        command_history = list(filter(lambda x: x != "",command_history[::-1]))
        reverse_pre = " in reverse"
    else:
        command_history = list(filter(lambda x: x != "",command_history))
    return command_history, reverse_pre


def replay_silent(silent):
    """
        functions that handels silent command
        :param silent: boolean true if silent
        :return silent_pre: prefix to add to output command
    """
    silent_pre = ""
    if silent:
        silent_pre = " silently"
    return silent_pre


def valid_replay_command(command):
    """
        checks input commands with listed commands and returns commands
    """
    movement_commands = ['forward', 'back', 'right', 'left', 'sprint']
    for each in movement_commands:
        if each in command:
            return command


def split_command_range(each):
    """
    splits replay range if "-" found
    """
    n = each
    m = "0"
    if each.find("-") > -1:
        slit_range = each.split("-")
        n = slit_range[0]
        m = slit_range[1]
    return int(n), int(m)


def check_replay_range(command):
    """
        function check replay range
        :param command: commands
        :return flag: boolean true if range valid
        :return n, m: int range
    """
    split_command = command.split(" ")
    n = 0
    m = 0
    flag = False
    for each in split_command:
        if any(map(str.isdigit, each)):
            flag = True
            n, m = split_command_range(each)
    return flag, n, m
    

def do_replay(robot_name, command_history, command, reverse, silent):
    """
        replay command history.
        :param command_history: history commands
        :param command: last inputed command
        :param reverse: boolean true if output must be in reverse
        :param silent: boolean true if output must be silent
    """
    replay_range, n, m = check_replay_range(command)

    movement_commands = ['forward', 'back', 'right', 'left', 'sprint']
    command_history = list(map(valid_replay_command, command_history))
    command_history =list(filter(lambda x: x != None, command_history))

    command_history, reverse_pre = reversed_replay(command_history, reverse)
    silent_pre = replay_silent(silent)

    if replay_range:
        index = len(command_history) - n
        command_history = command_history[index:]

    x = 0
    for command in command_history:
        handle_command(robot_name, command, command_history, silent)
        if x == m and m > 0:
            break
        x += 1
    
    return True, " > {} replayed {} commands{}{}.".format(robot_name, len(command_history) - m, reverse_pre, silent_pre), False


def handle_command(robot_name, command, command_history, silent):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """
    global position_x, position_y
    reverse = False
    if command.find("replay") != -1:
        if command.find("silent") != -1:
            silent = True
        if command.find("reversed") != -1:
            reverse = True
        (do_next, command_output, silent) = do_replay(robot_name, command_history, command, reverse, silent)

    (command_name, arg) = split_command_input(command)

    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    
    if not silent:
        print(command_output)
        show_position(robot_name, position_x, position_y)

    return do_next


def add_command_history(command, command_history):
    command_history.append(command)
    return command_history


def robot_start():
    """This is the entry point for starting my robot"""

    global position_x, position_y, current_direction_index
    position_x = 0
    position_y = 0
    current_direction_index = 0

    list_of_obstacles = obstacles.get_obstacles()

    if turtle_flag:
        setup_turtle(list_of_obstacles)

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")
    
    print_obstacles(list_of_obstacles)

    command_history = []
    command = get_command(robot_name)
    silent = False
    while handle_command(robot_name, command, command_history, silent):
        command_history = add_command_history(command, command_history)
        command = get_command(robot_name)

    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()
