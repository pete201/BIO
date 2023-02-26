"""string rewriting"""

debug = True

# first input 2 lines:
# a three letter string (where each letter will be A, B, C, D or E),
# 2 integers - 
# The first integer indicating the number of rewriting steps 
# the second indicating a position.


if debug:
    in_string = 'A'
    steps = 8
    position = 1000
else:
    in_string = input('Enter input characters: ')
    in_string = in_string.upper()
    steps = int(input('Enter steps: '))
    position = int(input('Enter position: '))

def mutate(in_char):
    out_char = in_char
    if in_char == 'A':
        out_char = 'B'

    if in_char == 'B':
        out_char = 'AB'

    if in_char == 'C':
        out_char = 'CD'

    if in_char == 'D':
        out_char = 'DC'

    if in_char == 'E':
        out_char = 'EE'

    return out_char

def count(char, string):
    return string.count(char)

def main():
    global in_string
    chars = 'ABCDE'
    print(f'input sting: {in_string}, steps: {steps}, position: {position}')
    

    for step in range(steps):
        output = ''
        for letter in in_string:
            output += mutate(letter)

        #if debug: print(f'step {step} output is: {output}')
        # truncation of in_string is necessary so that counts of 29 return in <2s
        in_string = output[:position]
    
    # truncate to p characters
    output = output[:position]
    #print(output)
    for each in chars:
        print(count(each, output), end=' ')
    print()
    

if __name__ == '__main__':
    main()