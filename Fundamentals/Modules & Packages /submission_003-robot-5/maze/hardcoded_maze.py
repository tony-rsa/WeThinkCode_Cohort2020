import random

obstacles_list = []


def get_obstacles():
    """
    Returns a list of randomly generated obstacle coordinates.
    """
    global obstacles_list
    y = 200

    maze_file = open('maze/maze1.txt', 'r')
    maze_lines = maze_file.readlines()
    maze_file.close()
    
    for line in maze_lines:
        y -= 5
        x = -105
        for c in line:
            x += 5
            if c == 'X':
                obstacles_list.append((x, y))

    return obstacles_list


def is_position_blocked(x, y):
    """
    Checks if there is an obstacle at the robots destination.
    Parameters:
            x, y : the coordinates of robots destination
    Returns:
            True if obstacle
            False if no obstacle
    """
    global obstacles_list

    for c in obstacles_list:
        if (x in range(c[0], c[0] + 5)) and (y in range(c[1], c[1] + 5)):
            return True
    return False


def is_path_blocked(x1, y1, x2, y2):
    """
    Checks if there is an obstacle in robots path.
    Parameters:
            x1, y1 : starting coordinates of robot
            x2, y2 : ending coordinates of robot
    Returns:
            True if obstacle in path
            False if no obstacle in path
    """
    global obstacles_list

    for c in obstacles_list:
        if x1 == x2 and x1 in range(c[0], c[0] + 5):
            for y in range(c[1], c[1] + 5):
                if (y1 < y < y2) or (y1 > y > y2):
                    return True
        if y1 == y2 and y1 in range(c[1], c[1] + 5):
            for x in range(c[0], c[0] + 5):
                if (x1 < x < x2) or (x1 > x > x2):
                    return True
    return False