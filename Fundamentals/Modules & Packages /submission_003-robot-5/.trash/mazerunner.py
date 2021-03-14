import robot
from collections import deque

def return_valid_pixels(obst_import):
    valid_pixels = []
    for y in range(-200,201):
        for x in range(-100,101):
            if not obst_import.is_position_blocked(x,y):
                valid_pixels.append((x,y))
    return valid_pixels


def run_maze(x, y, obst_import):

    valid_pixels = return_valid_pixels(obst_import)
    
    inline_list = deque()
    wayout_list = dict()
    inline_list.append((x,y))
    wayout_list[x,y] = x,y

    way_commands = [""]
    checked_list = []

    y = 0
    while len(inline_list) > 0 or y >= 0:

        x, y = inline_list.popleft()

        #check up
        if (x,y+5) in valid_pixels and (x,y+5) not in checked_list:
            inline_list.append((x,y+5))
            wayout_list[(x,y+5)] = (x,y)
            if way_commands[len(way_commands)-1] != ("D", 5):
                way_commands.append(("U", 5))
            checked_list.append((x,y+5))

        #check left
        if (x+5,y) in valid_pixels and (x+5,y) not in checked_list:
            inline_list.append((x+5,y))
            wayout_list[(x+5,y)] = (x,y)
            checked_list.append((x+5,y))
            if way_commands[len(way_commands)-1] != ("R", 5):
                way_commands.append(("L", 5))
        #check down
        if (x,y-5) in valid_pixels and (x,y-5) not in checked_list:
            inline_list.append((x,y-5))
            wayout_list[(x,y-5)] = (x,y)
            checked_list.append((x,y-5))
            if way_commands[len(way_commands)-1] != ("U", 5):
                way_commands.append(("D", 5))

        #check right
        if (x-5,y) in valid_pixels and (x-5,y) not in checked_list:
            inline_list.append((x-5,y))
            wayout_list[(x-5,y)] = (x,y)
            checked_list.append((x-5,y))
            if way_commands[len(way_commands)-1] != ("L", 5):
                way_commands.append(("R", 5))
    
    # print(way_commands)

    return way_commands
    

    # for x in range(0,5):
    #     rslt = robot.do_forward("test", 50)
    #     print(rslt[0])

def do_maze(x, y, obst_import):
    valid_pixels = return_valid_pixels(obst_import)

    fronter = deque()
    checked = []
    fronter.append((x,y))
    path = dict()

    check = "U"
    while x >= 0 and y > 0 and len(fronter) > 0:
        x, y = fronter.popleft()
        prev = check
        for check in ["U", "L", "D", "R"]:
                if not obst_import.is_position_blocked(x, y+5) and (-100 <= x <= 100 and -200 <= y+5 <= 200) and not (x,y) in checked:
                    fronter.append((x,y+5))
                    path[(x,y)] = prev
                    checked.append((x,y))
                    y += 5
            
            if check == "L":
                if not obst_import.is_position_blocked(x-5, y) and (-100 <= x-5 <= 100 and -200 <= y <= 200) and not (x,y) in checked:
                    fronter.append((x-5,y))
                    path[(x,y)] = prev
                    checked.append((x,y))
                    x -= 5
            
            if check == "D":
                if not obst_import.is_position_blocked(x, y-5) and (-100 <= x <= 100 and -200 <= y-5 <= 200) and not (x,y) in checked:
                    fronter.append((x,y-5))
                    path[(x,y)] = prev
                    checked.append((x,y))
                    y -= 5

            if check == "R":
                if not obst_import.is_position_blocked(x+5, y) and (-100 <= x+5 <= 100 and -200 <= y <= 200) and not (x,y) in checked:
                    fronter.append((x+5,y))
                    path[(x,y)] = prev
                    checked.append((x,y))
                    x += 5
    print(path)
    return path
            
