import random

global list_of_obstacles
list_of_obstacles = []

def get_obstacles():
    """
        function randomly creates list with turlpe that has (x,y) coordinate - positions of obstacels
        :return list_of_obstacles: a list with obstacels in the form (x,y) 
    """
    global list_of_obstacles

    list_of_obstacles = [(random.randint(-100,100),random.randint(-200,200))\
                    for i in range(0,random.randint(1,10))]

    return list_of_obstacles


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
        returns smallest value first
    """
    if value1 > value2:
        return value2, value1

    return value1, value2
    


def is_path_blocked(x1,y1, x2, y2):
    """
        return true if path is blocked
        return false if path is not blocked
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


def show_obst():
    """
        returns list of created obst.
    """
    global list_of_obstacles

    return list_of_obstacles