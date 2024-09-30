
class Robot:
    # The application is a simulation of a toy robot moving on
    # a square table top, of dimensions 5 units x 5 units.
    MIN_X = 0
    MIN_Y = 0
    MAX_X = 4
    MAX_Y = 4
    COMMANDS = ["PLACE", "MOVE", "RIGHT", "LEFT", "REPORT", "EXIT"]
    ERROR_MESSAGES = {
        "invalid": "Invalid command.",
        "place": "Usage: PLACE x,y,direction",
        "positive_only": "Coordinates should be positive integer only",
        "range": f"Coordinates should only be between {MIN_X} and {MAX_X}"
    }
    speed = 1   # We can make this robot faster in the future
    COMPASS = {
        "NORTH": [0, speed],
        "EAST": [speed, 0],
        "SOUTH": [0, -speed],
        "WEST": [-speed, 0]
    }
    is_active = False   # Terminates the loop
    facing = None
    curr_x = 0
    curr_y = 0

    def __init__(self):
        # Activate the robot
        self.is_active = True

    def __str__(self):
        # returns human readable version of the object
        if self.is_on_the_table:
            return f"{self.curr_x},{self.curr_y},{self.facing}"
        return ""

    @property
    def is_on_the_table(self):
        """Flag that tells us the robot is on the table"""
        # This just checks that facing is set.
        # Currently it will only be set by using of the place function.
        # All commands until then gives a return value of None
        return bool(self.facing)

    def place(self, x, y, f):
        """Function that sets the location and direction of the robot"""
        try:
            next_x = int(x)
            next_y = int(y)
        except ValueError:
            print(self.ERROR_MESSAGES['place'])
            return None
        if any([next_x < 0, next_y < 0]):
            print(self.ERROR_MESSAGES['positive_only'])
            return None
        if any([
            next_x not in range(self.MIN_X, self.MAX_X + 1),
            next_y not in range(self.MIN_Y, self.MAX_Y + 1),
        ]):
            print(self.ERROR_MESSAGES['range'])
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
        if not self.is_on_the_table:
            return None
        move_x, move_y = self.COMPASS[self.facing]
        next_x = sum([self.curr_x, move_x])
        next_y = sum([self.curr_y, move_y])
        # Check if the robot will fall
        will_fall = any([
            next_x < self.MIN_X,
            next_y < self.MIN_Y,
            next_x > self.MAX_X,
            next_y > self.MAX_X
        ])
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
        if self.is_on_the_table:
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
        if not self.is_on_the_table:
            return None
        print(self.__str__())
