'''encryption'''

# I will start with an encrypter, which I will need to find encrypted stings
# and it seems an easier place to start

debug = True

alphabet = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# enter encrypted string...
if debug == True:
    #input_string = 'ENCRYPT'
    input_string = 'OLYMPIAD'
else:
    input_string = input('Enter an UPPERCASE word up to 10 letters...')

# convert input_string to list so that we can re-assign values
input_list = []
for letter in input_string:
    input_list.append(letter)


def letter_to_number(letter):
    return alphabet.find(letter)

def number_to_letter(num):
    return alphabet[num]

def encrypt(in_list):
    length = len(in_list)
    for n in range (1,length):
        # get number values for next 2 letters...
        e1 = letter_to_number(in_list[n-1])
        e2 = letter_to_number(in_list[n])
        sum = e1 + e2
        if sum >26:
            sum = sum -26
        in_list[n] = number_to_letter(sum)
    return in_list
    

def decrypt(in_list):
    length = len(in_list) - 1
    print('decrypt: lenght assignment:',length)
    for n in range(length,0,-1):
        # get number vlaues for 2 letters
        d1 = letter_to_number(in_list[n-1])
        d2 = letter_to_number(in_list[n])
        sum = d2 - d1
        if sum < 1:
            sum = sum + 26
        in_list[n] = number_to_letter(sum)
    return in_list

def rotate_encrypt(in_list):
    '''returns number of times a list can be encrypted before returning to original lsit'''
    original_list = input_list.copy()
    # do one encrypt, then keep going until output = input again
    count = 1
    result = encrypt(in_list)
    while result != original_list and count < 1000:
        count += 1
        result = encrypt(result)
    return count

result = encrypt(input_list)
print(result)

decrypt(result)
print(result)

print(rotate_encrypt(input_list))
print(input_list)