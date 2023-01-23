# https://www.olympiad.org.uk/papers/2022/bio/bio22-exam.pdf
#
# in this version i'll use a 5x5 array of hexagons attempting to find neighbours from a given hex

# contants
RED_MOVE_DISTANCE  = 1
BLUE_MOVE_DISTANCE = 14
SKIRMISHES = 31
FEUDS = 19

class hexagon():
    '''the building block of hive with 6 sides that can be set to red/blue'''
    def __init__(self) -> None:
        self.sides = []
        for _ in range (6):
            self.sides.append('_')

    def get_count(self, drone):
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


    def get_count(self, hex_coords, drone):
        return self.rows[hex_coords[0]][hex_coords[1]].get_count(str(drone))
         

    def set_hex_side(self, hex_coords, side, drone):
        '''sets owner of hexagon sides when a bee lands'''
        self.rows[hex_coords[0]][hex_coords[1]].sides[side] = drone
        #TODO neighbours

    
    def __str__(self) -> str:
        '''returns a representation of the hive status'''
        rep = ""
        for r in range(len(self.rows)):
            for c in range (len(self.hexagons)):
                rep += str(self.rows[r][c]) + "\t"
            rep += "\n"
        return rep


class drone():
    '''buzzes round the hive setting sides as it goes'''
    def __init__(self, name, start_coords, start_direction, rotation, move_distance) -> None:
        self.name = name
        self.position = start_coords
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

        #TODO - change this to co-ordinates system
        #  self.position += self.move_distance
        # if self.position > 24:
        #     self.position -= 25 #25 hexagons in the hive
        # if self.position < 0:
        #     self.position += 25


###################################################################################
#  MAIN  #

myHive = hive()


myHive.set_hex_side([0,0],side=0, drone='R')
myHive.set_hex_side([0,0],side=1, drone='R')
myHive.set_hex_side([0,0],side=5, drone='B')

count_red = myHive.get_count([0,0], 'R')
count_blue = myHive.get_count([0,0], 'B')
print('R B : ', count_red, count_blue, '\n')

print(myHive)
