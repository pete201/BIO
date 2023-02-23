'''files to create rotors and reflector for full alphabet'''
import random

PORTS = 'ABCD'

def create_reflector():
    reflector_offset = []
    if not len(PORTS)%2:
        for n in range(len(PORTS)):
            reflector_offset.append(len(PORTS) - 1 -(n*2))
    return reflector_offset

def create_rotor():
    left = string_to_list(PORTS)
    right = string_to_list(PORTS)
    rotor_offset = [0] * len(PORTS)
    
    while len(left):
        first = left.pop(random.randint(0, len(left)-1))
        second = right.pop(random.randint(0, len(right)-1))
        offset = PORTS.find(second) - PORTS.find(first)
        print(first, second, offset)
        rotor_offset[PORTS.find(first)] = offset
    return rotor_offset

def string_to_list(mystring):
    my_list = []
    for each in mystring:
        my_list.append(each)
    return my_list



def main():
    reflector_offset = create_reflector()
    print(f'reflector offset array = {reflector_offset}')

    print(create_rotor())


if __name__ == '__main__':
    main()