# input 9 characters

debug = False

if debug:
    input_string = 'EOOOOXXXX'
else:
    input_string = input('Enter valid start posn (e.g. EOOOOXXXX)')
    input_string = input_string.upper()

# turn string into list so we can manipulate it
input_list = []
for char in input_string:
    input_list.append(char)

#test
print(f'initial board layout is ', input_list)