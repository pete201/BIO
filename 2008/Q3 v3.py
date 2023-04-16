# sort shirts on a line
# must iterate through every permutation to find shortest path

debug = False
max_count = 20

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
 
# that's the easy bit done, now I need an algorithm...

print(f'original = {washing_line}')
moves = (leftmost, rightmost, middle_left, middle_right)
# prior moves limits number of permutations to compute
prior_moves = []
pending_moves = [(washing_line, 0)]
count = 0
while not (washing_line == '1234567') and count < max_count:
    count += 1
    for next_move in moves:
        result = next_move(washing_line)
        if result not in prior_moves:
            prior_moves.append(result)
            pending_moves.append((result,count))

    washing_line, count = pending_moves.pop(0)
    if debug:
        print(f'count = {count}, line = {washing_line}')

if washing_line == '1234567':
    print('completed in:', count)
else:
    print('error, did not complete')