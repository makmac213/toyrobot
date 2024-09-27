from classes.robot import Robot


def console():
    robot = Robot()
    while robot.is_active:
        response = robot.parse_command()
        if response.get('error'):
            print(response.get('msg'))


def main():
    # if input via console
    console()


if __name__ == "__main__":
    main()
