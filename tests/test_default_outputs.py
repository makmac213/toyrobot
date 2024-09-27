from toyrobot.classes.robot import Robot


def test_output_a(capfd):
    """Test for output a from the pdf"""
    robot = Robot()
    robot.place(0, 0, "NORTH")
    robot.move()
    robot.report()
    out, err = capfd.readouterr()
    # adding \n as print adds new line character
    assert out == "0,1,NORTH\n"


def test_output_b(capfd):
    """Test for output b from the pdf"""
    robot = Robot()
    robot.place(0, 0, "NORTH")
    robot.rotate("LEFT")
    robot.report()
    out, err = capfd.readouterr()
    # adding \n as print adds new line character
    assert out == "0,0,WEST\n"


def test_output_c(capfd):
    """Test for output c from the pdf"""
    robot = Robot()
    robot.place(1, 2, "EAST")
    robot.move()
    robot.move()
    robot.rotate("LEFT")
    robot.move()
    robot.report()
    out, err = capfd.readouterr()
    # adding \n as print adds new line character
    assert out == "3,3,NORTH\n"
