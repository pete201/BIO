# i'll use a string instead of a list

debug = False
max_count = 100

if debug:
    washing_line = "6417352"
else:
    washing_line = input("enter 7 digit number: ")


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
# find pairing that gives longest sequence
# else find number that is out of sequence and move it closer to it's intended position

def find_pair(instring):
    '''Looks for a move that results in a number pairing; returns 0 if pairing found, 1 if not'''
    # test move 1 - leftmost to middle...
    if abs(instring[0]-instring[3])==1 or abs(instring[0]-instring[4])==1:
        leftmost(instring)
        return 0 
    # test move 2 - rightmost to middle...
    if abs(instring[6]-instring[2])==1 or abs(instring[0]-instring[3])==1:
        rightmost(instring)
        return 0
    # test move 3 - middle to left...
    if abs(instring[3]-instring[0])==1:
        middle_left(instring)
        return 0
    # test move 4 - middle to right...
    if abs(instring[3]-instring[6])==1:
        middle_right(instring)
        return 0
    return 1 #pairing not found

def find_out_of_sequence(instring):
    '''Looks for first number that is not paired and moves it! '''
    # test move 1 - leftmost to middle...
    if abs(instring[0]-instring[1]) != 1:
        leftmost(instring)
        return
    # test move 2 - rightmost to middle...
    if abs(instring[6]-instring[5]) != 1:
        rightmost(instring)
        return
    # test move 3 - middle to left if value is <4...
    if abs(instring[3]-instring[2])!=1 and abs(instring[3]-instring[4])!=1:
        if instring[3] < 4:
            middle_left(instring)
        # DEFAULT move 4 - middle to left if value is >3...
        else middle_right(instring)
        return
    

count = 0
while not (washing_line == '1234567') and count < max_count:
    if not find_pair(washing_line):
        find_out_of_sequence(washing_line)
    count += 1
    print(f'count = {count}, line = {washing_line}')

print('the end:', washing_line)
