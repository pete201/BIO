# sort shirts on a line
# works but not very well.  does not find optimum sort
# e.g. 7123456 should take 2 moves, but my prog takes 4

debug = False
max_count = 50

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
# find pairing that gives longest sequence
# else find number that is out of sequence and move it closer to it's intended position

def find_pair(instring):
    '''Looks for a move that results in a number pairing; returns 0 if pairing found, 1 if not'''
    outstring = instring
    # test move 1 - leftmost to middle...
    if int(instring[0]) - int(instring[3]) == 1 or int(instring[0]) - int(instring[4]) == -1:
        outstring = leftmost(instring)
    # test move 2 - rightmost to middle...
    elif int(instring[6]) - int(instring[2])==1 or int(instring[6]) - int(instring[3]) == -1:
        outstring = rightmost(instring)
    # test move 3 - middle to left...
    elif int(instring[3]) - int(instring[0]) == -1:
        outstring = middle_left(instring)
    # test move 4 - middle to right...
    elif int(instring[3]) - int(instring[6])==1:
        outstring = middle_right(instring)
    return outstring, instring != outstring

def find_out_of_sequence(instring):
    '''Looks for first number that is not paired and moves it! '''
    outstring = instring
    # test move 1 - leftmost to middle...
    if int(instring[0]) - int(instring[1]) != -1:
        outstring = leftmost(instring)
    # test move 2 - rightmost to middle...
    elif int(instring[6]) - int(instring[5]) != 1:
        outstring = rightmost(instring)
    # test move 3 - middle to left if value is <4...
    elif int(instring[3]) - int(instring[2]) != 1 and int(instring[3]) - int(instring[4]) != -1:
        if int(instring[3]) < 4:
            outstring = middle_left(instring)
        # DEFAULT move 4 - middle to right if value is >3...
        else: outstring = middle_right(instring)
    return outstring, instring != outstring
    

count = 0
while not (washing_line == '1234567') and count < max_count:
    washing_line, pair_found = find_pair(washing_line)
    if not pair_found:
        washing_line, seq_found = find_out_of_sequence(washing_line)
        if not seq_found:
            print('ERROR - how did we get here??')
    count += 1
    print(f'count = {count}, line = {washing_line}')

print('the end:', washing_line)
