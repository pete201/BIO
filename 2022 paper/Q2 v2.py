# in this version i'll use a linear run of 25 hexagons and a look up table for neighbours
# problem is I can't find a quick easy soln to find neighbors from a given hex (else a grid makes more sense)

# contants
RED_MOVE_DISTANCE  = 9
BLUE_MOVE_DISTANCE = 3

neighbours = {
    [0,1]:[1,4],
    [0,2]:[5,5],
}

class hexagon():
    '''the building block of hive with 6 sides that can be set to red/blue'''

    def __init__(self) -> None:

        self.hex_controller = None

        self.sides_list = []
        for n in range (6):
            side = None
            self.sides_list.append(side)

    def get_controller(self):
        for item in self.sides_list:
            print (item, end=" ")
        print()

class hive():
    '''a set of 25 hexagons'''

    def __init__(self) -> None:
        self.hex_list = []
        for n in range (25):
            hex = hexagon()
            self.hex_list.append(hex)

    def get_hex_controller(self, ref):
        self.hex_list[ref].get_controller()

    def set_hex_side(self, hex, side, team):
        self.hex_list[hex].sides_list[side] = team
        # and also set the corresponding side of neighbouring hexagons



class bee():
    '''buzzes around the hive setting sides to it's team colour'''

    def __init__(self, start_hex, start_direction, rotation, move_distance) -> None:
        self.position = start_hex
        self.move_distance = move_distance
        self.direction = start_direction
        self.rotation = rotation

    
    def rotate_move(self, move):
        self.direction += self.rotation
        if self.direction > 5:
            self.direction = 0
        if self.direction < 0:
            self.direction = 5

        self.position += self.move_distance
        if self.position > 24:
            self.position -= 25 #25 hexagons in the hive
        if self.position < 0:
            self.position += 25


def skirmish():
    # The red drone takes ownership (for the red colony) of the edge it is facing, it then rotates 60°
    # clockwise to face a new edge and finally it jumps r hexagons along the hive.
    myHive.set_hex_side(red.position,red.direction, 'R') 
    red.rotate_move(RED_MOVE_DISTANCE)
    # The blue drone similarly takes ownership of the edge it is facing, it then rotates 60° anti-clockwise to
    # face a new edge before finally jumping b hexagons.
    myHive.set_hex_side(blue.position,blue.direction, 'B') 
    blue.rotate_move(BLUE_MOVE_DISTANCE)
    


myHive = hive()

"Two drones are in the hive: a red drone on hexagon 1 facing edge 1" 
"and a blue drone on hexagon 25 facing edge 6."
red = bee(0, 0, 1, RED_MOVE_DISTANCE)
blue = bee(24, 5, -1, BLUE_MOVE_DISTANCE)

for n in range(3):
    skirmish()

# print out the hive:
for n in range (25):
        print(n+1, end=" ")
        myHive.get_hex_controller(n)

print(neighbours([0,1]))