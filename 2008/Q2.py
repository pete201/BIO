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

    

    def __init__(self, off0, off1, off2, off3) -> None:
        '''set up the rotors offsets which are unique to each rotor'''
        self.left_offset = [off0, off1, off2, off3]
        self.port = 'ABCD'
        self.rotate_counter = 0
    
    def left_port(self, char_in):
        '''reads an input on left and outputs right port'''
        index = self.port.find(char_in)
        translation = index + self.left_offset[index]
        if translation > 3:
            translation -= 4
        return self.port[translation]

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