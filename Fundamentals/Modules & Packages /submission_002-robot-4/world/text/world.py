from world import obstacles

def print_obstacles(list_of_obst):
    """
        print all obstacles
        :param list_of_obst: list with obstacles
    """
    if len(list_of_obst) > 0:
        print("There are some obstacles:")
        for each in list_of_obst:
            print("- At position {},{} (to {},{})".format(each[0], each[1], each[0]+4, each[1]+4))


def show_position(robot_name, position_x, position_y):
    """
        prints current position of bot
    """
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y, position_x, position_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    # area limit vars
    min_y, max_y = -200, 200
    min_x, max_x = -100, 100

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y, obstacles.is_path_blocked(position_x,position_y, new_x, new_y)


def update_position(steps, position_x, position_y, current_direction_index):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    directions = ['forward', 'right', 'back', 'left']

    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    zone_flag, obst_flag = is_position_allowed(new_x, new_y, position_x, position_y)
    if zone_flag and not obst_flag:
        return zone_flag, obst_flag, new_x, new_y
    return zone_flag, obst_flag, position_x, position_y