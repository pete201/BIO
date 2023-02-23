'''files to create rotors for full alphabet.
Copy PORTS = from Q2 file (must be identical)
Run this file and copy resulting ROTOR offset into Q2 main at rotor init
'''
import random

PORTS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .'


def create_rotor():
    left = string_to_list(PORTS)
    right = string_to_list(PORTS)
    rotor_offset = [0] * len(PORTS)
    
    while len(left):
        first = left.pop(random.randint(0, len(left)-1))
        second = right.pop(random.randint(0, len(right)-1))
        offset = PORTS.find(second) - PORTS.find(first)
        #print(first, second, offset)
        rotor_offset[PORTS.find(first)] = offset
    return rotor_offset

def string_to_list(mystring):
    my_list = []
    for each in mystring:
        my_list.append(each)
    return my_list



def main():

    print(create_rotor())


if __name__ == '__main__':
    main()