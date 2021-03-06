def move_square(size):
    """
    This function makes the robot move in the shape a square
    """
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")


def move_rectangle():
    """
    This function makes the robot move in the shape of a rectangle
    """
    length = 20
    width = 10
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")


def move_square_dancing():
    """
    This function makes the robot dance 3 time in the shape of square
    """
    size = 20
    degrees = 90
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        length = 20
        print("* Move Forward "+str(length))
        move_square(20)


def move_circle():
    """
    This function makes the robot move in a circle
    """
    print("Moving in a circle")
    degrees = 1
    for k in range(360):
        length = 1
        print("* Move Forward " + str(length))
        print("* Turn Right " + str(degrees) + " degrees")


def move_crop_circles():
    """
    This function makes the robot crop 4 circls
    """
    print("Crop circles - 4 circles")
    for i in range(4):
        length = 20
        print("* Move Forward "+str(length))
        move_circle()


# TODO: Decompose into functions
def move():
    """
        robotoy_functions(): this function calls all the functions(moves) that move the robot
    """
    move_square(10)
    move_rectangle()
    move_circle()
    move_square_dancing()
    move_crop_circles()


def robot_start():
    """
    This function activates the robot
    """
    move()


if __name__ == "__main__":
    robot_start()
