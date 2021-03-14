from collections import deque

def find_edge(direction, obst_import):
    """
        Function find a vaild point at the adge to start from
        :returns : tulpe with x and y coordinates
    """
    direction_dict = {"U": (-60,200), "D": (-60,-200), \
                        "R": (100,-90), "L": (-100,-90)}
    x, y  = direction_dict[direction]

    if direction == "U" or direction == "D":
        while obst_import.is_position_blocked(x,y):
            x += 5
    else:
        while obst_import.is_position_blocked(x,y):
            y += 5   
             
    return (x, y)


def compress_instrc(instruct, output_list):
    """
        This functions compresses instructions like "U,U,D,D,L,R,R,R" to a shorter list "U2,D2,L1,R3"
        :param instruct: list with instructions that need compressing
        :returns output_list: a list with less instructions 
    """
    while True:
        if len(instruct) == 1:
            break

        count = 0
        command = instruct[0]
        while command == instruct[0]:
            count += 5
            command = instruct.pop(0)

        output_list.append((command, count))

    return output_list


def append_handler(value1, value2, pos, neg):
    """
        function used to help convert coorinates to instuctions
        :param value1, value2: valuse to check
        :return pos, neg: instructions like "U", "D", "L", "R"
    """
    if value1 < value2:
        return pos
    else:
        return neg


def make_instr(wayout, instruct):
    """
        this function coverts coordinates to the wayout into instructions like "U", "D", "L", "R"
        :param wayout: list with coordinates from start (0,0) to end point
        :returns: list with instructions which gets compressed 
    """
    for j in range(0, len(wayout)-1):

        if wayout[j][0] == wayout[j+1][0]:
            instruct.append(append_handler(wayout[j][1],\
                                    wayout[j+1][1],"U","D"))
        else:
            instruct.append(append_handler(wayout[j][0],\
                                    wayout[j+1][0],"R","L"))

    instruct.append("")

    return compress_instrc(instruct, [])


def backRoute(solution, end_x, end_y, x, y):
    """
        function find back route
        :param solution: a dict with solution to the maze run
        :param end_x, end_y: the coordinates of the edge
        :param x, y: the start coordinates
    """
    wayout = [(x,y)]

    while (x, y) != (end_x, end_y):
        x, y = solution[x, y] 
        wayout.append((x,y))

    return make_instr(wayout, [])


def do_x_y(x, y, todo, step):
    """
        this function shifts the x and y in the direction ot "todo" by "step" count
        :returns direction_dict: tulpe with new x and y coordinates
    """
    direction_dict = {"U": (x,y+step), "D": (x,y-step), \
                        "R": (x+step,y), "L": (x-step,y)}
    
    return direction_dict[todo]


def search(direction, start_x, start_y, end_x, end_y, obst_import):
    """
        function use breath first search method with a dict for backtracking a vaild route
        :param direction: the adge you wish the robot to go
        :param obst_import: the maze module
        :returns : step by step instruction that will lead the robot to the adge
    """
    frontier = deque()
    solution = dict()
    visited = list()

    x = end_x
    y = end_y    

    frontier.append((x, y))
    solution[x,y] = x,y

    while len(frontier) > 0:
        x, y = frontier.popleft()

        for j in ["U", "R", "D", "L"]:
            cell = do_x_y(x, y, j, 5)
            if not obst_import.is_path_blocked(x,y, cell[0], cell[1]) and\
                (-101 <= cell[0] <= 101 and -201 <= cell[1] <= 201) and\
                                                 cell not in visited:
                solution[cell] = x, y    # backtracking routine [cell] is the current cell. x, y is the prev cell
                frontier.append(cell)
                visited.append(cell)

    return solution