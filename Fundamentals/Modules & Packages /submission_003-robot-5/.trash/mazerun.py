import robot

def convert_combo(x, y, inst):
    if inst == "U":
        y += 10
    if inst == "R":
        x += 5
    if inst == "D":
        y -= 10
    if inst == "L":
        x -= 5
    return (x , y)


def find_end(find_x, find_y, combo):

    for j in combo:
        find_x, find_y = convert_combo(find_x, find_y, j)

    if find_x == 0 and find_y == 200:
        return True
    
    return False


def valid_obst(obst_import, x, y, put):

    for j in put:
        x, y = convert_combo(x, y, j)
        if obst_import.is_position_blocked(x, y) or not (-100 <= x <= 100 and -200 <= y <= 200):
            return False
    
    return True


def solve_maze(obst_import, find_x, find_y):
    que = [""]
    combination = ""
    x = ""
    y = ""
    while not find_end(find_x,find_y,combination):
        print("here")
        combination = que.pop(0)
        for j in ["U", "R", "D", "L"]:
            put =  combination + j
            if valid_obst(obst_import, 0, 0, put):
                que.append(put)
                print(put)
                x, y = convert_combo(find_x, find_y, put)
    
    print("solve x {} y {}".format(x,y))

    return que