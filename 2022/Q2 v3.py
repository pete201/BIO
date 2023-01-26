# https://www.olympiad.org.uk/papers/2022/bio/bio22-exam.pdf
#
# in this version i'll use a 5x5 array of hexagons attempting to find neighbours from a given hex

# contants
RED_MOVE_DISTANCE  = 9
BLUE_MOVE_DISTANCE = 3
SKIRMISHES = 3
FEUDS = 19

class hexagon():
    '''the building block of hive with 6 sides that can be set to red/blue'''
    def __init__(self) -> None:
        self.sides = []
        for _ in range (6):
            self.sides.append('_')

    def get_sides_count(self, drone):
        '''returns number of sides for drone'''
        return self.sides.count(drone)

    def __str__(self) -> str:
        rep = ""
        for item in self.sides:
            rep += item + "."
        return rep


class hive():
    '''a 5x5 array of hexagons'''
    def __init__(self) -> None:
        self.rows = []
        for row in range(5):
            self.hexagons = []
            for col in range(5):
                self.hexagons.append(hexagon())
            self.rows.append(self.hexagons)

    def get_side_count(self, hex_coords, drone):
        return self.rows[hex_coords[0]][hex_coords[1]].get_sides_count(drone.name)
         
    def take_ownership(self, drone):
        '''sets owner of adjoining hexagon sides when a bee lands'''
        # first, take ownership of this hexagon side that drone is facing
        self.set_hexagon_side(drone.position, drone.direction, drone.name)
        # then get neighbour of facing side
        neighbour = self.get_neighbour(drone.position, drone.direction)
        # and take ownership of adjoining edge
        self.set_opposite_side(neighbour, drone.direction, drone.name)


    def get_neighbour(self, drone_coords, drone_direction):
        '''finds neighbouring hex that drone is facing'''

        
        #TODO - DISALLOW NEIGHBOURS OUT OF RANGE


        # neighbours depend upon odd/even row number  (row%2 = 1 for odd rows)
        # so, for TR and BR = current cell number + row%2
        # and for TL and BL = current cell number -1 + row%2 
        
        neighbour = [-1,-1]
        # TOP RIGHT:
        if drone_direction == 0:
            if drone_coords[0] > 0:   # only look for top neighbour if not in top row
                neighbour[0] = (drone_coords[0] - 1)
                neighbour[1] = drone_coords[1] + drone_coords[0]%2
                if neighbour[1] < 5:
                    #print(drone_coords,'found a neighbour at', neighbour)
        # RIGHT:
        if drone_direction == 1:
            neighbour[0] = drone_coords[0]
            if drone_coords[1] < 4:
                neighbour[1] = drone_coords[1] + 1
                print(drone_coords,'found a neighbour at', neighbour)
        # BOTTOM RIGHT:
        if drone_direction == 2:
            if drone_coords[0] < 4:   # only look for top neighbour if not in bottom row
                neighbour[0] = (drone_coords[0] + 1)
                neighbour[1] = drone_coords[1] + drone_coords[0]%2
                if neighbour[1] < 5:
                    print(drone_coords,'found a neighbour at', neighbour)
        # BOTTOM LEFT:
        if drone_direction == 3:
            if drone_coords[0] < 4:   # only look for top neighbour if not in bottom row
                neighbour[0] = (drone_coords[0] + 1)
                neighbour[1] = drone_coords[1] -1 + drone_coords[0]%2
                if neighbour[1] > -1:
                    print(drone_coords,'found a neighbour at', neighbour)
        # LEFT:
        if drone_direction == 4:
            neighbour[0] = drone_coords[0]
            if drone_coords[1] > 0:
                neighbour[1] = drone_coords[1] - 1
                print(drone_coords,'found a neighbour at', neighbour)
        # TOP LEFT:
        if drone_direction == 5:
            if drone_coords[0] > 0:   # only look for top neighbour if not in top row
                neighbour[0] = (drone_coords[0] - 1)
                neighbour[1] = drone_coords[1] -1 + drone_coords[0]%2
                if neighbour[1] > -1:
                    print(drone_coords,'found a neighbour at', neighbour)

        return neighbour
        
    def set_opposite_side(self, hex_coords, side, name):
        '''given a hexagon side, returns opposite side'''
        opposite = side + 3
        if opposite > 5:
            opposite -= 6
        self.rows[hex_coords[0]][hex_coords[1]].sides[opposite] = name

    def set_hexagon_side(self, hex_coords, side, name):
        self.rows[hex_coords[0]][hex_coords[1]].sides[side] = name

    def __str__(self) -> str:
        '''returns a representation of the hive status'''
        rep = ""
        for r in range(len(self.rows)):
            for c in range (len(self.hexagons)):
                rep += str(self.rows[r][c]) + "\t"
            rep += "\n"
        return rep


class drone():
    '''buzzes round the hive setting sides as it goes
    Start Direction = hex wall number (0-5)
    Rotation is either +1 or -1'''
    def __init__(self, name, start_coords, start_direction, rotation, move_distance) -> None:
        self.name = name
        self.position = start_coords
        self.move_distance = move_distance
        self.direction = start_direction
        self.rotation = rotation

    def rotate_move(self):
        '''rotates the bee and moves it's set move distance'''
        self.direction += self.rotation
        if self.direction > 5:
            self.direction = 0
        if self.direction < 0:
            self.direction = 5

        # note moves are always forwards
        self.position[1] += self.move_distance
        while self.position[1] > 4:
            self.position[1] -= 5 # 5 hexagons in each row
            self.position[0] += 1
            if self.position[0] > 4:
                self.position[0] -= 5   # 5 rows in the hive


def skirmish(n):
    for _ in range(n):
        myHive.take_ownership(red)
        red.rotate_move()

        myHive.take_ownership(blue)
        blue.rotate_move()
        print(red.position, blue.position)

###################################################################################
#  MAIN  #

myHive = hive()

red = drone('R', [0,0], 0, 1, RED_MOVE_DISTANCE)
blue = drone('B', [4,4], 5, -1, BLUE_MOVE_DISTANCE)

skirmish(SKIRMISHES)
    
print(myHive)


red_control_count = 0
blue_control_count = 0

for row in range(5):
    for col in range(5):
        if myHive.get_side_count([row,col], red) > myHive.get_side_count([row,col], blue):
            red_control_count +=1
        if myHive.get_side_count([row,col], blue) > myHive.get_side_count([row,col], red):
            blue_control_count +=1

print('Red controlls : ', red_control_count)
print('Blue controlls: ', blue_control_count)
