'''parking'''

debug = False

class cars():
    '''parameters for each car'''
    def __init__(self, name) -> None:
        self.name =  name
        self.position = 0
        self.preference_list = ''

    def add_preference(self, space):
        self.preference_list += str(space)

    def __str__(self) -> str:
        return self.name +' ' + str(self.position) + ' prefers space: ' + self.preference_list

    
if debug:
    parking_order = ['c','a','b','d']
    num_cars = len(parking_order)
    preference_index  = 5
else:
    # first input final parking arrangement string:
    parking_order = []
    next ='1'
    while next != '':
        next = input('input next parked car, <enter> to finish...\t')
        if next.isalnum and next !='':
            parking_order.append(next)
            print(f'cars parked so far: {parking_order}')
    # and input desired preference list number
    num_cars = len(parking_order)
    print(f'{num_cars} cars parked')
    preference_index = int(input(f'enter preference list between 1 and {num_cars}\t'))

print('parking order:',parking_order, '\npreference index required:', preference_index)


# get a list of cars in alphabetical order:
alphabet = parking_order.copy()
alphabet.sort()

# create car objects alphabetically, and populate with position
car_objects = []
for car in alphabet:
    new_car = cars(car)
    car_objects.append(new_car)
    # store car parked posiiton
    new_car.position = parking_order.index(car)

# initiate our street with no cars parked
street = []
for n in range(num_cars):
    street.append('')

# create preference list for each car
# this is based upon parked posn, + all preceeding contiguous occupied spaces in street
for next_car in car_objects:
    # add to street
    street[next_car.position] = next_car.name
    # starting at parked posn, itterate backwards through STREET to add occupied spaces
    i = int(next_car.position)
    while i > -1 and street[i] != '':
        next_car.add_preference(alphabet[i].capitalize())
        i -= 1

    
print('street:', street)

if debug:
    for each in car_objects:
        print(each)

# now combine preference lists from all cars into a list of preference lists
'''
start with car a
make n lists where n = len(car_a.preference_list)
append each list with first caracter of preference_list and remove that char
'''
# initiate with empty string
pref_strings_list = ['']
for car in car_objects:
    new_strings_list = []
    for stem in pref_strings_list:
        for char in car.preference_list:
            newstring = stem + char
            new_strings_list.append(newstring)
    pref_strings_list = new_strings_list

pref_strings_list.sort()

#if debug:
print(pref_strings_list)

# index starts from 0, so subtract 1 from requested preference item
print('Requested string is:',pref_strings_list[preference_index-1])