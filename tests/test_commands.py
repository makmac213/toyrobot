from toyrobot.classes.robot import Robot


def test_output_a_console(capfd, monkeypatch):
    robot = Robot()
    monkeypatch.setattr("builtins.input", lambda _: "PLACE 0,0,NORTH")
    robot.parse_command()
    monkeypatch.setattr("builtins.input", lambda _: "MOVE")
    robot.parse_command()
    monkeypatch.setattr("builtins.input", lambda _: "REPORT")
    robot.parse_command()
    robot.is_active = False
    out, err = capfd.readouterr()
    # adding \n as print adds new line character
    assert out == "0,1,NORTH\n"


def test_output_b_console(capfd, monkeypatch):
    robot = Robot()
    monkeypatch.setattr("builtins.input", lambda _: "PLACE 0,0,NORTH")
    robot.parse_command()
    monkeypatch.setattr("builtins.input", lambda _: "LEFT")
    robot.parse_command()
    monkeypatch.setattr("builtins.input", lambda _: "REPORT")
    robot.parse_command()
    robot.is_active = False
    out, err = capfd.readouterr()
    # adding \n as print adds new line character
    assert out == "0,0,WEST\n"


def test_output_c_console(capfd, monkeypatch):
    robot = Robot()
    monkeypatch.setattr("builtins.input", lambda _: "PLACE 1,2,EAST")
    robot.parse_command()
    monkeypatch.setattr("builtins.input", lambda _: "MOVE")
    robot.parse_command()
    monkeypatch.setattr("builtins.input", lambda _: "MOVE")
    robot.parse_command()
    monkeypatch.setattr("builtins.input", lambda _: "LEFT")
    robot.parse_command()
    monkeypatch.setattr("builtins.input", lambda _: "MOVE")
    robot.parse_command()
    monkeypatch.setattr("builtins.input", lambda _: "REPORT")
    robot.parse_command()
    robot.is_active = False
    out, err = capfd.readouterr()
    # adding \n as print adds new line character
    assert out == "3,3,NORTH\n"


def test_invalid_place_values(capfd, monkeypatch):
    robot = Robot()
    # invalid x
    monkeypatch.setattr("builtins.input", lambda _: "PLACE A,2,EAST")
    robot.parse_command()
    robot.is_active = False
    out, err = capfd.readouterr()
    # adding \n as print adds new line character
    assert out == f"{Robot.ERROR_MESSAGES.get('place')}\n"
    # invalid y
    monkeypatch.setattr("builtins.input", lambda _: "PLACE 1,B,EAST")
    robot.parse_command()
    robot.is_active = False
    out, err = capfd.readouterr()
    # adding \n as print adds new line character
    assert out == f"{Robot.ERROR_MESSAGES.get('place')}\n"
    # invalid direction
    monkeypatch.setattr("builtins.input", lambda _: "PLACE 1,B,EASTERN")
    robot.parse_command()
    robot.is_active = False
    out, err = capfd.readouterr()
    # adding \n as print adds new line character
    assert out == f"{Robot.ERROR_MESSAGES.get('place')}\n"


def test_negative_x(capfd, monkeypatch):
    robot = Robot()
    # invalid x
    monkeypatch.setattr("builtins.input", lambda _: "PLACE -1,2,WEST")
    robot.parse_command()
    robot.is_active = False
    out, err = capfd.readouterr()
    # adding \n as print adds new line character
    assert out == f"{Robot.ERROR_MESSAGES.get('positive_only')}\n"


def test_negative_y(capfd, monkeypatch):
    robot = Robot()
    # invalid x
    monkeypatch.setattr("builtins.input", lambda _: "PLACE 2,-2,WEST")
    robot.parse_command()
    robot.is_active = False
    out, err = capfd.readouterr()
    # adding \n as print adds new line character
    assert out == f"{Robot.ERROR_MESSAGES.get('positive_only')}\n"


def test_invalid_command(capfd, monkeypatch):
    robot = Robot()
    invalid_command = "FLY 0,0,1"
    monkeypatch.setattr("builtins.input", lambda _: invalid_command)
    response = robot.parse_command()
    assert response.get("error")
    assert response.get("msg") == f"{Robot.ERROR_MESSAGES.get('invalid')}"


def test_invalid_valid_command(capfd, monkeypatch):
    robot = Robot()
    invalid_command = "LEFT 0,0,NORTH"
    monkeypatch.setattr("builtins.input", lambda _: invalid_command)
    response = robot.parse_command()
    assert response.get("error")
    assert response.get("msg") == f"{Robot.ERROR_MESSAGES.get('invalid')}"
