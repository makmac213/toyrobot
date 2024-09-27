
class Robot:
    COMMANDS = ["PLACE", "MOVE", "RIGHT", "LEFT", "REPORT", "EXIT"]
    ERROR_MESSAGES = {
        "invalid": "Invalid command.",
        "place": "Usage: PLACE x,y,direction",
        "positive_only": "Coordinates should be positive integer only",
    }

    speed = 1   # We can make this robot faster in the future
    COMPASS = {
        "NORTH": [0, speed],
        "EAST": [speed, 0],
        "SOUTH": [0, -speed],
        "WEST": [-speed, 0]
    }
    is_active = False
    facing = None
    curr_x = 0
    curr_y = 0

    def __init__(self):
        # Activate the robot
        self.is_active = True

    def __str__(self):
        # returns human readable version of the object
        if self.facing:
            return f"{self.curr_x},{self.curr_y},{self.facing}"
        return ""

    def place(self, x, y, f):
        """Function that sets the location and direction of the robot"""
        try:
            next_x = int(x)
            next_y = int(y)
        except ValueError:
            print(self.ERROR_MESSAGES['place'])
            return None
        if next_x < 0:
            print(self.ERROR_MESSAGES['positive_only'])
            return None
        if next_y < 0:
            print(self.ERROR_MESSAGES['positive_only'])
            return None
        if f not in self.COMPASS.keys():
            print(self.ERROR_MESSAGES['place'])
            return None
        self.curr_x = next_x
        self.curr_y = next_y
        self.facing = f.strip()

    def move(self):
        """Function that moves the robot"""
        # check if facing is set, if not return
        if not self.facing:
            return None
        move_x, move_y = self.COMPASS[self.facing]
        next_x = sum([self.curr_x, move_x])
        next_y = sum([self.curr_y, move_y])
        # Check if the robot will fall
        will_fall = any([next_x == -1, next_y == -1])
        if will_fall:
            return None
        # it did not fall then set current coordinates
        self.curr_x = next_x
        self.curr_y = next_y

    def rotate(self, direction):
        """Rotate robot 90 degrees to the direction"""
        # We could have utilized the below code to get a list
        # of the directions but this will not work on older
        # python versions (e.g. 2.7) but will work in newer versions
        # of Python.
        # compass_keys = list(self.COMPASS.keys())
        if self.facing:
            compass_keys = ["NORTH", "EAST", "SOUTH", "WEST"]
            curr_facing_idx = compass_keys.index(self.facing)
            if direction == "RIGHT":
                next_idx = (curr_facing_idx + 1) % 4
                next_facing = compass_keys[next_idx]
            elif direction == "LEFT":
                next_idx = curr_facing_idx - 1
                if next_idx < 0:
                    next_idx = 3
                next_facing = compass_keys[next_idx]
            self.facing = next_facing

    def parse_command(self):
        """Process the user input"""
        # We use max split here so that there will be a possibility to
        # split PLACE command if user accidentally adds spaces to its
        # parameters
        status = {"error": False, "msg": ""}
        invalid_command_status = {
            "error": True,
            "msg": self.ERROR_MESSAGES['invalid']
        }
        invalid_place_status = {
            "error": True,
            "msg": self.ERROR_MESSAGES['place']
        }
        command = input(">").split(" ", 1)
        # split the existing commands to single-word
        # commands (MOVE, RIGHT, LEFT, REPORT)
        # and PLACE. This is for command validation
        action = command[0]
        if action in self.COMMANDS:
            if len(command) == 1:
                if action == "MOVE":
                    self.move()
                elif action == "REPORT":
                    self.report()
                elif action in ["RIGHT", "LEFT"]:
                    self.rotate(action)
                elif action == "EXIT":
                    self.is_active = False
                else:
                    status = invalid_place_status
            elif len(command) == 2 and action == "PLACE":
                args = command[1].split(",")
                if len(args) == 3:
                    self.place(*args)
                else:
                    status = invalid_place_status
            else:
                status = invalid_command_status
        else:
            status = invalid_command_status
        return status

    def report(self):
        """Report the robot's current coordinates and direction"""
        if not self.facing:
            return None
        print(self.__str__())
