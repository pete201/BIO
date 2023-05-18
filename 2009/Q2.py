'''coloured tiles in a 4 by 4 grid'''

debug = True

class Grid():
    '''4 by 4 playing grid'''
    all_tiles = [0, 1, 2, 3, 4, 5, 6 ,7, 8, 9, 10, 11, 12, 13, 14, 15]
    
    def __init__(self, rows) -> None:
        
        self.available = [] + Grid.all_tiles
        cols = [rows[0][n] + rows[1][n] + rows[2][n] + rows[3][n] for n in range(4)]
        self.stacks = [list(cols[0]), list(cols[1]), list(cols[2]), list(cols[3])]

        self.stack_index = [0] * 4
        self.tiles = [' '] *16
        self.matched_tiles = []

    def fill_from_stack(self, column):
        '''fills grid tiles from the stack above the grid'''
        result = self.stacks[column][self.stack_index[column]]
        self.stack_index[column] = (self.stack_index[column] + 1) % 4
        return result
    
    def fill_from_above(self, tile):
        '''fills a tile with the value of the tile directly above it'''
        while tile > 3:
            self.tiles[tile] = self.tiles[tile - 4]
            tile -= 4
        self.tiles[tile] = self.fill_from_stack(tile % 4)
        return
    
    def fill_grid(self):
        '''fills empty spaces in the grid and resets available tiles'''
        self.available.clear()
        self.available += Grid.all_tiles

        for t in range (15, 0, -1):
            while self.tiles[t] == ' ':
                self.fill_from_above(t)
        return
    
    def look_left(self, tile):
        '''return tile number for matching tile, else -1'''
        result = -1
        if tile % 4 != 0:
            if self.tiles[tile] == self.tiles[tile -1] and (tile -1) in self.available:
                result = tile -1
        return result
    
    def look_right(self, tile):
        '''return tile number for matching tile, else -1'''
        result = -1
        if tile % 4 < 3:
            if self.tiles[tile] == self.tiles[tile +1] and (tile +1) in self.available:
                result = tile +1
        return result
    
    def look_up(self, tile):
        '''return tile number for matching tile, else -1'''
        result = -1
        if tile // 4 != 0:
            if self.tiles[tile] == self.tiles[tile -4] and (tile -4) in self.available:
                result = tile -4
        return result
    
    def look_down(self, tile):
        '''return tile number for matching tile, else -1'''
        result = -1
        if tile // 4 < 3:
            if self.tiles[tile] == self.tiles[tile +4] and (tile +4) in self.available:
                result = tile +4
        return result
    
    def count_neighbours(self, tile):
        '''returns a count of matching tiles'''
        count = 1
        self.available.remove(tile)
        for look in [self.look_left, self.look_right, self.look_up, self.look_down]:
            match = look(tile)
            if match > -1:
                self.matched_tiles.append(tile)
                self.matched_tiles.append(match)
                count += (self.count_neighbours(match))
        return count

    def find_sets(self):
        sets = []
        self.matched_tiles.clear()
        while self.available:                       # while there are available 
            count = self.count_neighbours(self.available[0])
            if count > 1: sets.append(count)
        return sets
    
    def remove_sets(self):
        for tile in self.matched_tiles:
            self.tiles[tile] = ' '
        return
  
    def __str__(self) -> str:
        result = ''
        for index, each in enumerate(self.tiles):
            if index % 4 == 0:
                result = result + '\n'
            result = result + each
        return result
    
if debug:
    rows = ['RRGB', 'GRBG', 'RRGB', 'GBRB']
    number_rounds = 2
else:
    rows = list(input("enter next row: ").upper() for _ in range(4))
    number_rounds = int(input('enter number of rounds: '))
# reverse the rows order before constructing grid since row 0 is at bottom
rows.reverse()

myGrid = Grid(rows)
myGrid.fill_grid()

total = 0
for n in range(number_rounds):
    groups = myGrid.find_sets()
    if len(groups) < 1:
        print()
        print('GAME OVER')
        break
    score = 1
    for each in groups:
        score = score * each
    if score == 1: score = 0
    # remove matched tiles
    myGrid.remove_sets()
    total += score
    myGrid.fill_grid()
    
print(f'grid: {myGrid}')
print(total)
