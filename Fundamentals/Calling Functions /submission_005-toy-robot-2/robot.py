def safezone_error(robo_info):
    print("{}: Sorry, I cannot go outside my safe zone.".format(robo_info[0]))


def turn_robot(robo_info, direction):
    """this function updates robot direction"""
    if direction == "RIGHT":
        robo_info[2] = robo_info[2] + 90
    if direction == "LEFT":
        robo_info[2] = robo_info[2] - 90
    if robo_info[2] == 360:
            robo_info[2] = 0
    if robo_info[2] < 0:
        robo_info[2] = 360 - (robo_info[2] * -1)
    return robo_info


def print_position(robo_info):
    """this function returns a printable string with robot position
        returns
            istr: robots position
    """
    istr = "("+str(robo_info[1][0])+","+str(robo_info[1][1])+")"
    return " > {} now at position {}.".format(robo_info[0], istr)


def update_position(robo_info, icommand, command_count):
    """This function update robot cooordinates 
        returns
            robo_info: list with robot name and robot coordinates"""
    temp = 0
    command = icommand.upper()
    if command == "FORWARD":
        if robo_info[2] == 0:
            temp = robo_info[1][1] + int(command_count)
            if not temp < 200 and temp > -200:
                safezone_error(robo_info)
            else:
                robo_info[1][1] = temp
                print(move_forward_back(robo_info, icommand, command_count))

        if robo_info[2] == 90:
            temp = robo_info[1][0] + int(command_count)
            if not temp < 100 and temp > -100:
                safezone_error(robo_info)
            else:
                robo_info[1][0] = temp
                print(move_forward_back(robo_info, icommand, command_count))

        if robo_info[2] == 180:
            temp = robo_info[1][1] - int(command_count)
            if not temp < 200 and temp > -200:
                safezone_error(robo_info)
            else:
                robo_info[1][1] = temp
                print(move_forward_back(robo_info, icommand, command_count))

        if robo_info[2] == 270:
            temp = robo_info[1][0] - int(command_count)
            if temp > -100 and temp < 100:
                robo_info[1][0] = temp
                print(move_forward_back(robo_info, icommand, command_count))
            else:
                safezone_error(robo_info)
                

    if command == "BACK":
        if robo_info[2] == 0:
            temp = robo_info[1][1] - int(command_count)
            if not temp < 200 and temp > -200:
                safezone_error(robo_info)
            else:
                robo_info[1][1] = temp
                print(move_forward_back(robo_info, icommand, command_count))

        if robo_info[2] == 90:
            temp = robo_info[1][0] - int(command_count)
            if not temp < 100 and temp > -100:
                safezone_error(robo_info)
            else:
                robo_info[1][0] = temp
                print(move_forward_back(robo_info, icommand, command_count))

        if robo_info[2] == 180:
            temp = robo_info[1][1] + int(command_count)
            if not temp < 200 and temp > -200:
                safezone_error(robo_info)
            else:
                robo_info[1][1] = temp
                print(move_forward_back(robo_info, icommand, command_count))

        if robo_info[2] == 270:
            temp = robo_info[1][0] + int(command_count)
            if temp > -100 and temp < 100:
                robo_info[1][0] = temp
                print(move_forward_back(robo_info, icommand, command_count))
            else:
                safezone_error(robo_info)

    return robo_info


def move_forward_back(robo_info, icommand, command_count):
    """This function moves the robot front and back
        returns
            result: how many times robot moved"""
    result = " > {} moved {} by {} steps.".format(robo_info[0], icommand.lower(), command_count)
    return result


def handle_help_command():
    """This function hanldes the help command
        returns 
            man_help: long string with help message
    """
    man_help = "I can understand these commands:\n"
    man_help += "OFF  - Shut down robot\n"
    man_help += "HELP - provide information about commands\n"
    man_help += "FORWARD [count]- Moves the bot forward count times\n"
    man_help += "BACK [count]- Moves the bot back count times\n"
    man_help += "RIGHT - Turns robot right\n"
    man_help += "LEFT - Turns robot left\n"
    man_help += "SPRINT - sprints robot count times\n"
    return man_help

    
def handle_command(robo_info, icommand, command_count):
    """This function handles and calls all the robo commands"""
    command = icommand.upper()
    if command == "OFF":
        #robot Turns OFF
        print("{}: Shutting down..".format(robo_info[0]))

    if command == "HELP":
        man_help = handle_help_command()
        print(man_help)
        run_commands(robo_info)

    if command == "FORWARD" or command == "BACK":
        #position is updated
        robo_info = update_position(robo_info, icommand, command_count)
        print(print_position(robo_info))
        run_commands(robo_info)

    if command == "RIGHT" or command == "LEFT":
        robot_info = turn_robot(robo_info, command)
        print(" > {} turned {}.".format(robo_info[0], command.lower()))
        print(print_position(robo_info))
        run_commands(robo_info)

    if command == "SPRINT":
        icount = int(command_count)
        while icount != 0:
            robo_info = update_position(robo_info, "FORWARD", icount)
            icount -= 1
        print(print_position(robo_info))
        run_commands(robo_info)


def check_valid_command(command, command_count, valid_command_list):
    """This function checks if requseted command is vaild or not
        returns
            result: True when command exists, False when command is invalid
    """
    result = False
    if command.upper() in valid_command_list:
        if command.upper() != "FORWARD" and command.upper() != "BACK":
            result = True
        elif command_count.isdigit():
            result = True
    return result


def command_spliter(user_input):
    """This function breaks user input command to two strings
        returns
            command: what the robot must do
            command_count: How many times the robot must do it"""
    command = ""
    command_count = ""
    for c in user_input:
        if c.isalpha():
            command += c
        if c.isdigit():
            command_count += c
    return command, command_count


def get_command_input(robo_info, valid_command_list):
    """This Function asks user to enter command till valid command is entered
        returns
            command : a vaild command
            command_count: how many times the command must happen
    """
    user_input = input("{}: What must I do next? ".format(robo_info[0]))
    command, command_count = command_spliter(user_input)

    while not check_valid_command(command, command_count, valid_command_list):
        print("{}: Sorry, I did not understand '{}'.".format(robo_info[0], user_input))
        user_input = input("{}: What must I do next? ".format(robo_info[0]))
        command, command_count = command_spliter(user_input)
    return command, command_count


def run_commands(robo_info):
    """This function asks and runs robot commands"""
    valid_command_list = ["OFF", "HELP", "FORWARD", "BACK", "RIGHT", "LEFT", "SPRINT"]
    command, command_count = get_command_input(robo_info, valid_command_list)
    handle_command(robo_info, command, command_count)


def name_robot_input():
    """This function ask the user to name the robot
        returns
            name: the robots name
    """
    user_input = input("What do you want to name your robot? ")
    name = ""
    if len(user_input) > 0:
        name = user_input
    else:
        name_robot()
    return name


def robot_start():
    """This is the entry function, do not change"""
    robo_info = list()
    robo_info.append(name_robot_input())
    #coordinates of robot at 0
    robo_info.append([0,0])
    robo_info.append(0)

    #robot turns ON
    print("{}: Hello kiddo!".format(robo_info[0]))
    run_commands(robo_info)


if __name__ == "__main__":
    robot_start()
