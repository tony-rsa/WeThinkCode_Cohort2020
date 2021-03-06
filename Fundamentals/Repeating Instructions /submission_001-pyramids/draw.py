def re_run():
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)  
    
    
def    print_spaces(spaces):
    x = 0
    while  x < spaces:
        print(" ", end="")
        x += 1  


def    print_stars(stars, height, i, outline):
    y = 0
    while y < stars:
        if (outline == True) and ((i > 0) and (i < height - 1)) and (y > 0) and (y < stars - 1):
            print(" ", end="")
        else:
            print("*", end="")
        y += 1


# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shapes = ["pyramid", "triangle", "square", "parallelogram", "trapeze", "rhombus"]
    user_input = ""
    while not user_input in shapes:
        user_input = input("Shape?: ").lower()

    return user_input    


# TODO: Step 1 - get height (it must be int!)
def get_height():
    while True:
        try:
            user_input = int(input("Height?: "))
        except ValueError:
            continue
        else:
            return user_input
    

# TODO: Step 2
def draw_pyramid(height, outline):
    if height >= 3 and height <= 80:
        spaces = height - 1
        stars = 1
        i = 0
        while i < height:
            print_spaces(spaces)
            print_stars(stars,  height, i, outline)
            print()
            spaces -= 1
            stars += 2
            i += 1
    else:
        print('》Error: Pyramid must have height between 3 and 80!')
        re_run()


# TODO: Step 3
def draw_square(height, outline):
    if height >= 3 and height <= 80:
        i = 0
        while i < height:
            print_stars(height, height, i, outline)
            print()
            i += 1
    else:
        print('》Error: Square must have height between 3 and 80!')
        re_run()


# TODO: Step 4
def draw_triangle(height, outline):
    if height >= 3 and height <= 80:
        stars = 1
        i = 0
        while i < height:
            print_stars(stars, height, i, outline)
            print()
            stars += 1
            i += 1
    else:
        print('》Error: Triangle must have height between 3 and 80!')
        re_run()


def draw_parallelogram(height, outline):
    if height >= 3 and height <= 50:
        spaces = height - 1
        stars = height * 2
        i = 0
        while i < height :
            print_spaces(spaces)
            print_stars(stars,  height, i, outline)
            print()
            spaces -= 1
            i += 1
    else:
        print('》Error: parallelogram height must be between 3 and 50!')


def handel_rhombus(stars, spaces, height, i):
    if (i < (height-1)/2):
        stars += 2
        spaces -= 1
    else:
        stars -= 2
        spaces += 1
    return stars, spaces


def draw_rhombus(height, outline):
    if height >= 3 and height <= 80:
        stars = 1
        if (height % 2 == 0):
            height = height + 1
        spaces = (height - 1) / 2
        i = 0
        while i < height:
            print_spaces(spaces)
            print_stars(stars, height, i, outline)
            print()
            stars, spaces = handel_rhombus(stars, spaces, height, i)
            i += 1
    else:
        print('》Error: Rhombus must have height between 3 and 80!')


def draw_trapeze(height, outline):
    if height >= 3 and height <= 80:
        spaces = height - 1
        stars = height*2
        i = 0
        while i < height:
            print_spaces(spaces)
            print_stars(stars,  height, i, outline)
            print()
            spaces -= 1
            stars += 2
            i += 1
    else:
        print('》Error: Pyramid must have height between 3 and 80!')
        re_run()

 
# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if (shape == "pyramid"):
        draw_pyramid(height, outline)
    elif (shape == "square"):
        draw_square(height, outline)
    elif (shape == "triangle"):
        draw_triangle(height, outline)
    elif (shape == 'parallelogram'):
        draw_parallelogram(height,  outline)
    elif (shape == 'rhombus'):
        draw_rhombus(height,  outline)
    elif (shape == 'trapeze'):
        draw_trapeze(height,  outline)
    else:
        print('》Error: Cannot print shape! try - pyramid, square, triangle, parallelogram, rhombus or cross.')


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    result = False
    user_input = input("Outline only? (y/N):")
    try:
        if (user_input[0] == 'y'):
            result = True
    except:
        pass
    return result


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)