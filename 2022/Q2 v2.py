# https://www.olympiad.org.uk/papers/2022/bio/bio22-exam.pdf
#
# in this version i'll use a linear run of 25 hexagons and a look up table for neighbours
# problem is I can't find a quick easy soln to find neighbors from a given hex (else a grid makes more sense)

# edit from laptop

# contants
RED_MOVE_DISTANCE  = 9
BLUE_MOVE_DISTANCE = 3


class hexagon():
    '''the building block of hive with 6 sides that can be set to red/blue'''
    def __init__(self) -> None:
        self.hex_controller = None
        self.sides_list = []
        for n in range (6):
            side = None
            self.sides_list.append(side)


    def get_controller(self):
        '''returns team with majority sides or None'''
        controller = "None"
        if self.sides_list.count("R") > self.sides_list.count("B"):
            controller = "R"
        if self.sides_list.count("B") > self.sides_list.count("R"):
            controller = "B"
        return controller


    def __str__(self) -> str:
        rep = ""
        for item in self.sides_list:
            rep += str(item) + " "
        return rep


class hive():
    '''a set of 25 hexagons'''

    # neighbours is a list of all 25 hexagons, each with a list of neighbours per side
    # NOTE look up cells in range 0-24, and sides in range 0-5
    # NOTE returned cell number is in range 1-25 
    # e.g cell=0 (first list), side=1 (second value in sublist) returns cell 2 as neighbour
    neighbours = [
        [None,2,6,None,None,None],
        [None,3,7,6,1,None],
        [None,4,8,7,2,None],
        [None,5,9,8,3,None],
        [None,None,10,9,4,None],
        
        [2,7,12,11,None,1],
        [3,8,13,12,6,2],
        [4,9,14,13,7,3],
        [5,10,15,14,8,4],
        [None,None,None,13,9,5],

        [6,12,16,None,None,None],
        [7,13,17,16,11,6],
        [8,14,18,17,12,7],
        [9,15,19,18,11,8],
        [10,None,20,19,14,9],

        [12,17,22,21,None,11],
        [13,18,23,22,16,12],
        [14,19,24,23,17,13],
        [15,20,25,24,18,14],
        [None,None,None,25,19,15],

        [16,22,None,None,None,None],
        [17,23,None,None,21,16],
        [18,24,None,None,22,17],
        [19,25,None,None,23,18],
        [20,None,None,None,24,19]
        ]

    def __init__(self) -> None:
        self.hex_list = []
        for n in range (25):
            hex = hexagon()
            self.hex_list.append(hex)


    def get_hex_controller(self, ref):
        '''returns team with majority sides or None'''
        return self.hex_list[ref].get_controller()


    def set_hex_side(self, hex, side, team):
        '''sets contorol of hexagon sides when a bee lands'''
        self.hex_list[hex].sides_list[side] = team
        # and also set the corresponding side of neighbouring hexagons
        hex_neighbour = hive.neighbours[hex][side] # -1 see neighbour NOTE
        # neighbour's side is opposite side 
        side_neighbour = side + 3
        if side_neighbour > 5:
            side_neighbour -= 6
        if hex_neighbour:
            self.hex_list[int(hex_neighbour) -1].sides_list[side_neighbour] = team


    def __str__(self) -> str:
        '''returns a representation of the hive status'''
        rep = ""
        for hex in range (25):
            rep += str(self.hex_list[hex]) + "\n"
        return rep


class bee():
    '''buzzes around the hive setting sides to it's team colour'''
    def __init__(self, start_hex, start_direction, rotation, move_distance) -> None:
        self.position = start_hex
        self.move_distance = move_distance
        self.direction = start_direction
        self.rotation = rotation

    
    def rotate_move(self, move):
        '''rotates the bee and moves it's set move distance'''
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
    
####################
# Main starts here #
####################

myHive = hive()

"Two drones are in the hive: a red drone on hexagon 1 facing edge 1" 
"and a blue drone on hexagon 25 facing edge 6."
red = bee(start_hex=0, start_direction=0, rotation=1, move_distance=RED_MOVE_DISTANCE)
blue = bee(start_hex=24, start_direction=5, rotation=-1, move_distance=BLUE_MOVE_DISTANCE)

for n in range(3):
    skirmish()

print("print hive representation")
print(myHive)

print("Hive hex controller summary")

for n in range (25):
    print(n+1, end=" ")
    print(myHive.get_hex_controller(n))

