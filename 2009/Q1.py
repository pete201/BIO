debug = False

if debug:
    intext = 'BOUNCE'
else: intext = input('enter single word: ').upper()

print('finding digits in:', intext)

digits = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

def digit_in_word(digit, word):
    '''find list digit in list word'''
    #print(f'finding {digit} in {word}')
    
    if digit:
        d = digit.pop(0)
        w = ''
        while d != w:
            try: 
                w = word.pop(0)
            except IndexError: 
                return False
        result = digit_in_word(digit, word)
    else: result = True
    return result

result = 'No'
for index, digit in enumerate(digits):
    if digit_in_word(list(digit), list(intext)):
        result = index + 1
        break
print(result)
