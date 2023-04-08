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
# 1 - if [0] > [1] then leftmost
# else if [3] < [0] then mid_left
# else if [3] > [6] then mid-right
# else if (default) [6] < [3] rightmost
#NOPE - this does not work as a srategy :(

count = 0
while not (washing_line == '1234567') and count < max_count:
    if washing_line[0] > washing_line[1]: washing_line = leftmost(washing_line)
    elif washing_line[3] < washing_line[0]: washing_line =middle_left(washing_line)
    elif washing_line[3] > washing_line[4]: washing_line =middle_right(washing_line)
    else: washing_line = rightmost(washing_line)
    count += 1
    print(f'count = {count}, line = {washing_line}')

print('the end:', washing_line)