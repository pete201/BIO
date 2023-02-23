'''Enigma machine https://www.olympiad.org.uk/papers/2008/bio/bio08-exam.pdf Q2'''

debug = True
PORTS = 'ABCD'

if debug:
    encrypted_letters = 14
    word = 'AAABBB'
else:
    encrypted_letters = int(input('enter # letters already encrypted: '))
    word = input('enter word to be encrypted: ')
    word = word.upper()

class rotor():
    '''offsets input character in both left-right and right-left directions'''

    def __init__(self, off0, off1, off2, off3) -> None:
        '''set up the rotors offsets which are unique to each rotor'''
        self.left_offset_ref = [off0, off1, off2, off3]
        self.left_offset = self.left_offset_ref
        # set up right hand side based on LHS. 
        # basis is that LH_index + LtoR_value = RH_index
        # and now RtoL_value at RH-index = -LtoR_value
        # e.g. B=1, left_offset[1] = 1 : RH = 2 = C
        # so C = 2 has RtoL_value of -1
        self.right_offset_ref = [0,0,0,0]
        for index, value in enumerate(self.left_offset):
            RH_index = (index + value)%4
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

def create_reflector():
    reflector_offset = []
    for n in range(len(PORTS)):
        reflector_offset.append(len(PORTS) - 1 -(n*2))
    return reflector_offset


def main():
    global encrypted_letters
    encrypted_word = ''

    rotor1 = rotor(0, 2, -1, -1)
    rotor2 = rotor(0, 1, -1, 0)
    reflector1 = reflector()
        
    for char in word:
        rotor1.turn(encrypted_letters)
        # turns for second rotor is 'integer-divide' encrypted_letters
        rotor2.turn(encrypted_letters//4)

        step1 = rotor1.left_port(char)
        step2 = rotor2.left_port(step1)
        step3 = reflector1.reflect(step2)
        step4 = rotor2.right_port(step3)
        step5 = rotor1.right_port(step4)
        #print(f'{char} becomes {step5}')
        encrypted_word += step5

        encrypted_letters += 1

    print(f'encrypted word is: {encrypted_word}')




if __name__ == '__main__':
    main()