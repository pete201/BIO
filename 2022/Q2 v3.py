# https://www.olympiad.org.uk/papers/2022/bio/bio22-exam.pdf
#
# in this version i'll use a 5x5 array of hexagons attempting to find neighbours from a given hex


#TODO failed on 25,15,3,13 (should be 10,13)
#TODO failed on 25,24,11,33 (should be 7,16)

# contants
RED_MOVE_DISTANCE  = 18
BLUE_MOVE_DISTANCE = 6
SKIRMISHES = 53
FEUDS = 3

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
        # if a neighbour returned, take ownership of adjoining edge
        if neighbour:
            self.set_opposite_side(neighbour, drone.direction, drone.name)


    def get_neighbour(self, drone_coords, drone_direction):
        '''finds neighbouring hex that drone is facing'''

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
                    return neighbour
        # RIGHT:
        if drone_direction == 1:
            neighbour[0] = drone_coords[0]
            if drone_coords[1] < 4:
                neighbour[1] = drone_coords[1] + 1
                #print(drone_coords,'found a neighbour at', neighbour)
                return neighbour
        # BOTTOM RIGHT:
        if drone_direction == 2:
            if drone_coords[0] < 4:   # only look for top neighbour if not in bottom row
                neighbour[0] = (drone_coords[0] + 1)
                neighbour[1] = drone_coords[1] + drone_coords[0]%2
                if neighbour[1] < 5:
                    #print(drone_coords,'found a neighbour at', neighbour)
                    return neighbour
        # BOTTOM LEFT:
        if drone_direction == 3:
            if drone_coords[0] < 4:   # only look for top neighbour if not in bottom row
                neighbour[0] = (drone_coords[0] + 1)
                neighbour[1] = drone_coords[1] -1 + drone_coords[0]%2
                if neighbour[1] > -1:
                    #print(drone_coords,'found a neighbour at', neighbour)
                    return neighbour
        # LEFT:
        if drone_direction == 4:
            neighbour[0] = drone_coords[0]
            if drone_coords[1] > 0:
                neighbour[1] = drone_coords[1] - 1
                #print(drone_coords,'found a neighbour at', neighbour)
                return neighbour
        # TOP LEFT:
        if drone_direction == 5:
            if drone_coords[0] > 0:   # only look for top neighbour if not in top row
                neighbour[0] = (drone_coords[0] - 1)
                neighbour[1] = drone_coords[1] -1 + drone_coords[0]%2
                if neighbour[1] > -1:
                    #print(drone_coords,'found a neighbour at', neighbour)
                    return neighbour

        return None
        
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
        self.feud_hex_start = start_coords[0]
        if self.feud_hex_start == 0:
            self.feud_hex_stop = 5
        else: self.feud_hex_stop = -1
        self.feud_line_start = start_direction
        if self.feud_line_start == 0:
            self.feud_line_stop = 6
        else: self.feud_line_stop = -1

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

    
def feud(drone, opponent):
    # preff is: +2 hexagons, +1 hex -1 opponent hex, +1 hex, -1 opponent hex, any unoccupied side

    #list neutral hexagons with an unoccupied side
    neutral_avail = []
    for row in range(drone.feud_hex_start , drone.feud_hex_stop, drone.rotation):
        for hex in range(drone.feud_hex_start , drone.feud_hex_stop, drone.rotation):
            hive_hex = [row, hex]
            if myHive.get_side_count(hive_hex, drone) == myHive.get_side_count(hive_hex, opponent):
                # look for an unoccupied side, i.e. == '_'
                for side in range(drone.feud_line_start, drone.feud_line_stop, drone.rotation):
                    if myHive.rows[row][hex].sides[side] == '_':
                        #print(f'neutral hex {hive_hex} has free side at {side}')
                        neutral_avail.append(hive_hex)
                        break
    # +2 hexagons: - must have neutral neighbour
    for each in neutral_avail:
        # look for an unoccupied side, i.e. == '_'
        for side in range(drone.feud_line_start, drone.feud_line_stop, drone.rotation):
            if myHive.rows[each[0]][each[1]].sides[side] == '_':
                neighbour = myHive.get_neighbour(each, side)
                if neighbour:
                    if myHive.get_side_count(neighbour, drone) == myHive.get_side_count(neighbour, opponent):
                        print(f'feud: {drone.name} takes {each} side {side} AND neutral neighbour {neighbour}')
                        myHive.set_hexagon_side(each, side, drone.name)
                        myHive.set_opposite_side(neighbour, side, drone.name)
                        return
    # now look for +1 hex -1 opponent hex...
    for each in neutral_avail:
        # look for an unoccupied side, i.e. == '_'
        for side in range(drone.feud_line_start, drone.feud_line_stop, drone.rotation):
            if myHive.rows[each[0]][each[1]].sides[side] == '_':
                neighbour = myHive.get_neighbour(each, side)
                if neighbour:
                    if myHive.get_side_count(neighbour, drone) + 1 == myHive.get_side_count(neighbour, opponent):
                        print(f'feud: {drone.name} takes {each} side {side} and neutralises opponent neighbour {neighbour}')
                        myHive.set_hexagon_side(each, side, drone.name)
                        myHive.set_opposite_side(neighbour, side, drone.name)
                        return
    # now look for +1 hex 
    for each in neutral_avail:
        # look for an unoccupied side, i.e. == '_'
        for side in range(drone.feud_line_start, drone.feud_line_stop, drone.rotation):
            if myHive.rows[each[0]][each[1]].sides[side] == '_':
                print(f'feud: {drone.name} takes {each} side {side} to take single hexagon')
                myHive.set_hexagon_side(each, side, drone.name)
                #if this side has a neighbour, set that too
                neighbour = myHive.get_neighbour(each, side)
                if neighbour:
                    myHive.set_opposite_side(neighbour, side, drone.name)
                    return
    # now look for -1 opponent hex 
    for row in range(drone.feud_hex_start , drone.feud_hex_stop, drone.rotation):
        for hex in range(drone.feud_hex_start , drone.feud_hex_stop, drone.rotation):
            hive_hex = [row, hex]
            if myHive.get_side_count(hive_hex, drone) +1 == myHive.get_side_count(hive_hex, opponent):
                # look for an unoccupied side, i.e. == '_'
                for side in range(drone.feud_line_start, drone.feud_line_stop, drone.rotation):
                    if myHive.rows[row][hex].sides[side] == '_':
                        print(f'feud: {drone.name} found unoccupied {hive_hex} side {side} to neutralise opponent hexagon')
                        myHive.set_hexagon_side(hive_hex, side, drone.name)
                        #if this side has a neighbour, set that too
                        neighbour = myHive.get_neighbour(hive_hex, side)
                        if neighbour:
                            myHive.set_opposite_side(neighbour, side, drone.name)
                            return

    # lastly, take first unoccupied side:
    for row in range(drone.feud_hex_start , drone.feud_hex_stop, drone.rotation):
        for hex in range(drone.feud_hex_start , drone.feud_hex_stop, drone.rotation):
            hive_hex = [row, hex]
            # look for an unoccupied side, i.e. == '_'
            for side in range(drone.feud_line_start, drone.feud_line_stop, drone.rotation):
                if myHive.rows[row][hex].sides[side] == '_':
                    print(f'feud: {drone.name} found unoccupied {hive_hex} side {side} as a last resort....')
                    myHive.set_hexagon_side(hive_hex, side, drone.name)
                    #if this side has a neighbour, set that too
                    neighbour = myHive.get_neighbour(hive_hex, side)
                    if neighbour:
                        myHive.set_opposite_side(neighbour, side, drone.name)
                        return
    print(f'feud: {drone.name}  NOTHING FOUND')

