# sort shirts on a line
# works but not very well.  does not find optimum sort
# e.g. 7123456 should take 2 moves, but my prog takes 4

debug = False
max_count = 10

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
 

print(f'original = {washing_line}')

# that's the easy bit done, now I need an algorithm

# try:
# perform each operation and see which result gives most chars in sequence
# in sequence is counted for any digit which is adjacent to next in sequence
# e.g. 7126345 would yield 5 in sequence digits

def count_in_sequence(instring):
    count = 0
    i=0
    for i in range(7):
        if i < 6:
            if int(instring[i]) == int(instring[i+1]) - 1:
                count += 1
            elif int(instring[i]) == int(instring[i-1]) + 1:
                count += 1
        elif i == 6:
            if int(instring[i]) == int(instring[i-1]) + 1:
                count += 1
    #debug
    print('count_in_sequence: ',instring,':',count )
    #ENDdebug
    return count

def find_best_move(instring):
    moves = (leftmost, rightmost, middle_left, middle_right)
    results = [0,0,0,0]
    for i in range(4):
        results[i] = count_in_sequence(moves[i](instring))
    best = results.index(max(results))
    return moves[best]

count = 0
while not (washing_line == '1234567') and count < max_count:
    next_move = find_best_move(washing_line)
    washing_line = next_move(washing_line)
    count += 1
    print(f'count = {count}, line = {washing_line}')

print('completed in:', count)
