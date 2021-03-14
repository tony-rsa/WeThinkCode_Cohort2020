import random

global list_of_obstacles
list_of_obstacles = []

def randomly_populate_pixel(x_crd,y_crd):
    """
        Function randomly populates a 20X20 pixel with obstacles.
        :param x_crd, y_crd: start coordinates(start of the pixel)
        :returns : list with randomly populated obstacles
    """
    global list_of_obstacles

    for y in range(0,4):
        for x in range(0,4):
            if random.randint(1,20) % 4 == 0:
                list_of_obstacles.append((x_crd,y_crd))
            x_crd += 5
        x_crd -= 20
        y_crd += 5

    return list_of_obstacles


def get_obstacles():
    """
        Function Randomly generates a maze
        :returns : list with obstacles (x,y)
    """
    y_crd = -200
    for y in range(0,20):
        x_crd = -100
        for x in range(0,10):
            if not (y_crd in range(-20,20) and x_crd in range(-20,20)):
                list_obst = randomly_populate_pixel(x_crd,y_crd)
            x_crd += 20
        y_crd += 20

    return list_obst


def is_position_blocked(x,y):
    """
        function checks if given position is blocked with an obstacle
        :param x: x coordinate
        :param y: y coordinate
        :return True/False : False if position is not blocked, true if it is
    """
    global list_of_obstacles

    for each in list_of_obstacles:
        if x in range(each[0], each[0]+5) and y in range(each[1], each[1]+5):
            return True

    return False


def check_greater(value1, value2):
    """
        :returns: smallest value first
    """
    if value1 > value2:
        return value2, value1

    return value1, value2
    

def is_path_blocked(x1,y1, x2, y2):
    """ 
        :return true: if path is blocked
        :return false: if path is not blocked
    """
    if y1 == y2:
        x1, x2 = check_greater(x1, x2)
        for x in range(x1, x2):
            if is_position_blocked(x, y1):
                return True
    else:
        y1, y2 = check_greater(y1, y2)
        for y in range(y1, y2):
            if is_position_blocked(x1, y):
                return True
                
    return False