###################################################################################
#  MAIN  #

myHive = hive()

red = drone('R', [0,0], 0, 1, RED_MOVE_DISTANCE)
blue = drone('B', [4,4], 5, -1, BLUE_MOVE_DISTANCE)

skirmish(SKIRMISHES)
    
#print(myHive)

red_control_count = 0
blue_control_count = 0

for row in range(5):
    for col in range(5):
        if myHive.get_side_count([row,col], red) > myHive.get_side_count([row,col], blue):
            red_control_count +=1
        if myHive.get_side_count([row,col], blue) > myHive.get_side_count([row,col], red):
            blue_control_count +=1

print(f'after {SKIRMISHES} skirmishes...')
print('Red controlls : ', red_control_count)
print('Blue controlls: ', blue_control_count)

for f in range(FEUDS):
    feud(red, blue)
    feud(blue, red)

print(myHive)

red_control_count = 0
blue_control_count = 0
for row in range(5):
    for col in range(5):
        if myHive.get_side_count([row,col], red) > myHive.get_side_count([row,col], blue):
            red_control_count +=1
        if myHive.get_side_count([row,col], blue) > myHive.get_side_count([row,col], red):
            blue_control_count +=1

print(f'after {FEUDS} feuds...')
print('Red controlls : ', red_control_count)
print('Blue controlls: ', blue_control_count)

