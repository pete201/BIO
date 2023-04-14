# sort shirts on a line
# works but not very well.  does not find every sort
# e.g. 5674321 is not found within 100 moves (should take 14)

debug = False
max_count = 100

if debug: washing_line = "6417352"
else: washing_line = input("enter 7 digit number: ")

def leftmost(instring):
    return instring[1:4] + instring[0] + instring[4:] 

def rightmost(instring):
    return instring[0:3] + instring[6] + instring[3:6] 

def middle_left(instring):
    return instring[3] + instring[0:3] + instring[4:] 

def middle_right(instring):
    return instring[0:3] + instring[4:] + instring[3]
 
# that's the easy bit done, now I need an algorithm
# try:
# perform each operation and see which result gives most connections
# a connection is counted for any digit which is adjacent to next in sequence

def count_in_sequence(instring):
    count = 0
    i=0
    for i in range(6):
        if int(instring[i]) == int(instring[i+1]) - 1:
            count += 1
    if debug:
        print('count_in_sequence: ',instring,':',count )
    return count

def find_best_move(instring):
    moves = (leftmost, rightmost, middle_left, middle_right)
    results = [0,0,0,0]
    for i in range(4):
        results[i] = count_in_sequence(moves[i](instring))
    best = results.index(max(results))
    return moves[best]

print(f'original = {washing_line}')
count = 0
while not (washing_line == '1234567') and count < max_count:
    next_move = find_best_move(washing_line)
    washing_line = next_move(washing_line)
    count += 1
    if debug:
        print(f'count = {count}, line = {washing_line}')

if washing_line == '1234567':
    print('completed in:', count)
else:
    print('error, did not complete')
