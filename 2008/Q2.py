'''Enigma machine https://www.olympiad.org.uk/papers/2008/bio/bio08-exam.pdf Q2'''

debug = False

# define PORTS to be all the available characters on our enigma keyboard
PORTS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .'
if len(PORTS)%2:
    print('PORTS must have an even number of characters. Quitting')
    exit()


class rotor():
    '''offsets input character in both left-right and right-left directions'''
    def __init__(self, *args) -> None:
        '''set up the rotors offsets which are unique to each rotor'''
        self.left_offset_ref = []
        for arg in args:
            self.left_offset_ref.append(arg)
        self.left_offset = self.left_offset_ref
        # set up right hand side based on LHS. 
        # basis is that LH_index + LtoR_value = RH_index
        # and now RtoL_value at RH-index = -LtoR_value
        # e.g. B=1, left_offset[1] = 1 : RH = 2 = C
        # so C = 2 has RtoL_value of -1
        self.right_offset_ref = [0] * len(self.left_offset_ref)
        for index, value in enumerate(self.left_offset):
            RH_index = (index + value)%len(self.left_offset)
            self.right_offset_ref[RH_index] = -value   
        self.right_offset = self.right_offset_ref  
        #print(f'rotor_init: left_offset = {self.left_offset}, right_offset = {self.right_offset}')

    def left_port(self, char_in):
        '''reads an input on left and outputs right port'''
        index = PORTS.find(char_in)
        translation = (index + self.left_offset[index])%len(PORTS)
        return PORTS[translation]

    def right_port(self, char_in):
        '''reads an input on right and outputs left port'''
        index = PORTS.find(char_in)
        translation = (index + self.right_offset[index])%len(PORTS)
        return PORTS[translation]

    def turn(self, n):
        '''rotates both the right and left port translations'''
        n = n%len(PORTS)
        # note that we always calculate from the static '_ref' arrays
        self.left_offset = self.left_offset_ref[n:] + self.left_offset_ref[:n]
        self.right_offset = self.right_offset_ref[n:] + self.right_offset_ref[:n] 
        #print(f'rotor_turn: left_offset = {self.left_offset}, right_offset = {self.right_offset}')
        return

class reflector():
    '''simple fixed translation of letters'''
    def __init__(self) -> None:
        self.reflector_offset = []
        if not len(PORTS)%2:
            for n in range(len(PORTS)):
                self.reflector_offset.append(len(PORTS) - 1 -(n*2))

    def reflect(self, char_in):
        index = PORTS.find(char_in)
        translation = (index + self.reflector_offset[index])
        return PORTS[translation]


class enigma():
    def __init__(self) -> None:
        # Note, new reflectors can be created using the helper file
        self.rotor1 = rotor(25, 20, 24, 15, 5, 11, -5, -5, 15, -4, 3, -4, -9, -5, 3, 5, 3, -17, -4, -15, -14, 3, 5, -8, -14, -13, -4, -16)
        self.rotor2 = rotor(24, 26, 6, 6, 1, 10, -5, 10, 2, -2, -6, -9, 10, -2, 11, -3, 3, 9, -5, -5, 3, -15, -1, -3, -6, -25, -23, -11)
        self.reflector1 = reflector()

    def encrypt_letter(self, letter, no_encrypted_letters):
        self.rotor1.turn(no_encrypted_letters)
        # turns for second rotor is 'integer-divide' num_encrypted_letters
        self.rotor2.turn(no_encrypted_letters//len(PORTS))

        step1 = self.rotor1.left_port(letter)
        step2 = self.rotor2.left_port(step1)
        step3 = self.reflector1.reflect(step2)
        step4 = self.rotor2.right_port(step3)
        step5 = self.rotor1.right_port(step4)
        #print(f'{char} becomes {step5}')
        return step5


def main():
    my_enigma = enigma()

    if debug:
        num_encrypted_letters = 14
        word = 'AAABBB'
    else:
        num_encrypted_letters = int(input('enter number of letters already encrypted: '))
        word = input('enter word to be encrypted: ')
        word = word.upper()

    encrypted_word = ''
    for char in word:
        encrypted_word += my_enigma.encrypt_letter(char, num_encrypted_letters)
        num_encrypted_letters += 1
    print(f'encrypted word is: {encrypted_word}')


if __name__ == '__main__':
    main()