from toyrobot.classes.robot import Robot


def test_rotate_right_360():
    robot = Robot()
    robot.place(0, 0, "NORTH")
    robot.rotate("RIGHT")
    assert robot.facing == "EAST"
    robot.rotate("RIGHT")
    assert robot.facing == "SOUTH"
    robot.rotate("RIGHT")
    assert robot.facing == "WEST"
    robot.rotate("RIGHT")
    assert robot.facing == "NORTH"


def test_rotate_left_360():
    robot = Robot()
    robot.place(0, 0, "SOUTH")
    robot.rotate("LEFT")
    assert robot.facing == "EAST"
    robot.rotate("LEFT")
    assert robot.facing == "NORTH"
    robot.rotate("LEFT")
    assert robot.facing == "WEST"
    robot.rotate("LEFT")
    assert robot.facing == "SOUTH"


def test_will_not_fall_min_x():
    """Robot is facing west and will move 3 times"""
    robot = Robot()
    robot.place(1, 0, "WEST")
    robot.move()
    robot.move()
    robot.move()
    assert robot.curr_x == 0


def test_will_not_fall_max_x():
    robot = Robot()
    robot.place(Robot.MAX_X, 0, "EAST")
    robot.move()
    robot.move()
    robot.move()
    assert robot.curr_x == Robot.MAX_X


def test_will_not_fall_min_y():
    """Robot is facing south and will move 3 times"""
    robot = Robot()
    robot.place(1, 0, "SOUTH")
    robot.move()
    robot.move()
    robot.move()
    assert robot.curr_y == 0


def test_will_not_fall_max_y():
    robot = Robot()
    robot.place(0, Robot.MAX_Y, "NORTH")
    robot.move()
    robot.move()
    robot.move()
    assert robot.curr_y == Robot.MAX_Y


def test_robot_ignores_falling_commands_only():
    robot = Robot()
    robot.place(1, 1, "WEST")
    robot.move()
    robot.move()    # should have fallen here
    robot.rotate("LEFT")
    assert robot.facing == "SOUTH"
    robot.move()    # 0, 0
    robot.move()    # should have fallen here
    robot.rotate("RIGHT")
    robot.rotate("RIGHT")
    assert robot.facing == "NORTH"
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    assert robot.curr_y == 4
