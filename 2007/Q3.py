"""string rewriting
8pm fri 17th"""

debug = True

# first input 2 lines:
# a three letter string (where each letter will be A, B, C, D or E),
# 2 integers - 
# The first integer s indicating the number of rewriting steps 
# the second p indicating a position.

# WORKS UNTIL s >= 29, then takes way more than 2s so fail!!

if debug:
    input = 'EEE'
    steps = 29
    position = 10

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
    global input
    chars = 'ABCDE'
    print(f'input sting was {input}')
    

    for step in range(steps):
        output = ''
        for letter in input:
            output += mutate(letter)

        print(f'step {step} output is: {output}')
        input = output
    
    # truncate to p characters
    output = output[:position]
    #print(output)
    for each in chars:
        print(count(each, output), end=' ')
    print()
    

if __name__ == '__main__':
    main()