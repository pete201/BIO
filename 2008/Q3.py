# i'll use a string instead of a list

debug = True

if debug:
    washing_line = "7654321"
else:
    washing_line = input("enter 7 digit number: ")


def leftmost(instring):
    outstring = instring[1:4] + instring[0] + instring[4:]
    return outstring

def rightmost(instring):
    outstring = instring[0:3] + instring[6] + instring[3:6]
    return outstring

def middle_left(instring):
    outstring = instring[3] + instring[0:3] + instring[4:]
    return outstring

def middle_right(instring):
    outstring = instring[0:3] + instring[4:] + instring[3]
    return outstring

print(f'original = {washing_line}')
washing_line = middle_right(washing_line)
print(washing_line)
