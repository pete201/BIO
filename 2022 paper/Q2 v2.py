# https://www.olympiad.org.uk/papers/2022/bio/bio22-exam.pdf
#
# in this version i'll use a linear run of 25 hexagons and a look up table for neighbours
# problem is I can't find a quick easy soln to find neighbors from a given hex (else a grid makes more sense)

# contants
RED_MOVE_DISTANCE  = 25
BLUE_MOVE_DISTANCE = 15
SKIRMISHES = 3
FEUDS = 13

class hexagon():
    '''the building block of hive with 6 sides that can be set to red/blue'''
    def __init__(self) -> None:
        self.hex_controller = None
        self.sides_list = []
        for n in range (6):
            side = '_'
            self.sides_list.append(side)


    def get_controller(self):
        '''returns team with majority sides or None'''
        controller = "_"
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
    def __init__(self, team, start_hex, start_direction, rotation, move_distance, feud_direction) -> None:
        self.team = team
        self.position = start_hex
        self.move_distance = move_distance
        self.direction = start_direction
        self.rotation = rotation
        self.feud_direction = feud_direction
        if self.feud_direction == 1:
            self.feud_hex_start = 0
            self.feud_hex_stop = 25
            self.feud_side_start = 0
            self.feud_side_stop = 6
        else:
            self.feud_hex_start = 24
            self.feud_hex_stop = -1
            self.feud_side_start = 5
            self.feud_side_stop = -1
    
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

    def feud(self):
        # each bee determines what is preferred edge
        # 1 - gain control over most hexagons
        # 2 - take away control from enemy
        # 3 - hex number red=lowest, blue=highest

        # 1: find adjacent hex's with control==None
        feud_end = False
        for hex in range(self.feud_hex_start,self.feud_hex_stop,self.feud_direction):
            # find controller of this cell == None, continue, else next
            test_hex = myHive.get_hex_controller(hex) 
            if myHive.get_hex_controller(hex) == 'None':
                # see if any neighbour has controller == None
                for side in range (self.feud_side_start,self.feud_side_stop,self.feud_direction):
                    hex_neighbour = myHive.neighbours[hex][side]
                    # sometimes there is no neighbour, so check if neighbour is there
                    if hex_neighbour:
                        # hex neighbour is in range 1-25, so subtract 1
                        hex_neighbour -=1 
                        if myHive.get_hex_controller(hex_neighbour) == 'None':
                            # take control of this hex/side
                            myHive.set_hex_side(hex, side, self.team)
                            feud_end = True
                            break
                if feud_end:
                    break
                



def skirmish():
    # The red drone takes ownership (for the red colony) of the edge it is facing, it then rotates 60°
    # clockwise to face a new edge and finally it jumps r hexagons along the hive.
    myHive.set_hex_side(red.position,red.direction, red.team) 
    red.rotate_move(RED_MOVE_DISTANCE)
    # The blue drone similarly takes ownership of the edge it is facing, it then rotates 60° anti-clockwise to
    # face a new edge before finally jumping b hexagons.
    myHive.set_hex_side(blue.position,blue.direction, blue.team) 
    blue.rotate_move(BLUE_MOVE_DISTANCE)
    
    
####################
# Main starts here #
####################

myHive = hive()

"Two drones are in the hive: a red drone on hexagon 1 facing edge 1" 
"and a blue drone on hexagon 25 facing edge 6."
red = bee(team='R', start_hex=0, start_direction=0, rotation=1, move_distance=RED_MOVE_DISTANCE, feud_direction=1)
blue = bee(team='B', start_hex=24, start_direction=5, rotation=-1, move_distance=BLUE_MOVE_DISTANCE, feud_direction=-1)

for n in range(SKIRMISHES):
    skirmish()



for n in range(FEUDS):
    red.feud()
    blue.feud()


# count cells controlled by red and blue:
print("Hive hex controller summary")
red_total = 0
blue_total = 0
for n in range (25):
    print(n+1, end=" ")
    print(myHive.get_hex_controller(n))
    if myHive.get_hex_controller(n) == 'R':
        red_total += 1
    if myHive.get_hex_controller(n) == 'B':
        blue_total += 1

print("print hive representation")
print(myHive)


print('final results:')
print('red  controlls', red_total)
print('blue controlls', blue_total)
