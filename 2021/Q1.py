'''testing strings for pats'''

alphabet = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def max_index(input_string):
    # returns int max index within string
    max = 0
    for char in input_string:
        index = alphabet.find(char)
        if index > max:
            max = index
    return max

def min_index(input_string):
    # returns int min index within string
    min = 26
    for char in input_string:
        index = alphabet.find(char)
        if index < min:
            min = index
    return min

def reverse(input_string):
    length = len(input_string)
    output_string = ''
    for n in range(length, 0, -1):
        output_string = output_string + input_string[n-1]
    return output_string

def is_a_pat(input_string):
    # split string from left from 1 to n-1 chars
    length = len(input_string)
    result = False
    if length < 2:
        result = True
    else:
        for slice in range(1, length):
            left = input_string[:slice]
            right = input_string[slice:]
            print(f"is_a_pat - input: {input_string}, left: {left}, right: {right}")
            # first test chars in left > chars in right
            if min_index(left) > max_index(right):
                # if TRUE, test if reverse stings are pats:
                left_reverse = reverse(left)
                right_reverse = reverse(right)
                # both of these must be a pat
                if is_a_pat(left_reverse):
                    print(f'is_a_pat_deep - {left} part of {input_string} is a pat')
                if is_a_pat(right_reverse):
                    print(f'is_a_pat_deep - {right} part of {input_string} is a pat')
                if is_a_pat(left_reverse) and is_a_pat(right_reverse):
                    result = True
            else: print(f'is_a_pat deep - {left}-{right} is not a pat')
    return result


# read in 2 strings, s1 and s2
s1 = input("input  first string - between 1 and 6 letters: ")
s1 = s1.upper()
s2 = input("input second string - between 1 and 6 letters: ")
s2 = s2.upper()
s1s2 = s1 + s2
print(f'\nmain - s1 is {s1}, s2 is {s2}, s1s2 is {s1s2}\n')

s1reverse = reverse(s1)
s2reverse = reverse(s2)

s1_min = min_index(s1)
s2_max = max_index(s2)


if is_a_pat(s1):
    print('main - S1 YES is a pat')
else: print('main - S1 NO')
print()

if is_a_pat(s2):
    print('main - S2 YES is a pat')
else: print('main - S2 NO')
print()

if is_a_pat(s1s2):
    print('main - S1S2 YES is a pat')
else: print('main - S1S2 NO')
exit()