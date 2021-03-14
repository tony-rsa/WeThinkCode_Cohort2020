def convert(last_move, inst):
    x, y = last_move
    if inst == "U":
        y += 10
    if inst == "R":
        x += 10
    if inst == "D":
        y -= 10
    if inst == "L":
        x -= 10
    return (x , y)


def find_end(start , moves, end):
    first_move = moves[0]
    last_move = moves[len(moves)-1]

    if end == "+y":
        if first_move == start and (last_move[0] in range(-100,101) and last_move[1] == 200):
            return True

    if end == "-y":
        if first_move == start and (last_move[0] in range(-100,101) and last_move[1] == -200):
            return True

    if end == "+x":
        if first_move == start and (last_move[1] in range(-200,201) and last_move[0] == 100):
            return True

    if end == "-x":
        if first_move == start and (last_move[1] in range(-200,201) and last_move[0] == -100):
            return True
    
    return False
        

def valid_move(moves, check, visited, obst_import):
    last_move = moves[len(moves)-1]
    new_x, new_y = convert(last_move, check)

    if obst_import.is_path_blocked(last_move[0], last_move[1], new_x, new_y)\
                             or not (-101 <= new_x <= 101 and -201 <= new_y <= 201)\
                             or convert(last_move, check) in visited:
        return False
    
    return True


def solve_maze(start, end, obst_import):
    
    list_of_valid_moves = [[start]]
    visited = []
    moves = list_of_valid_moves.pop(0)

    while True:

        for check in ["U", "R", "D", "L"]:
            temp_list = []
            if valid_move(moves, check, visited, obst_import):
                print("HERE")
                temp_list = moves
                temp_list.append(convert(moves[len(moves)-1], check))
                list_of_valid_moves.append(temp_list)
                visited.append(moves[len(moves)-1])
        
        print(len(list_of_valid_moves))
        if len(list_of_valid_moves) > 0:
            moves = list_of_valid_moves.pop(0)
        
        print(moves)
        if find_end(start, moves, end):
            return moves