'''Roman look and say'''

romans = ['0', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']

# in_string = input('enter a roman numerals number: ')
# in_string = in_string.upper()
# count = input('enter number between 1 and 50: ')
in_string = 'MMLXXXXXXXXX'
n = 3

print(f'roman numerals = {in_string} and n = {n}')
#print('\n\n',in_string)

length_in_string = len(in_string)
position = 0

# count same letter in a row

out_string = ''

for _ in range(n):
    out_string = ''
    while position < length_in_string:
        char_to_count = in_string[position]
        next_char = char_to_count
        counter = 0
        while next_char == char_to_count:
            counter += 1
            position += 1
            if position < length_in_string:
                next_char = in_string[position]
            else: break
            
        out_string = out_string + romans[counter] + in_string[position-1] 
    
    print(out_string)
    
    
    in_string = out_string
    length_in_string = len(in_string)
    position = 0

print(out_string.count('I'))
print(out_string.count('V'))