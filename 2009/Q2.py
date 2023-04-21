'''coloured tiles in a 4 by 4 grid'''

debug = False

class Grid():
    '''4 by 4 playing grid'''
    all_tiles = [0, 1, 2, 3, 4, 5, 6 ,7, 8, 9, 10, 11, 12, 13, 14, 15]
    
    def __init__(self) -> None:
        
        self.available = [] + Grid.all_tiles
        self.stack0 = list('GRGR')
        self.stack1 = list('BRRR')
        self.stack2 = list('RGBG')
        self.stack3 = list('BBGB')
        self.stacks = [self.stack0, self.stack1, self.stack2, self.stack3]
        self.index = [0] * 4
        self.tiles = [' '] *16
        self.matched_tiles = []

    def fill_from_stack(self, column):
        '''fills grid tiles from the stack above the grid'''
        result = self.stacks[column][self.index[column]]
        self.index[column] = (self.index[column] + 1) % 4
        return result
    
    def fill_from_above(self, tile):
        '''fills a tile with the value of the tile directly above it'''
        if tile > 3:
            self.tiles[tile] = self.tiles[tile-4]
            self.fill_from_above(tile-4)
        else: self.tiles[tile] = self.fill_from_stack(tile%4)
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
        if tile % 4 > 0:
            if self.tiles[tile] == self.tiles[tile -1] and (tile - 1) in self.available:
                result = tile -1
        return result
    
    def look_right(self, tile):
        '''return tile number for matching tile, else -1'''
        result = -1
        if tile % 4 < 3:
            if self.tiles[tile] == self.tiles[tile +1] and (tile + 1) in self.available:
                result = tile +1
        return result
    
    def look_up(self, tile):
        '''return tile number for matching tile, else -1'''
        result = -1
        if tile // 4 > 0:
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
    

myGrid = Grid()
myGrid.fill_grid()

print(f'original grid: {myGrid}')

#print(myGrid.find_sets())
groups = myGrid.find_sets()
score = 1
for each in groups:
    score = score * each
if score == 1: score =0
print(score)

# remove matched tiles
myGrid.remove_sets()
#print(myGrid)

print('second round...')
myGrid.fill_grid()
print(myGrid)

groups = myGrid.find_sets()
score = 1
for each in groups:
    score = score * each
if score == 1: score =0
print(score)

# remove matched tiles
myGrid.remove_sets()
#print(myGrid)

print('third round...')
myGrid.fill_grid()
print(myGrid)