'''Enigma machine'''

'''
use class for rotors:
    Left port (input), + offset = right port (output)
    has 'rotate' method which rotates the offset
    class has a rotate counter which is used to rotate next rotor
and a class for reflector:
    input translates to output
'''

debug = True

if debug:
    n = 14
    word = 'AAABBB'

class rotor():
    '''rotates offset after each use'''

    PORTS = 'ABCD'

    def __init__(self, off0, off1, off2, off3) -> None:
        '''set up the rotors offsets which are unique to each rotor'''
        self.left_offset = [off0, off1, off2, off3]
        self.rotate_counter = 0
        # set up right hand side based on LHS
        # basis is that LH_index+LtoR_value = RH_index
        # and now RtoL_value at RH-index = -LtoR_value
        # e.g. B=1, left_offset[1] = 1 : RH = 2 = C
        # so C = 2 has RtoL_value of -1
        self.right_offset = [0,0,0,0]
        for index, value in enumerate(self.left_offset):
            RH_index = (index + value)%4
            self.right_offset[RH_index] = -value       
        #print(f'rotor_init: left_offset = {self.left_offset}, right_offset = {self.right_offset}')


    
    def left_port(self, char_in):
        '''reads an input on left and outputs right port'''
        index = rotor.PORTS.find(char_in)
        translation = index + self.left_offset[index]
        if translation > 3:
            translation -= 4
        return rotor.PORTS[translation]

    def right_port(self):
        '''reads an input on right and outputs left port'''
        #TODO how do i reverse the offsets from right to left??

    def rotate(self):
        if self.rotate_counter > 4:
            self.rotate_counter = 0
        newOffset = []
        for index in range(4):
            new_index = index +1
            if new_index >3: 
                new_index = 0
            newOffset[new_index] = self.left_offset[index]
        self.left_offset = newOffset
        self.rotate_counter += 1
        return self.rotate_counter

class reflector():
    '''input translates to output'''
    def __init__(self) -> None:
        '''Only one static reflector, so set up here'''
        pass

def main():
    rotor1 = rotor(0, 2, -1, -1)
    rotor2 = rotor(0, 1, -1, 0)

    print(rotor1.left_port('D'))

    


if __name__ == '__main__':
    main()